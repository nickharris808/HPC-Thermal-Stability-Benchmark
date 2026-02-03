#!/bin/bash
# ============================================================================
# HPC THERMAL STABILITY BENCHMARK - QUICK START DEMO
# ============================================================================
#
# This script runs a complete demonstration of the benchmark tool.
#
# Usage:
#   chmod +x run_demo.sh
#   ./run_demo.sh
#
# ============================================================================

set -e

echo "============================================================================"
echo "🔬 HPC THERMAL STABILITY BENCHMARK - DEMO"
echo "============================================================================"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.8+."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -q numpy matplotlib scipy 2>/dev/null || pip install -q numpy matplotlib scipy
echo "✅ Dependencies installed"
echo ""

# Generate figures
echo "📊 Generating visualizations..."
python3 generate_figures.py
echo ""

# Run benchmark on all chips
echo "🔎 Running thermal stability audit..."
python3 verify_roadmap.py --all
echo ""

# Summary
echo "============================================================================"
echo "✅ DEMO COMPLETE"
echo "============================================================================"
echo ""
echo "📁 Generated Files:"
echo "   - figures/thermal_cliff_comparison.png"
echo "   - figures/boiling_curve_comparison.png"
echo "   - figures/roadmap_projection.png"
echo "   - results/audit_results.json"
echo ""
echo "📖 Next Steps:"
echo "   1. Open README.md for full technical documentation"
echo "   2. Add your own chip configs to configs/"
echo "   3. Run: python verify_roadmap.py --config your_chip"
echo ""
echo "🔒 For access to the Genesis Marangoni solution:"
echo "   📧 Contact: genesis-thermal-ip@proton.me"
echo "============================================================================"
