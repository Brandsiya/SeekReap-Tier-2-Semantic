import uuid
from typing import Dict, List, Any
from dataclasses import dataclass
from taxonomy import TAXONOMY, VALID_TYPES
from datetime import datetime

@dataclass
class Seeker:
    id: str
    created_at: str
    status: str

@dataclass  
class Reap:
    id: str
    seeker_id: str
    start_time: str
    end_time: str
    duration: int
    status: str
    score: float = 0.0
    behaviors: List[str] = None

@dataclass
class Behavior:
    id: str
    reap_id: str
    type: str
    intensity: float
    timestamp: str

def create_seeker() -> Seeker:
    """Tier-0: Returns active Seeker with UUID"""
    return Seeker(
        id=str(uuid.uuid4()),
        created_at=datetime.utcnow().isoformat(),
        status="active"
    )

def create_reap(seeker_id: str) -> Reap:
    """Tier-0: Returns pending Reap"""
    now = datetime.utcnow().isoformat()
    return Reap(
        id=str(uuid.uuid4()),
        seeker_id=seeker_id,
        start_time=now,
        end_time=now,
        duration=0,
        status="pending",
        behaviors=[]
    )

def record_behavior(reap_id: str, behavior_data: Dict[str, Any]) -> Behavior:
    """Tier-0: Validate TAXONOMY + constraints"""
    if behavior_data["type"] not in VALID_TYPES:
        raise ValueError(f"Invalid type: {behavior_data['type']}")
    if not 0.0 <= behavior_data["intensity"] <= 1.0:
        raise ValueError(f"Intensity out of range: {behavior_data['intensity']}")
    
    return Behavior(
        id=str(uuid.uuid4()),
        reap_id=reap_id,
        type=behavior_data["type"],
        intensity=behavior_data["intensity"],
        timestamp=datetime.utcnow().isoformat()
    )

def verify_reap(reap: Reap) -> Reap:
    """Tier-0: score >= 0.70 AND >=3 behaviors"""
    if len(reap.behaviors) < 3:
        reap.status = "rejected"
        return reap
    
    score = 0.0
    for behavior_id in reap.behaviors:
        # Simulate score calculation (in real: fetch behaviors)
        score += 0.8  # Mock passing score
    
    if score >= 0.70:
        reap.status = "verified"
        reap.score = score
    else:
        reap.status = "rejected"
    
    return reap

def emit_verification_event(reap_id: str) -> Dict[str, Any]:
    """Tier-0: Idempotent event (verified only)"""
    # Mock event emission (pure function)
    return {"event": "verification_complete", "reap_id": reap_id}
