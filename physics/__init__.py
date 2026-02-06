"""
================================================================================
PHYSICS MODULE: HPC Thermal Stability Benchmark
================================================================================

This module provides physics-accurate implementations of Critical Heat Flux (CHF)
correlations and boiling curve calculations.

Submodules:
-----------
- boiling_curves: Zuber, Kandlikar, Rohsenow correlations
- marangoni_velocity: Derivation and calculation of self-pumping flow

Source Traceability:
-------------------
These physics implementations are derived from and validated against:
- PROVISIONAL_3_THERMAL_CORE/02_CODEBASE/laser_sim_v2_physics.py
- PROVISIONAL_3_THERMAL_CORE/02_CODEBASE/mixture_thermophysics.py

Patent Reference:
----------------
Genesis Patent 3: Thermal Core
US Provisional Applications 63/751,001 through 63/751,005
Filed: January 2026

================================================================================
"""

from .boiling_curves import (
    FluidProperties,
    calculate_zuber_chf,
    calculate_kandlikar_chf,
    calculate_boiling_curve,
    calculate_safety_margin
)

__all__ = [
    'FluidProperties',
    'calculate_zuber_chf', 
    'calculate_kandlikar_chf',
    'calculate_boiling_curve',
    'calculate_safety_margin'
]
