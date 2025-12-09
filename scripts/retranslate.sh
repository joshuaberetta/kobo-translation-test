#!/bin/bash
# Bulk Retranslation Helper Script
# 
# Quick wrapper around bulk_retranslate.py for common use cases

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/.."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if Python script exists
if [ ! -f "scripts/bulk_retranslate.py" ]; then
    echo -e "${RED}❌ Error: bulk_retranslate.py not found${NC}"
    exit 1
fi

# Show usage if no arguments
if [ $# -eq 0 ]; then
    echo "Bulk Retranslation Helper"
    echo ""
    echo "Quick commands:"
    echo "  $0 test-es          - Test with 2 files → Spanish"
    echo "  $0 test-all         - Test with 2 files → all languages"
    echo "  $0 all-es           - Retranslate all docs → Spanish"
    echo "  $0 all-langs        - Retranslate all docs → all languages"
    echo "  $0 dry-run          - Preview what would be translated"
    echo ""
    echo "Custom:"
    echo "  $0 custom --language es --files file1.md file2.md"
    echo ""
    echo "For full options, run:"
    echo "  python scripts/bulk_retranslate.py --help"
    exit 0
fi

case "$1" in
    test-es)
        echo -e "${GREEN}Testing with 2 files → Spanish${NC}"
        python scripts/bulk_retranslate.py \
            --language es \
            --files test_simple.md test_complex.md \
            --verbose
        ;;
    
    test-all)
        echo -e "${GREEN}Testing with 2 files → all languages${NC}"
        python scripts/bulk_retranslate.py \
            --language es fr ar \
            --files test_simple.md test_complex.md \
            --verbose
        ;;
    
    all-es)
        echo -e "${YELLOW}⚠️  This will retranslate ALL docs to Spanish${NC}"
        echo -e "${YELLOW}Estimated cost: \$15-\$30${NC}"
        read -p "Continue? (y/N) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            echo -e "${GREEN}Retranslating all docs → Spanish${NC}"
            python scripts/bulk_retranslate.py --language es
        else
            echo "Cancelled"
            exit 0
        fi
        ;;
    
    all-langs)
        echo -e "${RED}⚠️  WARNING: This will retranslate ALL docs to ALL languages${NC}"
        echo -e "${RED}Estimated cost: \$45-\$90${NC}"
        read -p "Are you absolutely sure? (y/N) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            echo -e "${GREEN}Retranslating all docs → all languages${NC}"
            python scripts/bulk_retranslate.py --language es fr ar
        else
            echo "Cancelled"
            exit 0
        fi
        ;;
    
    dry-run)
        echo -e "${GREEN}Dry run - showing what would be translated${NC}"
        python scripts/bulk_retranslate.py --language es --dry-run --verbose
        ;;
    
    custom)
        shift
        echo -e "${GREEN}Running custom bulk retranslation${NC}"
        python scripts/bulk_retranslate.py "$@"
        ;;
    
    *)
        echo -e "${RED}Unknown command: $1${NC}"
        echo "Run '$0' with no arguments to see available commands"
        exit 1
        ;;
esac
