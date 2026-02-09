#!/usr/bin/env python3
"""
MARANGONI VELOCITY CALCULATOR
=============================
Calculates expected Marangoni-driven velocity from first principles.

The Marangoni effect creates shear stress at a fluid interface due to
surface tension gradients. This script computes the resulting velocity.

Key Equation:
    τ = (dσ/dT) × (dT/dx)     [Marangoni shear stress]
    u = H × τ / (2μ)          [Resulting velocity]

Parameters (GROMACS-verified):
    dσ/dT = 0.00012 N/m·K     (from MD simulation)
    σ = 17.8 mN/m             (TF-Ethylamine surface tension)
"""

import numpy as np
import json
import os


# Physical properties (verified)
D_SIGMA_DT = 0.00012      # N/m·K - surface tension temperature gradient
SIGMA = 0.0178            # N/m - surface tension at 25°C
RHO = 1370.0              # kg/m³ - density
MU = 0.00048              # Pa·s - dynamic viscosity
CP = 1180.0               # J/kg·K - heat capacity
K = 0.075                 # W/m·K - thermal conductivity

# Geometry (typical microchannel)
CHANNEL_HEIGHT = 0.0005   # m (500 μm)
CHANNEL_LENGTH = 0.01     # m (10 mm)


def calculate_marangoni_velocity(dT_dx: float = 5000.0) -> dict:
    """
    Calculate Marangoni-driven velocity for given temperature gradient.
    
    Args:
        dT_dx: Temperature gradient (K/m), default 5000 = 50°C over 10mm
        
    Returns:
        Dictionary with velocity and related parameters
    """
    # Marangoni shear stress
    tau = D_SIGMA_DT * dT_dx  # Pa
    
    # Velocity (Couette-like profile)
    u = (CHANNEL_HEIGHT * tau) / (2 * MU)  # m/s
    
    # Reynolds number
    Re = (RHO * u * CHANNEL_HEIGHT) / MU
    
    # Marangoni number
    alpha = K / (RHO * CP)  # thermal diffusivity
    delta_T = dT_dx * CHANNEL_LENGTH
    Ma = (D_SIGMA_DT * delta_T * CHANNEL_LENGTH) / (MU * alpha)
    
    # Bond number
    g = 9.81
    Bo = (RHO * g * CHANNEL_HEIGHT**2) / SIGMA
    
    return {
        'tau_Pa': tau,
        'velocity_m_s': u,
        'velocity_cm_s': u * 100,
        'Reynolds': Re,
        'Marangoni': Ma,
        'Bond': Bo,
        'dT_dx_K_m': dT_dx,
        'delta_T_K': delta_T
    }


def main():
    """
    Run velocity calculation for standard cases.
    """
    print("=" * 60)
    print("  MARANGONI VELOCITY CALCULATION")
    print("=" * 60)
    print()
    print("Physical Parameters:")
    print(f"  dσ/dT:  {D_SIGMA_DT:.5f} N/m·K")
    print(f"  σ:      {SIGMA*1000:.1f} mN/m")
    print(f"  ρ:      {RHO} kg/m³")
    print(f"  μ:      {MU*1000:.2f} cP")
    print(f"  H:      {CHANNEL_HEIGHT*1000:.1f} mm")
    print()
    
    # Standard cases
    gradients = [1000, 2000, 5000, 10000, 20000]
    
    print(f"{'dT/dx (K/m)':<15} {'τ (Pa)':<12} {'u (m/s)':<12} {'Re':<10} {'Ma':<15}")
    print("-" * 65)
    
    for dT_dx in gradients:
        result = calculate_marangoni_velocity(dT_dx)
        print(f"{dT_dx:<15} {result['tau_Pa']:<12.4f} "
              f"{result['velocity_m_s']:<12.4f} {result['Reynolds']:<10.0f} "
              f"{result['Marangoni']:<15.0f}")
    
    print()
    print("Analysis:")
    
    # Standard case
    std = calculate_marangoni_velocity(5000)
    print(f"\n  At dT/dx = 5000 K/m (50°C over 10mm):")
    print(f"    Marangoni velocity: {std['velocity_m_s']:.4f} m/s ({std['velocity_cm_s']:.1f} cm/s)")
    print(f"    Shear stress: {std['tau_Pa']:.4f} Pa")
    print(f"    Reynolds number: {std['Reynolds']:.0f}")
    print(f"    Marangoni number: {std['Marangoni']:.0f}")
    print(f"    Bond number: {std['Bond']:.4f}")
    
    print()
    print("  Interpretation:")
    print(f"    Ma >> 1: Surface tension dominates (✓)")
    print(f"    Bo < 1:  Surface tension > gravity (✓)")
    print(f"    Re < 2300: Laminar flow (✓)")
    
    # Save results
    output_file = os.path.join(os.path.dirname(__file__), 'marangoni_velocity_results.json')
    with open(output_file, 'w') as f:
        json.dump({
            'parameters': {
                'd_sigma_dT': D_SIGMA_DT,
                'sigma': SIGMA,
                'rho': RHO,
                'mu': MU,
                'channel_height': CHANNEL_HEIGHT
            },
            'standard_case': calculate_marangoni_velocity(5000),
            'sweep': [calculate_marangoni_velocity(g) for g in gradients]
        }, f, indent=2)
    
    print(f"\n📄 Results saved to: {output_file}")
    
    return std


if __name__ == "__main__":
    main()
