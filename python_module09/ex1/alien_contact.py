from pydantic import BaseModel, Field, ValidationError
from enum import Enum
from typing import Optional
from datetime import datetime

class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"

class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    
    @model_validator(mode='after')
    def validate_contact(self) -> 'AlienContact':
        valid = (self.contact_id[0] == 'A' and 
        self.contact_id[1] == 'C')

        if not valid:
            raise ValueError("Contact ID must start with 'AC'")
        
        if self.contact_type == ContactType.PHYSICAL:
            if not self.is_verified:
                raise ValueError("Physical contact reports must be verified")
        
        if self.contact_type == ContactType.TELEPATHIC:
            if self.witness_count < 3:
                raise ValueError("Telepathic contact requires at least 3 witnesses")

        if self.signal_strength > 7.0:
            if self.message_received is None:
                raise ValueError("Strong signals should include received messages")
        return self
