# HPC Thermal Stability Benchmark
## Marangoni Self-Pumping Cooling Validation Suite

**Version:** 9.0 (Public Data Room)  
**Last Updated:** 2026-02-09

---

## Overview

This repository contains benchmark code and validation data for Marangoni 
self-pumping thermal cooling technology. The physics exploit surface-tension-driven
flow to achieve pump-free cooling at high heat fluxes.

**Key Metrics (Simulation-Verified):**
- Max stable flux: 234 W/cm²
- CHF enhancement vs pool boiling: 7.4x
- CHF enhancement vs Novec 7100: 11.0x
- Zero-gravity performance: 100% (gravity-independent)

---

## Quick Start

```bash
# Clone and run verification
git clone https://github.com/nharris/HPC-Thermal-Stability-Benchmark.git
cd HPC-Thermal-Stability-Benchmark/physics

# Run Marangoni velocity calculation
python3 marangoni_velocity.py

# Run analytical checks
python3 analytical_checks.py
```

---

## Physics Background

### Marangoni Effect
The Marangoni effect is surface-tension-driven flow caused by gradients in 
surface tension along a fluid interface. In thermal Marangoni convection:

1. Hot surface creates temperature gradient in fluid
2. Temperature gradient creates surface tension gradient (dσ/dT)
3. Surface tension gradient drives fluid from hot → cold regions
4. Continuous circulation without mechanical pump

### Key Dimensionless Numbers

| Number | Definition | Significance |
|--------|------------|--------------|
| Marangoni (Ma) | (dσ/dT)·ΔT·L / (μα) | Surface tension vs diffusion |
| Bond (Bo) | ρgL²/σ | Gravity vs surface tension |
| Grashof (Gr) | gβΔTL³/ν² | Buoyancy strength |

For this system:
- Ma >> 10⁶ (surface tension dominates)
- Bo < 1 (surface tension > gravity for thin films)
- Ri = Gr/Ma² << 1 (Marangoni dominates buoyancy)

---

## Verification Scripts

### 1. Marangoni Velocity (`physics/marangoni_velocity.py`)
Calculates expected Marangoni-driven velocity from first principles:
```
τ = (dσ/dT) × (dT/dx)
u = H × τ / (2μ)
```

### 2. Analytical Checks (`physics/analytical_checks.py`)
- Zuber CHF correlation
- Rohsenow boiling correlation
- Thermal stress estimation

### 3. Benchmark Cases (`benchmarks/`)
- NVIDIA B200 GPU (133 W/cm² hotspot)
- Fusion divertor (10 MW/m²)
- Zero-gravity sweep

---

## Fluid Properties

**Binary Mixture: HFO-1336mzz-Z + Fluorinated Amine**

| Property | Value | Source |
|----------|-------|--------|
| Surface tension | 17.5-17.8 mN/m | GROMACS MD |
| dσ/dT | 0.00012 N/m·K | MD-derived |
| Boiling point | 33°C | Literature |
| Latent heat | 195 kJ/kg | Literature |

---

## Benchmark Results

### NVIDIA B200 GPU Cooling
- Heat flux: 133 W/cm² (hotspot)
- Result: 68.9°C junction temperature
- Status: STABLE (below 85°C throttle)

### CHF Analysis
- Maximum stable flux: 234 W/cm²
- Zuber pool boiling CHF: 32 W/cm²
- Enhancement ratio: 7.4x

### Zero-G Performance
- Velocity ratio (0g/1g): 1.00
- Conclusion: Fully gravity-independent

---

## Directory Structure

```
HPC-Thermal-Stability-Benchmark/
├── README.md
├── physics/
│   ├── marangoni_velocity.py
│   ├── analytical_checks.py
│   └── thermal_solver.py
├── benchmarks/
│   ├── nvidia_b200.json
│   ├── fusion_divertor.json
│   └── zero_g.json
├── data/
│   └── fluid_properties.json
└── assets/
    └── [figures]
```

---

## Citation

If you use this benchmark, please cite:
```
Genesis Thermal Core: Marangoni Self-Pumping Cooling
Provisional Patent Application, 2026
```

---

## License

Academic/research use permitted. Commercial licensing contact required.

---

## Contact

For data room access or commercial inquiries:
- Repository: github.com/nharris/HPC-Thermal-Stability-Benchmark
- Private data room: Available upon NDA
