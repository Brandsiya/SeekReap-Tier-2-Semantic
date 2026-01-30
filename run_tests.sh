#!/bin/bash
# Tier-2 Test Runner
# Runs all tests with architectural verification

set -e

echo "=== TIER-2 TEST RUNNER ==="
echo "Timestamp: $(date)"
echo ""

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    if [ "$1" = "success" ]; then
        echo -e "${GREEN}✅ $2${NC}"
    elif [ "$1" = "warning" ]; then
        echo -e "${YELLOW}⚠️  $2${NC}"
    elif [ "$1" = "error" ]; then
        echo -e "${RED}❌ $2${NC}"
    else
        echo "$2"
    fi
}

# Step 1: Verify folder structure
echo "1. Verifying folder structure..."
if [ -d "tier2_core" ] && [ -d "tier2_tests" ] && [ -d "docs" ]; then
    print_status "success" "Folder structure OK"
else
    print_status "error" "Folder structure verification failed"
    exit 1
fi

# Step 2: Check for Tier-1 contamination
echo "2. Checking for Tier-1 contamination..."
if [ ! -d "tier1" ] && [ ! -d "tier1_core" ]; then
    print_status "success" "No Tier-1 contamination detected"
else
    print_status "error" "Tier-1 directories found (violation)"
    exit 1
fi

# Step 3: Run unit tests
echo "3. Running unit tests..."
python -m pytest tier2_tests/unit/ -v --tb=short
if [ $? -eq 0 ]; then
    print_status "success" "Unit tests passed"
else
    print_status "error" "Unit tests failed"
    exit 1
fi

# Step 4: Run boundary tests
echo "4. Running boundary tests..."
python -m pytest tier2_tests/boundary/ -v --tb=short
if [ $? -eq 0 ]; then
    print_status "success" "Boundary tests passed"
else
    print_status "error" "Boundary tests failed"
    exit 1
fi

# Step 5: Run integration tests
echo "5. Running integration tests..."
python -m pytest tier2_tests/integration/ -v --tb=short
if [ $? -eq 0 ]; then
    print_status "success" "Integration tests passed"
else
    print_status "error" "Integration tests failed"
    exit 1
fi

# Step 6: Check test coverage
echo "6. Checking test coverage..."
python -m pytest tier2_tests/ \
    --cov=tier2_core \
    --cov-report=term-missing \
    --cov-fail-under=80

if [ $? -eq 0 ]; then
    print_status "success" "Test coverage ≥80%"
else
    print_status "error" "Test coverage below 80%"
    exit 1
fi

# Step 7: Final verification
echo ""
echo "=== FINAL VERIFICATION ==="
echo "Total Python files: $(find . -name "*.py" -type f | grep -v "__pycache__" | wc -l)"
echo "Files with TIER-2 annotations: $(grep -l "TIER-2" $(find . -name "*.py" -type f) | wc -l)"
echo "Test files: $(find tier2_tests -name "test_*.py" -type f | wc -l)"
echo ""
print_status "success" "All Tier-2 architectural tests passed"
print_status "success" "Ready for production deployment"
