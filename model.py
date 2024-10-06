from pydantic import BaseModel
from typing import Optional
from enum import Enum

class Direction(str, Enum):
    BUY = "BUY"
    HOLD = "HOLD"
    SELL = "SELL"

class LLMResponse(BaseModel):
    direction: Direction
    strength: float
    rationale: str

    class Config:
        from_attributes = True 

class Agent(BaseModel):
    name: str
    type: str
    description: str
    isReal: bool = False
    realContext: Optional[str] = ''
    llmResponse: Optional[LLMResponse] = None

    class Config:
        from_attributes = True 
