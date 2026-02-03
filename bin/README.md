# Genesis Thermal Check Binary

## `genesis_thermal_check`

This directory contains the **proprietary verification binary** for the Genesis Marangoni Fluid.

### What It Does

The `genesis_thermal_check` binary:
1. Takes your thermal load as input (W/cm²)
2. Runs the proprietary Marangoni stability calculation
3. Returns PASS/FAIL with predicted surface temperature

### Usage

```bash
# Check if B200 (400 W/cm² hotspot) would be stable
./genesis_thermal_check --flux 400

# Output:
# ✅ STATUS: STABLE
# Max Temperature: 36.8°C
# CHF Margin: 75.8%
# Self-Pump Velocity: 0.12 m/s
```

### Access

This binary is **not included in the public repository**.

To request access:
1. Email: genesis-thermal-ip@proton.me
2. Subject: "Genesis Thermal Check Binary Access"
3. Include: Organization, Use Case, Target Power Density

### Source Reference

The physics implemented in this binary is derived from:
- **Patent:** Genesis Patent 3 (Thermal Core)
- **Claims:** 63/751,001 through 63/751,005
- **Data:** `PROVISIONAL_3_THERMAL_CORE/02_EVIDENCE_LOCKER/A_NVIDIA_KILL_SHOT/`

### Verified Performance

| Parameter | Value | Source |
|:----------|:------|:-------|
| CHF Enhancement | 5.5× | CFD Simulation (OpenFOAM) |
| Max CHF | 1650 W/cm² | Zuber + Marangoni Correction |
| Δσ Gradient | 7.0 mN/m | Molecular Dynamics (GROMACS) |
| Self-Pump Velocity | 0.1-1.0 m/s | CFD Validated |
| Max Temp @ 1000 W/cm² | 36.8°C | Full-Chip Simulation |

---

*Binary not included. Contact for NDA and Data Room access.*
