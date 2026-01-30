"""
BOUNDARY TEST: Tier-0 Protocol Conformance

PURPOSE: Verify Tier-2 does not redefine Tier-0 protocol invariants
STATUS: CRITICAL ARCHITECTURAL TEST
TIER RELATIONSHIPS:
  - Tier-0: Normative authority (protocol definition)
  - Tier-2: Must respect Tier-0 without redefinition
  - Other tiers: Must maintain clear authority hierarchy

TEST STRATEGY:
- Check for Tier-0 protocol term redefinition
- Verify authority acknowledgments in documentation
- Ensure no protocol semantics are introduced
"""

import os
import re

def test_no_tier0_protocol_redefinition():
    """Verify Tier-2 doesn't redefine Tier-0 protocol terms."""
    # Terms that indicate protocol redefinition attempts
    redefinition_patterns = [
        r'define\s+.*protocol',
        r'redefine',
        r'override',
        r'extend\s+.*protocol',
        r'new\s+.*standard',
        r'authoritative\s+.*definition'
    ]
    
    violations = []
    
    # Scan Python files for redefinition attempts
    for root, dirs, files in os.walk('tier2_core'):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                    
                    # Check for redefinition patterns
                    for pattern in redefinition_patterns:
                        if re.search(pattern, content, re.IGNORECASE):
                            # Check if it's in a comment (allowed) vs code (not allowed)
                            lines = content.split('\n')
                            for i, line in enumerate(lines):
                                if re.search(pattern, line, re.IGNORECASE):
                                    if not line.strip().startswith('#'):
                                        violations.append(f"Line {i+1} in {file_path}: {line.strip()}")
    
    assert len(violations) == 0, f"Tier-0 protocol redefinition violations:\n" + "\n".join(violations)
    print("✅ No Tier-0 protocol redefinition detected")

def test_tier0_authority_acknowledged():
    """Verify Tier-0 authority is properly acknowledged in documentation."""
    # Check architecture documentation
    architecture_docs = [
        'docs/TIER2_ARCHITECTURAL_CHARTER.md',
        'docs/TIER2_LOCK_SURFACE.md',
        'README.md'
    ]
    
    missing_acknowledgments = []
    for doc_path in architecture_docs:
        if os.path.exists(doc_path):
            with open(doc_path, 'r') as f:
                content = f.read()
                if 'Tier-0' not in content and 'authority' not in content.lower():
                    missing_acknowledgments.append(doc_path)
    
    assert len(missing_acknowledgments) == 0, \
        f"Missing Tier-0 authority acknowledgment in: {missing_acknowledgments}"
    
    print("✅ Tier-0 authority acknowledged in all architecture documentation")

def test_clear_tier_separation():
    """Verify clear separation between tiers is documented."""
    separation_indicators = [
        'Tier-0',
        'Tier-1',
        'Tier-2',
        'separation',
        'boundary',
        'authority hierarchy'
    ]
    
    found_indicators = 0
    
    # Check key documentation files
    for root, dirs, files in os.walk('docs'):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                    for indicator in separation_indicators:
                        if indicator in content:
                            found_indicators += 1
    
    # Should have at least some separation documentation
    assert found_indicators >= 3, "Insufficient tier separation documentation"
    
    print(f"✅ Tier separation documented with {found_indicators} indicators")

if __name__ == '__main__':
    test_no_tier0_protocol_redefinition()
    test_tier0_authority_acknowledged()
    test_clear_tier_separation()
    print("All Tier-0 conformance boundary tests passed")
