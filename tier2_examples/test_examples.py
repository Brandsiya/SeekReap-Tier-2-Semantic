"""
TEST: Verify example functionality works correctly
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tier2_examples.envelope_usage_example import (
    example_basic_envelope_creation,
    example_workflow_composition,
    example_data_pipeline,
    example_error_handling_and_recovery,
    example_audit_and_compliance
)

def test_examples():
    """Test that examples run without errors."""
    print("Testing example execution...")
    
    try:
        # Test basic creation
        print("1. Testing basic envelope creation...")
        example_basic_envelope_creation()
        print("   ✅ Basic creation successful")
        
        # Test workflow composition
        print("2. Testing workflow composition...")
        example_workflow_composition()
        print("   ✅ Workflow composition successful")
        
        # Test data pipeline
        print("3. Testing data pipeline...")
        example_data_pipeline()
        print("   ✅ Data pipeline successful")
        
        # Test error handling
        print("4. Testing error handling...")
        example_error_handling_and_recovery()
        print("   ✅ Error handling successful")
        
        # Test audit and compliance
        print("5. Testing audit and compliance...")
        example_audit_and_compliance()
        print("   ✅ Audit and compliance successful")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Example failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    if test_examples():
        print("\n✅ All examples executed successfully!")
        sys.exit(0)
    else:
        print("\n❌ Some examples failed")
        sys.exit(1)
