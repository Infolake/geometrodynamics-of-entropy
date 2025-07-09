"""
Geometrodynamics of Entropy (GoE) - Core Library
==============================================

This package implements the theoretical framework for the Geometrodynamics of Entropy
theory, focusing on the 6-dimensional Camargo metric and its implications for cosmology.

Modules:
    metric: Implementation of the Camargo metric (EGE-1)
    fibres: Quantization routines for fibre bundles Θ/Ξ
    bounce: Friedmann-Cartan integrator (EGE-7)

Author: Dr. Guilherme de Camargo
Version: 5.0 (Core Release)
Date: July 2025
"""

__version__ = "5.0.0"
__author__ = "Dr. Guilherme de Camargo"

# Import core modules
from .metric import CamargoMetric, MetricTensor
from .fibres import FibreQuantization, TorsionField
from .bounce import FriedmannCartan, CosmologicalBounce

__all__ = [
    'CamargoMetric',
    'MetricTensor', 
    'FibreQuantization',
    'TorsionField',
    'FriedmannCartan',
    'CosmologicalBounce'
]
