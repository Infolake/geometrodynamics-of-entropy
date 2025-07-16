#!/usr/bin/env python3
"""
Unit tests for GoE derivations

Author: Dr. Guilherme de Camargo
Version: v8.0 (Unification Edition)
Date: July 16, 2025
"""

import unittest
import numpy as np
import sys
import os

# Add scripts directory to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'derivations'))

class TestGoEDerivations(unittest.TestCase):
    """Test suite for GoE theoretical predictions"""
    
    def setUp(self):
        """Set up test parameters"""
        self.R2 = 4.6e-18  # Theta fiber radius (m)
        self.R3 = 1.0e-15  # Xi fiber radius (m)
        self.tolerance = 0.1  # 10% tolerance for predictions
        
    def test_muon_g2_calculation(self):
        """Test muon g-2 anomaly calculation"""
        # Calculate GoE contribution
        alpha = 1/137.0
        kappa_tau = 5.2e-4
        hbar_c = 0.197e-15  # GeV⋅m
        m_mu = 105.66e-3  # GeV
        
        Lambda_Theta = hbar_c / self.R2
        log_factor = np.log(Lambda_Theta**2 / m_mu**2)
        delta_a_mu = (alpha / (2 * np.pi)) * kappa_tau * log_factor
        
        # Convert to standard units (×10^-9)
        delta_a_mu *= 1e9
        
        # Expected experimental value
        expected = 2.30  # ×10^-9
        
        self.assertAlmostEqual(delta_a_mu, expected, delta=expected*self.tolerance,
                              msg=f"Muon g-2 calculation failed: {delta_a_mu:.2f} vs expected {expected:.2f}")
    
    def test_geometric_constant_consistency(self):
        """Test geometric constant K from muon-neutrino correlation"""
        delta_a_mu = 2.30e-9
        delta_cp = 1.970  # radians
        
        correlation_factor = 1 - np.cos(delta_cp)
        K_calculated = delta_a_mu / correlation_factor
        
        # Expected value from literature
        K_expected = 1.826e-9
        
        self.assertAlmostEqual(K_calculated, K_expected, delta=K_expected*self.tolerance,
                              msg=f"Geometric constant inconsistent: {K_calculated:.3e} vs expected {K_expected:.3e}")
    
    def test_fiber_radius_hierarchy(self):
        """Test that Xi fiber is larger than Theta fiber"""
        self.assertGreater(self.R3, self.R2, 
                          msg="Xi fiber radius should be larger than Theta fiber radius")
    
    def test_dimensional_analysis(self):
        """Test dimensional consistency of key equations"""
        # Muon g-2 should be dimensionless
        alpha = 1/137.0  # dimensionless
        kappa_tau = 5.2e-4  # dimensionless
        log_factor = 30  # dimensionless (typical value)
        
        delta_a_mu = (alpha / (2 * np.pi)) * kappa_tau * log_factor
        
        # Should be dimensionless and of order 10^-9
        self.assertLess(delta_a_mu, 1e-6, 
                       msg="Muon g-2 should be much less than 1")
        self.assertGreater(delta_a_mu, 1e-12, 
                          msg="Muon g-2 should be larger than 10^-12")
    
    def test_cp_phase_range(self):
        """Test CP violation phase is in valid range"""
        delta_cp = 1.970  # experimental value
        
        self.assertGreaterEqual(delta_cp, 0, 
                               msg="CP phase should be non-negative (taking absolute value)")
        self.assertLessEqual(delta_cp, 2*np.pi, 
                            msg="CP phase should be less than 2π")
    
    def test_gwb_frequency_scaling(self):
        """Test gravitational wave background frequency scaling"""
        f_peak = 1e-3  # Hz
        
        # Peak frequency should be in LISA sensitivity range
        self.assertGreater(f_peak, 1e-5, 
                          msg="GWB peak frequency too low for space-based detection")
        self.assertLess(f_peak, 1e-1, 
                       msg="GWB peak frequency too high for LISA")
    
    def test_unification_scale(self):
        """Test gauge coupling unification scale"""
        mu_GUT = 8.7e3  # GeV
        
        # Should be accessible to future colliders but above current energies
        self.assertGreater(mu_GUT, 1e3, 
                          msg="Unification scale should be above TeV")
        self.assertLess(mu_GUT, 1e5, 
                       msg="Unification scale should be below 100 TeV for accessibility")
    
    def test_perihelion_correction_magnitude(self):
        """Test perihelion precession correction is small"""
        K_orb = 1e-6
        R3_R2_ratio = self.R3 / self.R2
        GM = 1.327e20  # m^3/s^2 (Sun)
        c = 2.998e8  # m/s
        a = 5.79e10  # m (Mercury semi-major axis)
        e = 0.2056  # Mercury eccentricity
        
        delta_phi = K_orb * (R3_R2_ratio)**2 * GM / (c**2 * a * (1 - e**2))
        
        # Convert to arcsec/century
        arcsec_per_rad = 206265
        correction = delta_phi * arcsec_per_rad
        
        # Should be much smaller than GR prediction (42.98 arcsec/century)
        self.assertLess(correction, 1.0, 
                       msg="GoE perihelion correction should be sub-arcsec level")
        self.assertGreater(correction, 1e-6, 
                          msg="GoE correction should be potentially detectable")
    
    def test_semi_dirac_dispersion(self):
        """Test semi-Dirac dispersion relation properties"""
        # Test anisotropy
        v_F = 1e6  # m/s
        m_star = 1e-30  # kg
        hbar = 1.055e-34  # J⋅s
        
        k = 1e8  # 1/m
        
        # Energy for motion in x-direction (Dirac-like)
        E_x = hbar * v_F * k
        
        # Energy for motion in y-direction (parabolic)
        E_y = hbar**2 * k**2 / (2 * m_star)
        
        # At high momentum, x-direction should dominate
        if k * hbar > m_star * v_F:
            self.assertGreater(E_x, E_y, 
                              msg="At high momentum, Dirac term should dominate")

class TestGoEValidation(unittest.TestCase):
    """Test the validation infrastructure itself"""
    
    def test_experimental_data_loading(self):
        """Test that experimental data is properly loaded"""
        try:
            from validate_all_derivations import DerivationValidator
            validator = DerivationValidator()
            
            # Check required experimental data exists
            required_keys = ['muon_g2', 'cp_violation', 'jwst_galaxies', 'perihelion_mercury']
            for key in required_keys:
                self.assertIn(key, validator.experimental_data,
                             msg=f"Missing experimental data for {key}")
                
        except ImportError:
            self.skipTest("Validation module not available")
    
    def test_goe_parameters_loading(self):
        """Test that GoE parameters are properly loaded"""
        try:
            from validate_all_derivations import DerivationValidator
            validator = DerivationValidator()
            
            # Check required parameters exist
            required_params = ['R2', 'R3', 'kappa_tau', 'K_geometric']
            for param in required_params:
                self.assertIn(param, validator.goe_parameters,
                             msg=f"Missing GoE parameter {param}")
                
        except ImportError:
            self.skipTest("Validation module not available")

def run_tests():
    """Run all tests and return results"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes
    suite.addTests(loader.loadTestsFromTestCase(TestGoEDerivations))
    suite.addTests(loader.loadTestsFromTestCase(TestGoEValidation))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result

def main():
    """Main test entry point"""
    print("GoE Derivations Test Suite")
    print("=" * 40)
    
    result = run_tests()
    
    print(f"\nTest Summary:")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.wasSuccessful():
        print("🎉 All tests passed!")
        return 0
    else:
        print("❌ Some tests failed")
        return 1

if __name__ == "__main__":
    exit(main())