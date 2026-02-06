from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tier1.pure_functions import *
from typing import Dict, Any
import uvicorn

app = FastAPI(title="SeekReap Tier-2 Runtime")

# In-memory store (Tier-2 responsibility)  
store = {}

class BehaviorInput(BaseModel):
    type: str
    intensity: float

@app.post("/v1/seekers")
def api_create_seeker():
    return create_seeker()

@app.post("/v1/reaps/{seeker_id}")
def api_create_reap(seeker_id: str):
    return create_reap(seeker_id)

@app.post("/v1/behaviors/{reap_id}")
def api_record_behavior(reap_id: str, data: BehaviorInput):
    behavior = record_behavior(reap_id, data.dict())
    store[behavior.id] = behavior  # Tier-2 storage
    return behavior

@app.post("/v1/verify/{reap_id}")
def api_verify_reap(reap_id: str):
    reap = store.get(reap_id, create_reap("dummy"))
    verified = verify_reap(reap)
    store[reap_id] = verified
    return verified

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
