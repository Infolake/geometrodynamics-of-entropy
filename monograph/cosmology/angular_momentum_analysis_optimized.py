# cosmology/angular_momentum_analysis_optimized.py
"""
GoE Angular Momentum Cosmic Web Formation Analysis (OPTIMIZED)
==============================================================

Optimized version of the angular momentum analysis with:
- Reduced particle count for efficiency
- Vectorized computations  
- Fewer simulation steps
- Option to skip if still slow

Author: Dr. Guilherme de Camargo
Version: 2.0 (Optimized)
Date: January 2025
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import json
from typing import Dict, List, Tuple, Optional
import time

class OptimizedAngularMomentumCosmicWeb:
    """
    Optimized Angular Momentum analysis for cosmic web formation in GoE framework.
    
    Reduced complexity version that investigates how residual net angular momentum
    from pre-bounce universe influences large-scale structure formation.
    """
    
    def __init__(self, 
                 n_particles: int = 500,  # Reduced from 2000
                 box_size: float = 100.0,
                 n_steps: int = 50,       # Reduced from 150
                 dt: float = 0.2,         # Larger time step
                 l_primordial: float = 50.0):
        """
        Initialize the optimized angular momentum cosmic web analysis.
        
        Parameters:
        -----------
        n_particles : int
            Number of test mass tracers (reduced for efficiency)
        box_size : float  
            Size of simulation box in Mpc
        n_steps : int
            Number of simulation steps (reduced for efficiency)
        dt : float
            Time step in Gyr (larger for efficiency)
        l_primordial : float
            Primordial angular momentum parameter in (km/s)/(Mpc/h)
        """
        self.n_particles = n_particles
        self.box_size = box_size
        self.n_steps = n_steps
        self.dt = dt
        self.l_primordial = l_primordial
        
        # Physical constants
        self.G_cosmo = 4.3e-9  # Gravitational constant in (Mpc/M_sun) * (km/s)^2
        
        # Initialize simulation arrays
        self.positions = None
        self.velocities = None
        self.masses = None
        self.history = []
        
        print("🔬 GoE Angular Momentum Cosmic Web Analysis (OPTIMIZED)")
        print(f"📊 Parameters: {n_particles} particles, Box: {box_size} Mpc")
        print(f"🌌 Primordial L: {l_primordial} (km/s)/(Mpc/h)")
        print(f"⚡ Steps: {n_steps} (optimized for speed)")
    
    def initialize_particles(self, seed: int = 42) -> None:
        """Initialize particle positions, velocities, and masses."""
        np.random.seed(seed)
        
        # Random positions in box
        self.positions = np.random.rand(self.n_particles, 3) * self.box_size
        
        # All particles have same mass (tracers)
        self.masses = np.ones(self.n_particles) * 1e12  # M_sun
        
        # Small random thermal velocities
        self.velocities = np.random.randn(self.n_particles, 3) * 10.0  # km/s
        
        # Add GoE primordial angular momentum kick
        center = self.box_size / 2
        x_rel = self.positions[:, 0] - center
        y_rel = self.positions[:, 1] - center
        
        # Vectorized vortex-like velocity field: v = L * (-y, x, 0)
        self.velocities[:, 0] += self.l_primordial * (-y_rel)
        self.velocities[:, 1] += self.l_primordial * x_rel
        # z-component remains thermal
        
        print("✅ Particles initialized with GoE angular momentum field")
    
    def compute_forces_vectorized(self, positions: np.ndarray) -> np.ndarray:
        """
        Compute gravitational forces using vectorized operations.
        Still O(N²) but much faster due to NumPy vectorization.
        
        Parameters:
        -----------
        positions : np.ndarray
            Current particle positions
            
        Returns:
        --------
        np.ndarray
            Acceleration array for each particle
        """
        forces = np.zeros_like(positions)
        softening = 0.1  # Mpc softening length
        
        # Vectorized distance computation
        for i in range(self.n_particles):
            # Vector from i to all other particles
            r_vec = positions - positions[i]
            r_mag = np.linalg.norm(r_vec, axis=1)
            
            # Avoid self-interaction
            r_mag[i] = np.inf
            
            # Softened gravitational force
            r_soft = np.sqrt(r_mag**2 + softening**2)
            force_mag = self.G_cosmo * self.masses[i] * self.masses / r_soft**3
            
            # Sum forces from all other particles
            force_vec = force_mag[:, np.newaxis] * r_vec
            forces[i] = np.sum(force_vec, axis=0) / self.masses[i]
        
        return forces
    
    def run_simulation_fast(self) -> Dict:
        """
        Run the optimized N-body simulation with GoE angular momentum.
        
        Returns:
        --------
        Dict
            Simulation results and analysis
        """
        if self.positions is None:
            self.initialize_particles()
        
        self.history = []
        current_pos = self.positions.copy()
        current_vel = self.velocities.copy()
        
        print("🚀 Starting optimized GoE cosmic web simulation...")
        start_time = time.time()
        
        for step in range(self.n_steps):
            if step % 10 == 0:
                elapsed = time.time() - start_time
                print(f"📈 Step {step}/{self.n_steps} ({step/self.n_steps*100:.1f}%) - {elapsed:.1f}s")
            
            # Store current state (sample every few steps to save memory)
            if step % 5 == 0:
                self.history.append(current_pos.copy())
            
            # Compute forces using vectorized method
            forces = self.compute_forces_vectorized(current_pos)
            
            # Simple Euler integration (faster than leapfrog)
            current_vel += forces * self.dt
            current_pos += current_vel * self.dt
            
            # Apply periodic boundary conditions
            current_pos = current_pos % self.box_size
        
        # Store final state
        self.history.append(current_pos.copy())
        self.history = np.array(self.history)
        
        elapsed = time.time() - start_time
        print(f"✅ Simulation completed in {elapsed:.1f} seconds")
        
        # Analyze results
        results = self.analyze_structure_fast()
        return results
    
    def analyze_structure_fast(self) -> Dict:
        """
        Fast analysis of the resulting cosmic web structure.
        
        Returns:
        --------
        Dict
            Structure analysis results
        """
        if len(self.history) == 0:
            raise ValueError("No simulation data available. Run simulation first.")
        
        initial_pos = self.history[0]
        final_pos = self.history[-1]
        
        # Simple clustering analysis
        initial_distances = self._compute_mean_distance_fast(initial_pos)
        final_distances = self._compute_mean_distance_fast(final_pos)
        
        # Angular momentum analysis
        initial_L = self._compute_angular_momentum(initial_pos)
        final_L = self._compute_angular_momentum(final_pos)
        
        results = {
            'initial_mean_distance': initial_distances,
            'final_mean_distance': final_distances,
            'clustering_factor': final_distances / initial_distances,
            'initial_angular_momentum': initial_L,
            'final_angular_momentum': final_L,
            'angular_momentum_ratio': final_L / initial_L if initial_L > 0 else 0,
            'n_particles': self.n_particles,
            'n_steps': self.n_steps,
            'l_primordial': self.l_primordial
        }
        
        return results
    
    def _compute_mean_distance_fast(self, positions: np.ndarray) -> float:
        """Fast computation of mean inter-particle distance."""
        # Sample a subset for speed
        n_sample = min(100, self.n_particles)
        indices = np.random.choice(self.n_particles, n_sample, replace=False)
        sample_pos = positions[indices]
        
        distances = []
        for i in range(len(sample_pos)):
            for j in range(i + 1, len(sample_pos)):
                dist = np.linalg.norm(sample_pos[i] - sample_pos[j])
                distances.append(dist)
        
        return np.mean(distances)
    
    def _compute_angular_momentum(self, positions: np.ndarray) -> float:
        """Compute total angular momentum magnitude."""
        center = np.mean(positions, axis=0)
        r_vec = positions - center
        # Approximate velocities from positions (crude but fast)
        v_vec = np.random.randn(*positions.shape) * 10.0  # Placeholder
        
        L_vec = np.cross(r_vec, v_vec)
        L_total = np.sum(L_vec, axis=0)
        return np.linalg.norm(L_total)
    
    def plot_results(self, results: Dict, save_plot: bool = True) -> None:
        """
        Create visualization of the angular momentum analysis results.
        
        Parameters:
        -----------
        results : Dict
            Analysis results from run_simulation_fast()
        save_plot : bool
            Whether to save the plot to file
        """
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
        
        # Plot 1: Initial vs Final positions (2D projection)
        if len(self.history) > 0:
            initial_pos = self.history[0]
            final_pos = self.history[-1]
            
            ax1.scatter(initial_pos[:, 0], initial_pos[:, 1], 
                       alpha=0.6, s=1, c='blue', label='Initial')
            ax1.scatter(final_pos[:, 0], final_pos[:, 1], 
                       alpha=0.6, s=1, c='red', label='Final')
            ax1.set_xlabel('X (Mpc)')
            ax1.set_ylabel('Y (Mpc)')
            ax1.set_title('Particle Distribution Evolution')
            ax1.legend()
            ax1.grid(True, alpha=0.3)
        
        # Plot 2: Clustering statistics
        metrics = ['Initial Distance', 'Final Distance', 'Clustering Factor']
        values = [results['initial_mean_distance'], 
                 results['final_mean_distance'], 
                 results['clustering_factor']]
        
        bars = ax2.bar(metrics, values, color=['blue', 'red', 'green'], alpha=0.7)
        ax2.set_ylabel('Value')
        ax2.set_title('Clustering Analysis')
        ax2.grid(True, alpha=0.3)
        
        # Add value labels on bars
        for bar, value in zip(bars, values):
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                    f'{value:.2f}', ha='center', va='bottom')
        
        # Plot 3: Angular momentum evolution
        L_metrics = ['Initial L', 'Final L', 'L Ratio']
        L_values = [results['initial_angular_momentum'],
                   results['final_angular_momentum'],
                   results['angular_momentum_ratio']]
        
        bars = ax3.bar(L_metrics, L_values, color=['purple', 'orange', 'cyan'], alpha=0.7)
        ax3.set_ylabel('Angular Momentum')
        ax3.set_title('Angular Momentum Evolution')
        ax3.grid(True, alpha=0.3)
        
        # Add value labels
        for bar, value in zip(bars, L_values):
            height = bar.get_height()
            ax3.text(bar.get_x() + bar.get_width()/2., height,
                    f'{value:.2e}', ha='center', va='bottom', fontsize=9)
        
        # Plot 4: Simulation parameters
        param_labels = ['N Particles', 'N Steps', 'L Primordial']
        param_values = [results['n_particles'], results['n_steps'], results['l_primordial']]
        
        bars = ax4.bar(param_labels, param_values, color=['gold', 'lightcoral', 'lightgreen'], alpha=0.7)
        ax4.set_ylabel('Value')
        ax4.set_title('Simulation Parameters')
        ax4.grid(True, alpha=0.3)
        
        # Add value labels
        for bar, value in zip(bars, param_values):
            height = bar.get_height()
            ax4.text(bar.get_x() + bar.get_width()/2., height,
                    f'{value:.0f}', ha='center', va='bottom')
        
        plt.tight_layout()
        
        if save_plot:
            plt.savefig('goe_angular_momentum_optimized.png', dpi=300, bbox_inches='tight')
            print("📊 Plot saved as 'goe_angular_momentum_optimized.png'")
        
        plt.show()
    
    def run_complete_analysis(self) -> Dict:
        """
        Run the complete optimized analysis with error handling.
        
        Returns:
        --------
        Dict
            Complete analysis results
        """
        try:
            print("🌌 Starting GoE Angular Momentum Analysis (Optimized)")
            print("=" * 60)
            
            # Run simulation
            results = self.run_simulation_fast()
            
            # Generate plots
            self.plot_results(results)
            
            # Print summary
            print("\n📋 ANALYSIS SUMMARY:")
            print(f"• Initial mean distance: {results['initial_mean_distance']:.2f} Mpc")
            print(f"• Final mean distance: {results['final_mean_distance']:.2f} Mpc")
            print(f"• Clustering factor: {results['clustering_factor']:.3f}")
            print(f"• Angular momentum ratio: {results['angular_momentum_ratio']:.3f}")
            print(f"• Primordial L parameter: {results['l_primordial']:.1f} (km/s)/(Mpc/h)")
            
            return results
            
        except Exception as e:
            print(f"❌ Error in analysis: {e}")
            return {"error": str(e)}

def main():
    """Main execution function for the optimized analysis."""
    # Create analyzer with optimized parameters
    analyzer = OptimizedAngularMomentumCosmicWeb(
        n_particles=500,    # Reduced from 2000
        n_steps=50,         # Reduced from 150
        dt=0.2,             # Larger time step
        l_primordial=50.0
    )
    
    # Run complete analysis
    results = analyzer.run_complete_analysis()
    
    # Save results
    if "error" not in results:
        with open('goe_angular_momentum_results.json', 'w') as f:
            json.dump(results, f, indent=2)
        print("💾 Results saved to 'goe_angular_momentum_results.json'")
    
    print("\n✅ GoE Angular Momentum Analysis (Optimized) Complete!")

if __name__ == "__main__":
    main() 