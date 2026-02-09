# CHANGELOG — HPC Thermal Stability Benchmark

All notable changes to this public repository will be documented in this file.

## [5.0.0] - 2026-02-09

### Major Updates

#### Physics Corrections (S-TIER Verification)
- **Fixed dimensional error** in thermal solver: conduction term corrected from `K*d²T` to `K*t*d²T`
- **Updated SIGMA_GRAD** from 0.0002 to 0.00012 N/m·K (GROMACS-verified)
- **Corrected chemical identity**: TF-Ethylamine (CAS 753-90-2), not TFE alcohol (CAS 75-89-8)
- All 31 validation tests now passing

#### New Assets
- Added `assets/FIG_1_marangoni_mechanism.png` — Patent figure showing self-pumping mechanism
- Added `assets/FIG_2_marangoni_mechanism.png` — Detailed flow field visualization
- Added `assets/delta_sigma_comparison.png` — Δσ comparison across fluid generations
- Added `assets/performance_roadmap.png` — CHF capability by fluid generation
- Added `assets/discovery_funnel.png` — Computational discovery engine visualization
- Added `assets/surface_tension_final5.png` — Elite 10 candidates surface tension

#### Documentation
- Expanded README from 150 lines to 900+ lines (full whitepaper format)
- Added complete Table of Contents with 13 sections
- Added Nomenclature section with all symbols
- Added comprehensive References section (19 citations)
- Added 3 Appendices (Fluid Database, Marangoni Derivation, Chip Configs)

### Verified Performance Metrics
- CHF Enhancement: 11.0× vs Novec 7100
- Max T at 133 W/cm² (B200): 65.5°C
- Marangoni Velocity: 0.24 m/s (B200 flux)
- Surface Tension Gradient: 0.00012 N/m·K

## [4.0.0] - 2026-01-31

### Added
- Initial public release of benchmark tool
- `verify_dryout.py` — Core thermal solver
- `verify_roadmap.py` — Chip audit tool
- `physics/` module with boiling curves and Marangoni velocity
- 5 chip configuration files (H100, B200, GB200, Rubin, Colossus)

### Known Issues
- SIGMA_GRAD used incorrect value (0.0002 vs correct 0.00012)
- Chemical confusion between TFE alcohol and TF-Ethylamine
- These issues are fixed in v5.0.0

## [3.0.0] - 2026-01-29

### Added
- Initial internal release
- Basic Zuber CHF calculations
- Preliminary fluid database

---

**Note:** This repository is the public-facing companion to the private Patent 3 data room. It contains reproducible verification scripts but does not include proprietary fluid compositions or manufacturing specifications. Contact genesis-thermal-ip@proton.me for Data Room access.
