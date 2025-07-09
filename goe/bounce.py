"""
Friedmann-Cartan Integrator
===========================

This module implements the Friedmann-Cartan integrator (EGE-7) that forms
the basis of all cosmological predictions in the Geometrodynamics of Entropy theory.

The integrator solves the modified Friedmann equations with torsion terms
and handles the Big Bounce scenario with oscillatory behavior.

Classes:
    FriedmannCartan: Main integrator class
    CosmologicalBounce: Bounce dynamics implementation
    ScaleFactor: Scale factor evolution
    
Functions:
    integrate_friedmann: Main integration routine
    bounce_dynamics: Bounce phase evolution
    cosmic_evolution: Full cosmic evolution from bounce to present
"""

import numpy as np
from scipy.integrate import odeint, solve_ivp
from scipy.optimize import fsolve
import warnings

class FriedmannCartan:
    """
    Friedmann-Cartan integrator for modified cosmological equations.
    
    This class implements the solution of the modified Friedmann equations
    that include torsion terms from the compactified extra dimensions.
    """
    
    def __init__(self, metric_obj, initial_conditions=None):
        """
        Initialize the Friedmann-Cartan integrator.
        
        Parameters:
        -----------
        metric_obj : CamargoMetric
            The metric object defining the geometry
        initial_conditions : dict, optional
            Initial conditions for integration
        """
        self.metric = metric_obj
        
        # Standard cosmological parameters
        self.H0 = 67.0  # km/s/Mpc
        self.Omega_m = 0.31
        self.Omega_Lambda = 0.69
        self.Omega_r = 5.4e-5  # Radiation density
        
        # GoE-specific parameters
        self.z_bounce = 1e6  # Bounce redshift
        self.alpha_torsion = 0.03  # Torsion amplitude
        self.delta_bounce = 0.001  # Bounce oscillation amplitude
        
        # Initial conditions
        if initial_conditions is None:
            self.initial_conditions = {
                'a_initial': 1e-6,  # Initial scale factor
                'H_initial': 1e6,   # Initial Hubble parameter
                'phi_initial': 0.0,  # Initial scalar field
                'dphi_initial': 0.0  # Initial scalar field derivative
            }
        else:
            self.initial_conditions = initial_conditions
        
        # Integration parameters
        self.t_span = (0, 13.8e9)  # 0 to present age in years
        self.n_points = 10000
        
    def friedmann_equations(self, t, y):
        """
        Define the modified Friedmann equations with torsion.
        
        Parameters:
        -----------
        t : float
            Time coordinate
        y : array-like
            State vector [a, H, phi, dphi]
            
        Returns:
        --------
        dydt : array-like
            Time derivatives of state variables
        """
        a, H, phi, dphi = y
        
        # Prevent division by zero
        if a <= 0:
            a = 1e-10
        
        # Hubble parameter in terms of scale factor
        H_calculated = np.sqrt(
            (8 * np.pi * self.G_newton / 3) * (
                self.rho_matter(a) + self.rho_radiation(a) + 
                self.rho_lambda(a) + self.rho_torsion(a, phi)
            )
        )
        
        # Scale factor evolution
        dadt = a * H
        
        # Hubble parameter evolution
        dHdt = -0.5 * (8 * np.pi * self.G_newton) * (
            self.rho_matter(a) + self.rho_radiation(a) + 
            3 * self.rho_lambda(a) + self.pressure_torsion(a, phi)
        )
        
        # Scalar field evolution (torsion field)
        dphidt = dphi
        
        # Scalar field acceleration with torsion coupling
        d2phidt2 = -3 * H * dphi - self.torsion_potential_derivative(phi)
        
        return np.array([dadt, dHdt, dphidt, d2phidt2])
    
    def rho_matter(self, a):
        """
        Matter density as function of scale factor.
        
        Parameters:
        -----------
        a : float
            Scale factor
            
        Returns:
        --------
        rho_m : float
            Matter density
        """
        return self.Omega_m * self.H0**2 / (8 * np.pi * self.G_newton) * a**(-3)
    
    def rho_radiation(self, a):
        """
        Radiation density as function of scale factor.
        
        Parameters:
        -----------
        a : float
            Scale factor
            
        Returns:
        --------
        rho_r : float
            Radiation density
        """
        return self.Omega_r * self.H0**2 / (8 * np.pi * self.G_newton) * a**(-4)
    
    def rho_lambda(self, a):
        """
        Dark energy density (cosmological constant).
        
        Parameters:
        -----------
        a : float
            Scale factor
            
        Returns:
        --------
        rho_lambda : float
            Dark energy density
        """
        return self.Omega_Lambda * self.H0**2 / (8 * np.pi * self.G_newton)
    
    def rho_torsion(self, a, phi):
        """
        Torsion energy density.
        
        Parameters:
        -----------
        a : float
            Scale factor
        phi : float
            Torsion field value
            
        Returns:
        --------
        rho_torsion : float
            Torsion energy density
        """
        # Torsion energy density with oscillatory behavior
        oscillation = np.sin(phi * np.sqrt(self.metric.alpha) / self.metric.R2)
        
        base_density = self.alpha_torsion * self.H0**2 / (8 * np.pi * self.G_newton)
        
        return base_density * (1 + self.delta_bounce * oscillation) * a**(-6)
    
    def pressure_torsion(self, a, phi):
        """
        Torsion pressure.
        
        Parameters:
        -----------
        a : float
            Scale factor
        phi : float
            Torsion field value
            
        Returns:
        --------
        p_torsion : float
            Torsion pressure
        """
        # Torsion pressure with equation of state w = -1/3
        return -self.rho_torsion(a, phi) / 3
    
    def torsion_potential_derivative(self, phi):
        """
        Derivative of torsion potential.
        
        Parameters:
        -----------
        phi : float
            Torsion field value
            
        Returns:
        --------
        dV_dphi : float
            Potential derivative
        """
        return (self.alpha_torsion * np.sqrt(self.metric.alpha) / self.metric.R2 * 
                np.cos(phi * np.sqrt(self.metric.alpha) / self.metric.R2))
    
    @property
    def G_newton(self):
        """Newton's gravitational constant in natural units."""
        return 6.67e-11 * (3.086e22)**2 / (1.989e30)  # Converted to cosmological units
    
    def integrate(self, t_span=None, method='RK45'):
        """
        Integrate the Friedmann-Cartan equations.
        
        Parameters:
        -----------
        t_span : tuple, optional
            Time span for integration
        method : str
            Integration method
            
        Returns:
        --------
        solution : dict
            Integration solution
        """
        if t_span is None:
            t_span = self.t_span
        
        # Initial conditions vector
        y0 = np.array([
            self.initial_conditions['a_initial'],
            self.initial_conditions['H_initial'],
            self.initial_conditions['phi_initial'],
            self.initial_conditions['dphi_initial']
        ])
        
        # Solve the system
        try:
            sol = solve_ivp(self.friedmann_equations, t_span, y0, 
                           method=method, dense_output=True, 
                           rtol=1e-8, atol=1e-10)
            
            # Extract solution
            t_eval = np.linspace(t_span[0], t_span[1], self.n_points)
            y_eval = sol.sol(t_eval)
            
            solution = {
                't': t_eval,
                'a': y_eval[0],
                'H': y_eval[1], 
                'phi': y_eval[2],
                'dphi': y_eval[3],
                'success': sol.success,
                'message': sol.message
            }
            
            # Calculate derived quantities
            solution['z'] = 1/solution['a'] - 1  # Redshift
            solution['rho_total'] = np.array([
                self.rho_matter(a) + self.rho_radiation(a) + 
                self.rho_lambda(a) + self.rho_torsion(a, phi)
                for a, phi in zip(solution['a'], solution['phi'])
            ])
            
            return solution
            
        except Exception as e:
            warnings.warn(f"Integration failed: {e}")
            return None

class CosmologicalBounce:
    """
    Implementation of the Big Bounce scenario in GoE cosmology.
    
    This class handles the transition from contraction to expansion
    and the oscillatory behavior around the bounce point.
    """
    
    def __init__(self, friedmann_integrator):
        """
        Initialize the cosmological bounce.
        
        Parameters:
        -----------
        friedmann_integrator : FriedmannCartan
            The Friedmann integrator object
        """
        self.integrator = friedmann_integrator
        self.bounce_scale = 1e-6  # Minimum scale factor at bounce
        self.bounce_time = 0.0    # Time of bounce
        
    def bounce_conditions(self, a, H, phi):
        """
        Determine bounce conditions.
        
        Parameters:
        -----------
        a : float
            Scale factor
        H : float
            Hubble parameter
        phi : float
            Torsion field
            
        Returns:
        --------
        is_bounce : bool
            Whether bounce conditions are met
        """
        # Bounce occurs when Hubble parameter changes sign
        # and scale factor reaches minimum
        return (H > 0 and a <= self.bounce_scale)
    
    def pre_bounce_evolution(self, t_span_pre):
        """
        Evolution before the bounce (contraction phase).
        
        Parameters:
        -----------
        t_span_pre : tuple
            Time span for pre-bounce evolution
            
        Returns:
        --------
        pre_solution : dict
            Pre-bounce solution
        """
        # Modified initial conditions for contraction
        initial_conditions_pre = {
            'a_initial': 1.0,         # Start from large scale factor
            'H_initial': -1e2,        # Negative Hubble (contraction)
            'phi_initial': 0.0,
            'dphi_initial': 0.0
        }
        
        # Temporary change of initial conditions
        original_ic = self.integrator.initial_conditions
        self.integrator.initial_conditions = initial_conditions_pre
        
        # Integrate pre-bounce phase
        pre_solution = self.integrator.integrate(t_span_pre)
        
        # Restore original initial conditions
        self.integrator.initial_conditions = original_ic
        
        return pre_solution
    
    def post_bounce_evolution(self, t_span_post):
        """
        Evolution after the bounce (expansion phase).
        
        Parameters:
        -----------
        t_span_post : tuple
            Time span for post-bounce evolution
            
        Returns:
        --------
        post_solution : dict
            Post-bounce solution
        """
        # Use standard initial conditions for expansion
        return self.integrator.integrate(t_span_post)
    
    def full_bounce_evolution(self):
        """
        Complete evolution through bounce.
        
        Returns:
        --------
        full_solution : dict
            Complete bounce evolution
        """
        # Pre-bounce phase
        t_pre = (-1e6, 0)  # Before bounce
        pre_solution = self.pre_bounce_evolution(t_pre)
        
        # Post-bounce phase
        t_post = (0, 13.8e9)  # After bounce to present
        post_solution = self.post_bounce_evolution(t_post)
        
        # Combine solutions
        if pre_solution and post_solution:
            full_solution = {
                't': np.concatenate([pre_solution['t'], post_solution['t']]),
                'a': np.concatenate([pre_solution['a'], post_solution['a']]),
                'H': np.concatenate([pre_solution['H'], post_solution['H']]),
                'phi': np.concatenate([pre_solution['phi'], post_solution['phi']]),
                'z': np.concatenate([pre_solution['z'], post_solution['z']])
            }
            return full_solution
        
        return None

class ScaleFactor:
    """
    Scale factor evolution utilities.
    """
    
    @staticmethod
    def redshift_to_scale_factor(z):
        """
        Convert redshift to scale factor.
        
        Parameters:
        -----------
        z : float or array
            Redshift
            
        Returns:
        --------
        a : float or array
            Scale factor
        """
        return 1 / (1 + z)
    
    @staticmethod
    def scale_factor_to_redshift(a):
        """
        Convert scale factor to redshift.
        
        Parameters:
        -----------
        a : float or array
            Scale factor
            
        Returns:
        --------
        z : float or array
            Redshift
        """
        return 1/a - 1
    
    @staticmethod
    def lookback_time(z, H0=67.0, Omega_m=0.31, Omega_Lambda=0.69):
        """
        Calculate lookback time for given redshift.
        
        Parameters:
        -----------
        z : float or array
            Redshift
        H0 : float
            Hubble constant
        Omega_m : float
            Matter density parameter
        Omega_Lambda : float
            Dark energy density parameter
            
        Returns:
        --------
        t_lookback : float or array
            Lookback time in years
        """
        def integrand(z_prime):
            return 1 / ((1 + z_prime) * np.sqrt(
                Omega_m * (1 + z_prime)**3 + Omega_Lambda
            ))
        
        # Hubble time
        t_H = 9.78e9 / (H0 / 100)  # Years
        
        if np.isscalar(z):
            integral, _ = quad(integrand, 0, z)
            return t_H * integral
        else:
            results = []
            for z_val in z:
                integral, _ = quad(integrand, 0, z_val)
                results.append(t_H * integral)
            return np.array(results)

def integrate_friedmann(metric_obj, initial_conditions=None, t_span=None):
    """
    Convenience function to integrate Friedmann equations.
    
    Parameters:
    -----------
    metric_obj : CamargoMetric
        The metric object
    initial_conditions : dict, optional
        Initial conditions
    t_span : tuple, optional
        Time span for integration
        
    Returns:
    --------
    solution : dict
        Integration solution
    """
    integrator = FriedmannCartan(metric_obj, initial_conditions)
    return integrator.integrate(t_span)

def bounce_dynamics(friedmann_integrator):
    """
    Compute bounce dynamics.
    
    Parameters:
    -----------
    friedmann_integrator : FriedmannCartan
        The Friedmann integrator
        
    Returns:
    --------
    bounce_solution : dict
        Bounce dynamics solution
    """
    bounce = CosmologicalBounce(friedmann_integrator)
    return bounce.full_bounce_evolution()

def cosmic_evolution(metric_obj, include_bounce=True):
    """
    Compute full cosmic evolution from bounce to present.
    
    Parameters:
    -----------
    metric_obj : CamargoMetric
        The metric object
    include_bounce : bool
        Whether to include bounce dynamics
        
    Returns:
    --------
    evolution : dict
        Full cosmic evolution
    """
    integrator = FriedmannCartan(metric_obj)
    
    if include_bounce:
        bounce = CosmologicalBounce(integrator)
        return bounce.full_bounce_evolution()
    else:
        return integrator.integrate()
