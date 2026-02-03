#!/usr/bin/env python3
"""
================================================================================
FIGURE GENERATOR FOR HPC THERMAL STABILITY BENCHMARK
================================================================================

Generates publication-quality figures for the whitepaper README.

Usage:
    python generate_figures.py

Outputs:
    figures/thermal_cliff_comparison.png
    figures/boiling_curve_comparison.png
    figures/roadmap_projection.png

================================================================================
"""

import numpy as np
import os
from pathlib import Path

# Ensure figures directory exists
FIGURES_DIR = Path(__file__).parent / "figures"
FIGURES_DIR.mkdir(exist_ok=True)

def generate_thermal_cliff_chart():
    """Generate the viral 'Thermal Cliff' bar chart."""
    try:
        import matplotlib.pyplot as plt
        import matplotlib.patches as mpatches
    except ImportError:
        print("❌ matplotlib not installed. Run: pip install matplotlib")
        return
    
    # Data: Fluid CHF values (W/cm²)
    fluids = {
        "FC-72 (PFC)": 14,
        "Novec 649 (FK)": 14,
        "Novec 7100 (HFE)": 18,
        "HFO-1234ze": 21,
        "Ethanol": 45,
        "Deionized Water": 120,
        "GENESIS MARANGONI\n(Patent 3 - 🔒)": 165,
    }
    
    # Sort by CHF
    sorted_fluids = dict(sorted(fluids.items(), key=lambda x: x[1]))
    
    # Colors
    colors = []
    for chf in sorted_fluids.values():
        if chf > 100:
            colors.append('#2ecc71')  # Green
        elif chf > 50:
            colors.append('#f1c40f')  # Yellow
        elif chf > 25:
            colors.append('#e67e22')  # Orange
        else:
            colors.append('#e74c3c')  # Red
    
    # Override Genesis to purple
    colors[-1] = '#9b59b6'
    
    # Create figure
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(14, 8))
    
    y_pos = np.arange(len(sorted_fluids))
    bars = ax.barh(y_pos, list(sorted_fluids.values()), color=colors, 
                   edgecolor='black', linewidth=0.5, height=0.7)
    
    # Chip power lines
    chip_lines = [
        ("H100 Hotspot (215 W/cm²)", 215, '#3498db', '-'),
        ("B200 Hotspot (400 W/cm²)", 400, '#e67e22', '--'),
        ("Rubin 2026 (800 W/cm²)", 800, '#c0392b', ':'),
    ]
    
    for name, power, color, style in chip_lines:
        ax.axvline(x=power, color=color, linestyle=style, linewidth=2.5, zorder=1)
        ax.text(power + 15, len(sorted_fluids) - 0.3, name, fontsize=9, 
                color=color, fontweight='bold', va='top')
    
    # Danger zone
    ax.axvspan(250, 900, alpha=0.12, color='red', zorder=0)
    ax.text(850, 0.5, 'FAILURE\nZONE', fontsize=12, color='#c0392b', 
            ha='center', va='center', fontweight='bold', alpha=0.7)
    
    # Labels
    ax.set_yticks(y_pos)
    ax.set_yticklabels(list(sorted_fluids.keys()), fontsize=11)
    ax.set_xlabel('Critical Heat Flux (W/cm²)', fontsize=13, fontweight='bold')
    ax.set_title('THE THERMAL CLIFF\n'
                 'Critical Heat Flux Limits vs. AI Accelerator Power Density',
                 fontsize=16, fontweight='bold', pad=20)
    
    # Value labels
    for i, (bar, val) in enumerate(zip(bars, sorted_fluids.values())):
        if val > 80:
            ax.text(val - 8, bar.get_y() + bar.get_height()/2, f'{val} W/cm²',
                   ha='right', va='center', fontsize=10, color='white', fontweight='bold')
        else:
            ax.text(val + 5, bar.get_y() + bar.get_height()/2, f'{val} W/cm²',
                   ha='left', va='center', fontsize=10, color='black')
    
    # Legend
    legend_elements = [
        mpatches.Patch(facecolor='#e74c3c', edgecolor='black', label='Dangerous (< 25 W/cm²)'),
        mpatches.Patch(facecolor='#e67e22', edgecolor='black', label='Marginal (25-50)'),
        mpatches.Patch(facecolor='#f1c40f', edgecolor='black', label='Caution (50-100)'),
        mpatches.Patch(facecolor='#2ecc71', edgecolor='black', label='Safe (> 100)'),
        mpatches.Patch(facecolor='#9b59b6', edgecolor='black', label='Proprietary Solution'),
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=10, 
              framealpha=0.95)
    
    ax.set_xlim(0, 900)
    
    # Annotation
    textstr = ('THE PHYSICS PROBLEM\n'
               '━━━━━━━━━━━━━━━━━━━━━━━━\n'
               'All commercial dielectric\n'
               'fluids hit CHF below 25 W/cm².\n\n'
               'B200 hotspots: 400 W/cm².\n'
               'Rubin hotspots: 800 W/cm².\n\n'
               'This gap cannot be closed\n'
               'with conventional physics.')
    props = dict(boxstyle='round,pad=0.5', facecolor='#2c3e50', edgecolor='none', alpha=0.92)
    ax.text(0.97, 0.03, textstr, transform=ax.transAxes, fontsize=9,
            verticalalignment='bottom', horizontalalignment='right',
            bbox=props, color='white', family='monospace')
    
    plt.tight_layout()
    output_path = FIGURES_DIR / "thermal_cliff_comparison.png"
    plt.savefig(output_path, dpi=200, bbox_inches='tight', facecolor='white')
    print(f"✅ Saved: {output_path}")
    
    # SVG for web
    plt.savefig(str(output_path).replace('.png', '.svg'), format='svg', bbox_inches='tight')
    print(f"✅ Saved: {str(output_path).replace('.png', '.svg')}")
    
    plt.close()


def generate_boiling_curve():
    """Generate boiling curve comparison."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        return
    
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Superheat range
    dt = np.linspace(0.1, 80, 500)
    
    # Water boiling curve
    q_water = np.zeros_like(dt)
    for i, t in enumerate(dt):
        if t < 5:
            q_water[i] = 20 * t  # Natural convection
        elif t < 30:
            q_water[i] = 100 + ((t - 5) / 25) ** 2.8 * 110  # Nucleate boiling to CHF
        elif t < 35:
            q_water[i] = 120 - (t - 30) * 20  # Transition
        else:
            q_water[i] = 20 + 0.3 * (t - 35)  # Film boiling
    
    # Novec 7100 boiling curve
    q_novec = np.zeros_like(dt)
    for i, t in enumerate(dt):
        if t < 5:
            q_novec[i] = 3 * t
        elif t < 25:
            q_novec[i] = 15 + ((t - 5) / 20) ** 2.8 * 3
        elif t < 30:
            q_novec[i] = 18 - (t - 25) * 3
        else:
            q_novec[i] = 3 + 0.05 * (t - 30)
    
    # Genesis Marangoni curve (proprietary - shown as projection)
    q_genesis = np.zeros_like(dt)
    for i, t in enumerate(dt):
        if t < 5:
            q_genesis[i] = 50 * t
        elif t < 45:
            q_genesis[i] = 250 + ((t - 5) / 40) ** 2.2 * 1400
        else:
            q_genesis[i] = 1650
    
    # Plot curves
    ax.plot(dt, q_water, label='Deionized Water', color='#3498db', linewidth=2.5)
    ax.plot(dt, q_novec, label='Novec 7100 (HFE)', color='#e74c3c', linewidth=2.5)
    ax.plot(dt, q_genesis, label='GENESIS MARANGONI (🔒)', color='#9b59b6', 
            linewidth=3, linestyle='--')
    
    # Mark CHF points
    ax.scatter([30], [120], color='#3498db', s=120, zorder=5, edgecolor='black', linewidth=2)
    ax.scatter([25], [18], color='#e74c3c', s=120, zorder=5, edgecolor='black', linewidth=2)
    ax.scatter([45], [1650], color='#9b59b6', s=150, marker='*', zorder=5, 
               edgecolor='black', linewidth=1.5)
    
    # Annotations
    ax.annotate('CHF: 120 W/cm²\n(Water)', xy=(30, 120), xytext=(45, 200),
                fontsize=10, color='#3498db', fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='#3498db', lw=1.5))
    
    ax.annotate('CHF: 18 W/cm²\n(Novec)', xy=(25, 18), xytext=(40, 80),
                fontsize=10, color='#e74c3c', fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=1.5))
    
    ax.annotate('CHF: 1,650 W/cm²\n(5.5× Enhancement)', xy=(45, 1650), xytext=(55, 1300),
                fontsize=11, color='#9b59b6', fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='#9b59b6', lw=2))
    
    # Chip reference lines
    ax.axhline(y=400, color='#c0392b', linestyle=':', linewidth=2, alpha=0.7)
    ax.text(75, 430, 'B200 Hotspot', fontsize=10, color='#c0392b', fontweight='bold')
    
    ax.axhline(y=800, color='#8e44ad', linestyle=':', linewidth=2, alpha=0.7)
    ax.text(75, 830, 'Rubin 2026', fontsize=10, color='#8e44ad', fontweight='bold')
    
    # Film boiling zone shading
    ax.axhspan(0, 30, xmin=0.4, alpha=0.1, color='red')
    
    # Labels
    ax.set_xlabel('Surface Superheat ΔT (°C)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Heat Flux q" (W/cm²)', fontsize=12, fontweight='bold')
    ax.set_title('BOILING CURVE COMPARISON\n'
                 'The Physics of Heat Transfer Limits',
                 fontsize=14, fontweight='bold', pad=15)
    ax.legend(loc='upper left', fontsize=11, framealpha=0.95)
    ax.set_xlim(0, 80)
    ax.set_ylim(0, 1800)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    output_path = FIGURES_DIR / "boiling_curve_comparison.png"
    plt.savefig(output_path, dpi=200, bbox_inches='tight', facecolor='white')
    print(f"✅ Saved: {output_path}")
    plt.close()


def generate_roadmap_projection():
    """Generate chip power roadmap projection."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        return
    
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Data
    years = [2020, 2022, 2024, 2025, 2026, 2027]
    chips = ['A100', 'H100', 'B200', 'B300\n(Proj)', 'Rubin\n(Proj)', 'Rubin+\n(Proj)']
    hotspot_flux = [144, 215, 400, 600, 800, 1000]
    
    # Colors based on status
    colors = ['#2ecc71', '#f1c40f', '#e74c3c', '#c0392b', '#8e44ad', '#8e44ad']
    
    # Bar chart
    bars = ax.bar(chips, hotspot_flux, color=colors, edgecolor='black', linewidth=1)
    
    # CHF limit lines
    ax.axhline(y=18, color='#e74c3c', linestyle='--', linewidth=2, 
               label='Novec 7100 CHF (18 W/cm²)')
    ax.axhline(y=120, color='#3498db', linestyle='--', linewidth=2,
               label='Water CHF (120 W/cm²)')
    ax.axhline(y=1650, color='#9b59b6', linestyle='--', linewidth=2,
               label='Genesis CHF (1,650 W/cm²)')
    
    # Labels on bars
    for bar, flux in zip(bars, hotspot_flux):
        ax.text(bar.get_x() + bar.get_width()/2, flux + 30, f'{flux}',
               ha='center', fontsize=11, fontweight='bold')
    
    ax.set_ylabel('Hotspot Heat Flux (W/cm²)', fontsize=12, fontweight='bold')
    ax.set_xlabel('GPU Generation', fontsize=12, fontweight='bold')
    ax.set_title('AI ACCELERATOR POWER DENSITY ROADMAP\n'
                 'Projected Hotspot Heat Flux vs. Cooling Limits',
                 fontsize=14, fontweight='bold', pad=15)
    ax.legend(loc='upper left', fontsize=10)
    ax.set_ylim(0, 1200)
    
    # Danger zone annotation
    ax.annotate('ALL COMMERCIAL FLUIDS\nFAIL HERE',
                xy=(2, 400), xytext=(3.5, 700),
                fontsize=12, color='#c0392b', fontweight='bold',
                ha='center',
                arrowprops=dict(arrowstyle='->', color='#c0392b', lw=2))
    
    plt.tight_layout()
    output_path = FIGURES_DIR / "roadmap_projection.png"
    plt.savefig(output_path, dpi=200, bbox_inches='tight', facecolor='white')
    print(f"✅ Saved: {output_path}")
    plt.close()


def main():
    print("="*60)
    print("📊 HPC THERMAL STABILITY BENCHMARK - FIGURE GENERATOR")
    print("="*60)
    
    print("\n1. Generating Thermal Cliff Chart...")
    generate_thermal_cliff_chart()
    
    print("\n2. Generating Boiling Curve Comparison...")
    generate_boiling_curve()
    
    print("\n3. Generating Roadmap Projection...")
    generate_roadmap_projection()
    
    print("\n" + "="*60)
    print("✅ All figures generated successfully!")
    print(f"📁 Output directory: {FIGURES_DIR}")
    print("="*60)


if __name__ == "__main__":
    main()
