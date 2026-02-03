# Contributing to HPC Thermal Stability Benchmark

## Welcome

This benchmark tool is designed to be an **objective physics resource** for the HPC cooling industry. We welcome contributions that improve accuracy, add fluid data, or extend chip configurations.

## What We Accept

### ✅ Encouraged Contributions

1. **New Fluid Data**
   - Add thermophysical properties for cooling fluids not in our database
   - Must include peer-reviewed source citations
   - Format: JSON entry in `physics/standard_fluids_db.json`

2. **New Chip Configurations**
   - Add configurations for announced or projected AI accelerators
   - Must cite official specifications or credible leaks
   - Format: JSON file in `configs/`

3. **Correlation Improvements**
   - Enhanced CHF correlations (e.g., subcooling effects, pressure corrections)
   - Must cite the original paper
   - Add to `physics/boiling_curves.py` with docstrings

4. **Visualization Enhancements**
   - Better figure styling
   - Additional analysis plots
   - Interactive dashboards (Plotly, Streamlit)

5. **Documentation**
   - Typo fixes
   - Clarifications
   - Additional references

### ❌ Out of Scope

- Proprietary fluid data (covered under NDAs)
- Marketing content
- Unverified performance claims
- Closed-source dependencies

## How to Contribute

1. **Fork** the repository
2. **Create a branch** (`git checkout -b feature/new-fluid-data`)
3. **Make changes** with clear commit messages
4. **Add tests** if applicable
5. **Submit a Pull Request** with:
   - Description of changes
   - Source citations
   - Test results

## Code Style

- Python 3.8+
- PEP 8 formatting
- Docstrings for all functions
- Type hints encouraged

## Physics Standards

All CHF calculations must:
- Cite the original correlation paper
- State assumptions (pressure, orientation, subcooling)
- Include units in variable names or comments
- Validate against published experimental data where available

## Questions?

Open an issue with the `[Question]` tag.

---

*This benchmark exists to advance the state of thermal management for AI infrastructure. We believe open physics benefits everyone.*
