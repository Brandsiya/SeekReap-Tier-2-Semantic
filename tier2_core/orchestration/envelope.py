"""
Semantic envelope creation according to Tier-2 specifications.
ADR-001: Use deepcopy for immutability
ADR-002: Signature format: tier2-semantic-{policy}-{timestamp_ms}-{random}
ADR-003: Fixed required fields structure
"""
import time
import uuid
from copy import deepcopy
from typing import Any, Dict, Optional

def create_envelope(
    payload: Any,
    policy: str = "default",
    metadata: Optional[Dict] = None
) -> Dict:
    """
    Create a semantic envelope wrapping the given payload.
    
    Args:
        payload: The data to wrap (will be deep copied)
        policy: Orchestration policy applied
        metadata: Optional context dictionary
    
    Returns:
        Dict with required envelope fields:
        - id: Unique identifier
        - timestamp: Unix timestamp
        - payload: Deep copy of input
        - schema_version: "tier2-envelope-v1"
        - orchestration_policy: Policy applied
        - signature: Unique traceable signature
        - metadata: Optional (if provided)
    """
    # ADR-001: Use deepcopy for immutability
    immutable_payload = deepcopy(payload)
    
    # Generate unique ID
    unique_id = f"tier2-envelope-{uuid.uuid4()}"
    
    # Get current timestamp
    timestamp = time.time()
    
    # ADR-002: Create signature with millisecond precision
    timestamp_ms = int(timestamp * 1000)
    random_suffix = uuid.uuid4().hex[:8]
    signature = f"tier2-semantic-{policy}-{timestamp_ms}-{random_suffix}"
    
    # ADR-003: Required fields structure
    envelope = {
        "id": unique_id,
        "timestamp": timestamp,
        "payload": immutable_payload,
        "schema_version": "tier2-envelope-v1",
        "orchestration_policy": policy,
        "signature": signature,
    }
    
    # Add metadata if provided
    if metadata is not None:
        envelope["metadata"] = deepcopy(metadata)
    
    return envelope


def create_envelope_from_tier1(
    tier1_function: str,
    *args,
    metadata: Optional[Dict] = None
) -> Dict:
    """
    Create an envelope by executing a Tier-1 atomic behavior.
    
    Args:
        tier1_function: Name of Tier-1 function to call
        *args: Arguments to pass to the Tier-1 function
        metadata: Optional metadata
    
    Returns:
        Semantic envelope containing the result
    """
    from .tier1_adapter import (
        add, subtract, multiply, divide,
        process_data, filter_even,
        process_text, reverse_string,
        calculator_behavior, example_behavior, my_feature_behavior
    )
    
    # Map function names to actual functions
    function_map = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
        "calculator_behavior": calculator_behavior,
        "process_data": process_data,
        "filter_even": filter_even,
        "process_text": process_text,
        "reverse_string": reverse_string,
        "example_behavior": example_behavior,
        "my_feature_behavior": my_feature_behavior,
    }
    
    if tier1_function not in function_map:
        raise ValueError(f"Unknown Tier-1 function: {tier1_function}")
    
    # Execute the Tier-1 behavior
    func = function_map[tier1_function]
    result = func(*args)
    
    # Create envelope with result
    return create_envelope(
        payload=result,
        policy=f"tier1_{tier1_function}",
        metadata=metadata
    )
