from pydantic import BaseModel, Field, ValidationError, model_validator
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

def main() -> None:
    try:
        print("Alien Contact Log Validation")
        print("======================================")
        alien_contact = AlienContact(
                        contact_id = "AC_2024_001",
                        timestamp = "2015-08-01T01:01:01",
                        location = "Area 51, Nevada",
                        contact_type = "radio",
                        signal_strength = 8.5,
                        duration_minutes = 45,
                        witness_count = 5,
                        message_received = "Greetings from Zeta Reticuli",
        )
        print("Valid contact report:")
        print(f"ID: {alien_contact.contact_id}")
        print(f"Type: {alien_contact.contact_type.value}")
        print(f"Location: {alien_contact.location}")
        print(f"Signal: {alien_contact.signal_strength}/10")
        print(f"Duration: {alien_contact.duration_minutes} minutes")
        print(f"Witnesses: {alien_contact.witness_count}")
        print(f"Message: '{alien_contact.message_received}'")
        print("=====================================")
        print("Expected validation error:")
        alien_contact2 = AlienContact(
                        contact_id = "AC_2024_001",
                        timestamp = "2015-08-01T01:01:01",
                        location = "Area 51, Nevada",
                        contact_type = "telepathic",
                        signal_strength = 8.5,
                        duration_minutes = 45,
                        witness_count = 2,
                        message_received = "Greetings from Zeta Reticuli",
        )
       
    except ValidationError:
        print("Telepathic contact requires at least 3 witnesses")
    except Exception as e:
        print(e)

main()
