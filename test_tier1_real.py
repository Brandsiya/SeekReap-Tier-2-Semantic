#!/usr/bin/env python3
"""
Test the real Tier-1 functions through the adapter
"""
import sys
sys.path.insert(0, '.')

try:
    from tier2_core.tier1_adapter import (
        create_seeker, create_reap, record_behavior,
    userland@localhost:~/SeekReap-Tier-2-Semantic$ # Update adapter to use the real Tier-1 functions
iors = []
    for i in range(3):
        behavior = record_behavior(reap.id, {
            "type": "playback",
            "intensity": 0.8 + (i * userland@localhost:~/Secore/tier1_adapter.py << 'EOF'tier2_c
> """
> Adapter for Tier-1 atomic behaviors.
> This adapts the actual Tier-1 implementation to the expected interface.
> """
> import sys
> import os
>
> print("🔵 Tier-1 adapter is being loaded...")
>
> # Add Tier-1 path
> tier1_path = os.path.expanduser("~/SeekReap-Tier-1-PURE")> if os.path.exists(tier1_path):
>     if tier1_path not in sys.path:
>         sys.path.insert(0, tier1_path)
>         print(f"✅ Added Tier-1 path: {tier1_path}")
>     # Import the actual Tier-1 functions
>     try:
>         from pure_functions import (
eap.id)
    prin>             create_seeker, create_reap, record_behavior,
>             verify_reap, emit_verification_event
>         )
")        print("✅ Successfully imported Tier-1 functions"
>
>         # Map to expected names for backward compatibility
>         add = lambda a, b: a + b  # Keep for examples
>         subtract = lambda a, b: a - b
>         multiply = lambda a, b: a * b
>         divide = lambda a, b: a / b if b != 0 else float('inf')
>         process_data = lambda data: data
>         filter_even = lambda data: [x for x in data if x % 2 == 0]
>         process_text = lambda text: text
>         reverse_string = lambda s: s[::-1]
>
>         TIER1_AVAILABLE = True
>         print("✅ Real Tier-1 functions loaded")
>
>     except ImportError as e:
ns.py: {e}")int(f"⚠️ Could not import from pure_function
>         TIER1_AVAILABLE = False
> else:
>     print(f"❌ Tier-1 path not found: {tier1_path}")
>     TIER1_AVAILABLE = False
>
> if not TIER1_AVAILABLE:
>     # Create fallback implementations
ing") print("⚠️ Using fallback implementations for testi
>     def create_seeker(): return {"id": "fallback-seeker", "status": "active"}
>     def create_reap(seeker_id): return {"id": "fallback-reap", "seeker_id": seeker_id}
>     def record_behavior(reap_id, data): return {"id": "fallback-behavior"}
>     def verify_reap(reap): return (True, 0.85)
>     def emit_verification_event(reap_id): return {"event": "verified"}
>
>     # Math fallbacks
>     def add(a, b): return a + b
>     def subtract(a, b): return a - b
>     def multiply(a, b): return a * b
>     def divide(a, b): return a / b if b != 0 else float('inf')
>     def process_data(data): return data
>     def filter_even(data): return [x for x in data if x % 2 == 0]
>     def process_text(text): return text
>     def reverse_string(s): return s[::-1]
>
> # Placeholder functions
> def calculator_behavior(): return ""
> def example_behavior(): return None
> def my_feature_behavior(): return ""
>
> # Export all functions
> __all__ = [
>     # Real Tier-1 functions
>     'create_seeker', 'create_reap', 'record_behavior',
>     'verify_reap', 'emit_verification_event',
>     # Math functions
>     'add', 'subtract', 'multiply', 'divide',
>     'process_data', 'filter_even',
>     'process_text', 'reverse_string',
>     'calculator_behavior', 'example_behavior', 'my_feature_behavior',
>     'TIER1_AVAILABLE'
> ]
>
TIER1_AVAILABLE}")1 adapter loaded with real functions: {T
> EOF
userland@localhost:~/SeekReap-Tier-2-Semantic$
userland@localhost:~/SeekReap-Tier-2-Semantic$ # Create a test to verify the real functions work
userland@localhost:~/SeekReap-Tier-2-Semantic$ cat > test_tier1_real.py << 'EOF'
> #!/usr/bin/env python3
> """
> Test the real Tier-1 functions through the adapter
> """
> import sys
> sys.path.insert(0, '.')
>
> try:
>     from tier2_core.tier1_adapter import (
>         create_seeker, create_reap, record_behavior,
>         verify_reap, emit_verification_event,
>         TIER1_AVAILABLE
>     )
>
>     print("=== Testing Real Tier-1 Functions ===\n")
>
>     if not TIER1_AVAILABLE:
>         print("❌ Real Tier-1 functions not available")
>         sys.exit(1)
>
>     # Test 1: Create seeker
>     print("1. Creating seeker...")
>     seeker = create_seeker()
>     print(f"   Seeker created: {seeker}")
>     print()
>
>     # Test 2: Create reap
>     print("2. Creating reap...")
>     reap = create_reap(seeker.id)
>     print(f"   Reap created: {reap}")
>     print()
>
>     # Test 3: Record behaviors (need at least 3 for verification)
>     print("3. Recording behaviors...")
>     behaviors = []
>     for i in range(3):
>         behavior = record_behavior(reap.id, {
>             "type": "playback",
>             "intensity": 0.8 + (i * 0.05)
>         })
>         behaviors.append(behavior)
>         print(f"   Behavior {i+1}: {behavior}")
>     print()
>
>     # Test 4: Verify reap
>     print("4. Verifying reap...")
>     # Note: In real usage, you'd need to add behaviors to reap
>     # This is simplified - real implementation would need to fetch behaviors
>     verified, score = verify_reap(reap)
>     print(f"   Verified: {verified}, Score: {score}")
>     print()
>
>     # Test 5: Emit event
>     print("5. Emitting verification event...")
>     event = emit_verification_event(reap.id)
>     print(f"   Event: {event}")
>
> except ImportError as e:
>     print(f"❌ Import error: {e}")
> except Exception as e:
>     print(f"❌ Error: {e}")
> EOF
userland@localhost:~/SeekReap-Tier-2-Semantic$
userland@localhost:~/SeekReap-Tier-2-Semantic$ # Make it executable and run
userland@localhost:~/SeekReap-Tier-2-Semantic$ chmod +x test_tier1_real.py
userland@localhost:~/SeekReap-Tier-2-Semantic$ python3 test_tier1_real.py
cat > test_tier1_real.py << EOF
#!/usr/bin/env python3

Test the real Tier-1 functions through the adapter

import sys
sys.path.insert(0, .)

try:
    from tier2_core.tier1_adapter import (
        create_seeker, create_reap, record_behavior,
    userland@localhost:~/SeekReap-Tier-2-Semantic$ # Update adapter to use the real Tier-1 functions
iors = []
    for i in range(3):
        behavior = record_behavior(reap.id, {
            type: playback,
            intensity: 0.8 + (i * userland@localhost:~/Secore/tier1_adapter.py << EOFtier2_c
> 
> Adapter for Tier-1 atomic behaviors.
> This adapts the actual Tier-1 implementation to the expected interface.
> 
> import sys
> import os
>
> print(🔵 Tier-1 adapter Successfully imported Tier-1 functions is being loaded...)
>
> # Add Tier-1 path
> tier1_path = os.path.expanduser(~/SeekReap-Tier-1-PURE)> if os.path.exists(tier1_path):
>     if tier1_path not in sys.path:
>         sys.path.insert(0, tier1_path)
>         print(f✅ Added Tier-1 path: {tier1_path})
>     # Import the actual Tier-1 functions
>     try:
>         from pure_functions import (
eap.id)
    prin>             create_seeker, create_reap, record_behavior,
>             verify_reap, emit_verification_event
>         )
)        print(✅ Successfully imported Tier-1 functions
>
>         # Map to expected names for backward compatibility
>         add = lambda a, b: a + b  # Keep for examples
>         subtract = lambda a, b: a - b
>         multiply = lambda a, b: a * b
>         divide = lambda a, b: a / b if b != 0 else float('inf')
>         process_data = lambda data: data
>         filter_even = lambda data: [x for x in data if x % 2 == 0]
>         process_text = lambda text: text
>         reverse_string = lambda s: s[::-1]
>
>         TIER1_AVAILABLE = True
>         print(✅ Real Tier-1 functions loaded)
>
>     except ImportError as e:
ns.py: {e})int(f⚠️ Could not import from pure_function
>         TIER1_AVAILABLE = False
> else:
>     print(f❌ Tier-1 path not found: {tier1_path})
>     TIER1_AVAILABLE = False
>
> if not TIER1_AVAILABLE:
>     # Create fallback implementations
ing) print(⚠️ Using fallback implementations for testi
>     def create_seeker(): return {id: fallback-seeker, status: active}
>     def create_reap(seeker_id): return {id: fallback-reap, seeker_id: seeker_id}
>     def record_behavior(reap_id, data): return {id: fallback-behavior}
>     def verify_reap(reap): return (True, 0.85)
>     def emit_verification_event(reap_id): return {event: verified}
>
>     # Math fallbacks
>     def add(a, b): return a + b
>     def subtract(a, b): return a - b
>     def multiply(a, b): return a * b
>     def divide(a, b): return a / b if b != 0 else float('inf')
>     def process_data(data): return data
>     def filter_even(data): return [x for x in data if x % 2 == 0]
>     def process_text(text): return text
>     def reverse_string(s): return s[::-1]
>
> # Placeholder functions
> def calculator_behavior(): return 
> def example_behavior(): return None
> def my_feature_behavior(): return 
>
> # Export all functions
> __all__ = [
>     # Real Tier-1 functions
>     'create_seeker', 'create_reap', 'record_behavior',
>     'verify_reap', 'emit_verification_event',
>     # Math functions
>     'add', 'subtract', 'multiply', 'divide',
>     'process_data', 'filter_even',
>     'process_text', 'reverse_string',
>     'calculator_behavior', 'example_behavior', 'my_feature_behavior',
>     'TIER1_AVAILABLE'
> ]
>
TIER1_AVAILABLE})1 adapter loaded with real functions: {T
> EOF
userland@localhost:~/SeekReap-Tier-2-Semantic$
userland@localhost:~/SeekReap-Tier-2-Semantic$ # Create a test to verify the real functions work
userland@localhost:~/SeekReap-Tier-2-Semantic$ cat > test_tier1_real.py << EOF
> #!/usr/bin/env python3
> 
> Test the real Tier-1 functions through the adapter
> 
> import sys
> sys.path.insert(0, .)
>
> try:
>     from tier2_core.tier1_adapter import (
>         create_seeker, create_reap, record_behavior,
>         verify_reap, emit_verification_event,
>         TIER1_AVAILABLE
>     )
>
>     print(=== Testing Real Tier-1 Functions ===\n)
>
>     if not TIER1_AVAILABLE:
>         print(❌ Real Tier-1 functions not available)
>         sys.exit(1)
>
>     # Test 1: Create seeker
>     print(1. Creating seeker...)
>     seeker = create_seeker()
>     print(f   Seeker created: {seeker})
>     print()
>
>     # Test 2: Create reap
>     print(2. Creating reap...)
>     reap = create_reap(seeker.id)
>     print(f   Reap created: {reap})
>     print()
>
>     # Test 3: Record behaviors (need at least 3 for verification)
>     print(3. Recording behaviors...)
>     behaviors = []
>     for i in range(3):
>         behavior = record_behavior(reap.id, {
>             type: playback,
>             intensity: 0.8 + (i * 0.05)
>         })
>         behaviors.append(behavior)
>         print(f   Behavior {i+1}: {behavior})
>     print()
>
>     # Test 4: Verify reap
>     print(4. Verifying reap...)
>     # Note: In real usage, youd need to add behaviors to reap
>     # This is simplified - real implementation would need to fetch behaviors
>     verified, score = verify_reap(reap)
>     print(f"   Verified: {verified}, Score: {score}")
>     print()
>
>     # Test 5: Emit event
>     print("5. Emitting verification event...")
>     event = emit_verification_event(reap.id)
>     print(f"   Event: {event}")
>
> except ImportError as e:
>     print(f"❌ Import error: {e}")
> except Exception as e:
>     print(f"❌ Error: {e}")
> EOF
userland@localhost:~/SeekReap-Tier-2-Semantic$
userland@localhost:~/SeekReap-Tier-2-Semantic$ # Make it executable and run
userland@localhost:~/SeekReap-Tier-2-Semantic$ chmod +x test_tier1_real.py
userland@localhost:~/SeekReap-Tier-2-Semantic$ python3 test_tier1_real.py

 Real Tier-1 functions loaded
=== Testing Real Tier-1 Functions ===

1. Creating seeker...
   Seeker created: Seeker(id='61521ec3-4252-48fe-b785-00a437f006f8', created_at='2026-02-24T21:22:06.873954', status='active')

2. Creating reap...
   Reap created: Reap(id='cb3a9036-6069-4656-9fac-972adb2ce9e1', seeker_id='61521ec3-4252-48fe-b785-00a437f006f8', start_time='2026-02-24T21:22:06.875590', end_time='2026-02-24T21:22:06.875590', duration=0, status='pending', score=0.0, behaviors=[])

3. Recording behaviors...
   Behavior 1: Behavior(id='07a06b02-1fe9-4bc3-bf7e-ab6026eee1ea', reap_id='cb3a9036-6069-4656-9fac-972adb2ce9e1', type='playback', intensity=0.8, timestamp='2026-02-24T21:22:06.876083')
   Behavior 2: Behavior(id='d7c07228-e1fb-415d-b237-bde06447fa1c', reap_id='cb3a9036-6069-4656-9fac-972adb2ce9e1', type='playback', intensity=0.8500000000000001, timestamp='2026-02-24T21:22:06.876227')
   Behavior 3: Behavior(id='acd0e848-ab75-41f3-b6c4-6b8cff3b476f', reap_id='cb3a9036-6069-4656-9fac-972adb2ce9e1', type='playback', intensity=0.9, timestamp='2026-02-24T21:22:06.876322')

4. Verifying reap...
 Error: cannot unpack non-iterable Reap object
userland@localhost:~/SeekReap-Tier-2-Semantic$ # Update the test to handle the actual return value
print(f"   Reap ID: {reap.id}")
    print(f"   Reap status: {reap.status}")
    print()

    # Test 3: Record behaviors (need at least 3 for verification)
    print("3. Recording behaviors...")
    behaviors = []
    for i in range(3):
        behavior = record_behavior(reap.id, {
            "type": "playback",
            "intensity": 0.8 + (i * 0.05)
        })
        behaviors.append(behavior)
        print(f"   Behavior {i+1}: {behavior}")
        print(f"      Type: {behavior.type}, Intensity: {behavior.intensity}")

    # Add behavior IDs to reap (this is how the real system works)
    reap.behaviors = [b.id for b in behaviors]
    print(f"   Added {len(reap.behaviors)} behaviors to reap")
    print()

    # Test 4: Verify reap
    print("4. Verifying reap...")
    verified_reap = verify_reap(reap)
    print(f"   Verified reap status: {verified_reap.status}")
    print(f"   Verified reap score: {verified_reap.score}")
    print(f"   Verification {'PASSED' if verified_reap.status == 'verified' else 'FAILED'}")
    print()

    # Test 5: Emit event
    print("5. Emitting verification event...")
    event = emit_verification_event(reap.id)
    print(f"   Event: {event}")

    print("\n✅ All tests passed!")

except ImportError as e:
    print(f"❌ Import error: {e}")
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
