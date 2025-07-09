"""
Fibre Bundle Quantization
========================

This module implements the quantization routines for the fibre bundles Θ/Ξ
in the Geometrodynamics of Entropy theory. It handles the quantum field theory
aspects of the extra dimensions and torsion field quantization.

Classes:
    FibreQuantization: Main quantization framework
    TorsionField: Torsion field operations
    QuantumOperator: Quantum operator algebra
    
Functions:
    quantize_field: Field quantization procedure
    compute_vacuum_state: Vacuum state computation
    torsion_propagator: Torsion field propagator
"""

import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh
from scipy.special import hermite
import warnings

class FibreQuantization:
    """
    Quantization framework for fibre bundle fields in extra dimensions.
    
    This class handles the canonical quantization of fields living on the
    compactified extra dimensions of the Camargo metric.
    """
    
    def __init__(self, metric_obj, cutoff_scale=1.8):
        """
        Initialize fibre quantization.
        
        Parameters:
        -----------
        metric_obj : CamargoMetric
            The metric object defining the geometry
        cutoff_scale : float
            UV cutoff scale in GeV
        """
        self.metric = metric_obj
        self.Lambda_cutoff = cutoff_scale
        self.hbar = 1.0  # Natural units
        
        # Fibre parameters
        self.n_modes_theta = 100  # Number of modes in θ direction
        self.n_modes_xi = 100     # Number of modes in ξ direction
        
        # Quantization parameters
        self.field_normalization = 1.0 / np.sqrt(2 * np.pi)
        
    def mode_functions_theta(self, n, theta):
        """
        Compute mode functions for θ direction.
        
        Parameters:
        -----------
        n : int
            Mode number
        theta : float or array
            θ coordinate
            
        Returns:
        --------
        mode_fn : float or array
            Mode function value
        """
        # Harmonic oscillator basis on compactified dimension
        L_theta = 2 * np.pi * self.metric.R2
        omega_n = np.sqrt(n + 0.5) / self.metric.R2
        
        # Normalized mode function
        norm_factor = np.sqrt(omega_n / (np.pi * self.hbar))
        
        # Gaussian envelope with polynomial
        xi_theta = theta / self.metric.R2
        exp_factor = np.exp(-omega_n * xi_theta**2 / (2 * self.hbar))
        
        # Hermite polynomial
        H_n = hermite(n)
        poly_factor = H_n(np.sqrt(omega_n / self.hbar) * xi_theta)
        
        return norm_factor * poly_factor * exp_factor
    
    def mode_functions_xi(self, m, xi):
        """
        Compute mode functions for ξ direction.
        
        Parameters:
        -----------
        m : int
            Mode number
        xi : float or array
            ξ coordinate
            
        Returns:
        --------
        mode_fn : float or array
            Mode function value
        """
        # Similar to theta but for ξ dimension
        L_xi = 2 * np.pi * self.metric.R3
        omega_m = np.sqrt(m + 0.5) / self.metric.R3
        
        norm_factor = np.sqrt(omega_m / (np.pi * self.hbar))
        
        xi_xi = xi / self.metric.R3
        exp_factor = np.exp(-omega_m * xi_xi**2 / (2 * self.hbar))
        
        H_m = hermite(m)
        poly_factor = H_m(np.sqrt(omega_m / self.hbar) * xi_xi)
        
        return norm_factor * poly_factor * exp_factor
    
    def energy_spectrum(self, n_max=None):
        """
        Compute the energy spectrum of quantized modes.
        
        Parameters:
        -----------
        n_max : int, optional
            Maximum mode number to compute
            
        Returns:
        --------
        energies : dict
            Dictionary with energy levels for each mode
        """
        if n_max is None:
            n_max = min(self.n_modes_theta, self.n_modes_xi)
        
        energies = {
            'theta_modes': [],
            'xi_modes': [],
            'total_modes': []
        }
        
        # Theta mode energies
        for n in range(n_max):
            E_n = self.hbar * np.sqrt(n + 0.5) / self.metric.R2
            energies['theta_modes'].append(E_n)
        
        # Xi mode energies
        for m in range(n_max):
            E_m = self.hbar * np.sqrt(m + 0.5) / self.metric.R3
            energies['xi_modes'].append(E_m)
        
        # Combined mode energies
        for n in range(n_max):
            for m in range(n_max):
                E_nm = (self.hbar * np.sqrt(n + 0.5) / self.metric.R2 +
                       self.hbar * np.sqrt(m + 0.5) / self.metric.R3)
                energies['total_modes'].append(E_nm)
        
        return energies
    
    def vacuum_state(self, coordinates):
        """
        Compute the vacuum state of the quantized field.
        
        Parameters:
        -----------
        coordinates : array-like
            6D coordinates
            
        Returns:
        --------
        vacuum_amplitude : complex
            Vacuum state amplitude
        """
        t, x, y, z, theta, xi = coordinates
        
        # Vacuum state is product of ground states
        vacuum_theta = self.mode_functions_theta(0, theta)
        vacuum_xi = self.mode_functions_xi(0, xi)
        
        # Phase factor from time evolution
        E_0 = (self.hbar * 0.5 / self.metric.R2 + 
               self.hbar * 0.5 / self.metric.R3)
        
        time_evolution = np.exp(-1j * E_0 * t / self.hbar)
        
        return vacuum_theta * vacuum_xi * time_evolution
    
    def field_operator(self, coordinates, creation_ops, annihilation_ops):
        """
        Construct the field operator from creation/annihilation operators.
        
        Parameters:
        -----------
        coordinates : array-like
            6D coordinates
        creation_ops : dict
            Creation operators for each mode
        annihilation_ops : dict
            Annihilation operators for each mode
            
        Returns:
        --------
        field_op : complex
            Field operator value
        """
        t, x, y, z, theta, xi = coordinates
        
        field_op = 0.0
        
        # Sum over all modes
        for n in range(self.n_modes_theta):
            for m in range(self.n_modes_xi):
                # Mode energy
                E_nm = (self.hbar * np.sqrt(n + 0.5) / self.metric.R2 +
                       self.hbar * np.sqrt(m + 0.5) / self.metric.R3)
                
                # Mode functions
                u_nm = (self.mode_functions_theta(n, theta) *
                       self.mode_functions_xi(m, xi))
                
                # Time evolution
                time_factor = np.exp(-1j * E_nm * t / self.hbar)
                
                # Field operator expansion
                mode_key = f"({n},{m})"
                if mode_key in annihilation_ops:
                    field_op += (annihilation_ops[mode_key] * u_nm * time_factor +
                               creation_ops[mode_key] * np.conj(u_nm) * np.conj(time_factor))
        
        return field_op

class TorsionField:
    """
    Torsion field operations and quantization.
    
    This class handles the torsion field that arises from the non-trivial
    geometry of the compactified extra dimensions.
    """
    
    def __init__(self, metric_obj, coupling_constant=1.0):
        """
        Initialize torsion field.
        
        Parameters:
        -----------
        metric_obj : CamargoMetric
            The metric object
        coupling_constant : float
            Torsion coupling constant κ
        """
        self.metric = metric_obj
        self.kappa = coupling_constant
        
        # Torsion field parameters
        self.field_mass = 0.0  # Massless torsion field
        self.spin = 1  # Vector field
        
    def torsion_potential(self, coordinates):
        """
        Compute the torsion potential at given coordinates.
        
        Parameters:
        -----------
        coordinates : array-like
            6D coordinates
            
        Returns:
        --------
        potential : float
            Torsion potential value
        """
        t, x, y, z, theta, xi = coordinates
        
        # Potential depends on extra dimension coordinates
        V_theta = self.kappa * np.cos(theta / self.metric.R2)
        V_xi = self.kappa * np.cos(xi / self.metric.R3)
        
        # Cross-coupling term
        V_cross = self.kappa * np.sin(theta / self.metric.R2 + xi / self.metric.R3)
        
        return V_theta + V_xi + V_cross
    
    def propagator(self, k_vector, regularization=True):
        """
        Compute the torsion field propagator in momentum space.
        
        Parameters:
        -----------
        k_vector : array-like
            6D momentum vector
        regularization : bool
            Whether to apply UV regularization
            
        Returns:
        --------
        propagator : complex
            Torsion field propagator
        """
        k_squared = np.sum(k_vector**2)
        
        # Massless propagator
        prop = -1j / (k_squared + 1j * 1e-10)  # Small imaginary part for stability
        
        # UV regularization
        if regularization and k_squared > self.metric.Lambda_tau**2:
            cutoff_factor = np.exp(-(k_squared - self.metric.Lambda_tau**2) / self.metric.Lambda_tau**2)
            prop *= cutoff_factor
        
        return prop
    
    def interaction_vertex(self, coordinates):
        """
        Compute the torsion-matter interaction vertex.
        
        Parameters:
        -----------
        coordinates : array-like
            6D coordinates
            
        Returns:
        --------
        vertex : ndarray
            Interaction vertex tensor
        """
        torsion_tensor = self.metric.torsion_tensor(coordinates)
        
        # Vertex factor includes torsion tensor and coupling
        vertex = self.kappa * torsion_tensor
        
        return vertex

class QuantumOperator:
    """
    Quantum operator algebra for the fibre bundle fields.
    """
    
    def __init__(self, n_modes):
        """
        Initialize quantum operator algebra.
        
        Parameters:
        -----------
        n_modes : int
            Number of modes to include
        """
        self.n_modes = n_modes
        self.operators = {}
        
    def creation_operator(self, mode_indices):
        """
        Create a creation operator for given mode.
        
        Parameters:
        -----------
        mode_indices : tuple
            Mode indices (n, m)
            
        Returns:
        --------
        operator : dict
            Creation operator representation
        """
        key = f"a_dag_{mode_indices}"
        self.operators[key] = {
            'type': 'creation',
            'mode': mode_indices,
            'norm': 1.0
        }
        
        return self.operators[key]
    
    def annihilation_operator(self, mode_indices):
        """
        Create an annihilation operator for given mode.
        
        Parameters:
        -----------
        mode_indices : tuple
            Mode indices (n, m)
            
        Returns:
        --------
        operator : dict
            Annihilation operator representation
        """
        key = f"a_{mode_indices}"
        self.operators[key] = {
            'type': 'annihilation',
            'mode': mode_indices,
            'norm': 1.0
        }
        
        return self.operators[key]
    
    def commutator(self, op1, op2):
        """
        Compute commutator between two operators.
        
        Parameters:
        -----------
        op1, op2 : dict
            Operator representations
            
        Returns:
        --------
        commutator : float
            Commutator value (for canonical operators)
        """
        if (op1['type'] == 'annihilation' and op2['type'] == 'creation' and
            op1['mode'] == op2['mode']):
            return 1.0
        elif (op1['type'] == 'creation' and op2['type'] == 'annihilation' and
              op1['mode'] == op2['mode']):
            return -1.0
        else:
            return 0.0

def quantize_field(metric_obj, field_type='scalar', cutoff_scale=1.8):
    """
    Quantize a field on the fibre bundle.
    
    Parameters:
    -----------
    metric_obj : CamargoMetric
        The metric object
    field_type : str
        Type of field to quantize ('scalar', 'vector', 'tensor')
    cutoff_scale : float
        UV cutoff scale
        
    Returns:
    --------
    quantized_field : FibreQuantization
        Quantized field object
    """
    return FibreQuantization(metric_obj, cutoff_scale)

def compute_vacuum_state(quantized_field, coordinates):
    """
    Compute the vacuum state of a quantized field.
    
    Parameters:
    -----------
    quantized_field : FibreQuantization
        Quantized field object
    coordinates : array-like
        6D coordinates
        
    Returns:
    --------
    vacuum : complex
        Vacuum state amplitude
    """
    return quantized_field.vacuum_state(coordinates)

def torsion_propagator(metric_obj, k_vector):
    """
    Compute the torsion field propagator.
    
    Parameters:
    -----------
    metric_obj : CamargoMetric
        The metric object
    k_vector : array-like
        6D momentum vector
        
    Returns:
    --------
    propagator : complex
        Torsion propagator
    """
    torsion_field = TorsionField(metric_obj)
    return torsion_field.propagator(k_vector)
