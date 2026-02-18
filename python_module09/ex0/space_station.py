from pydantic import Field, BaseModel, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    try:
        spacestation = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            is_operational=True,
            last_maintenance="2013-11-04T11:11:11",
        )

        print("Space Station Data Validation")
        print("========================================")
        print("Valid station created:")
        print(f"ID: {spacestation.station_id}")
        print(f"Name: {spacestation.name}")
        print(f"Crew: {spacestation.crew_size} people")
        print(f"Power: {spacestation.power_level}%")
        print(f"Oxygen: {spacestation.oxygen_level}%")
        if spacestation.is_operational:
            print("Status: Operational")
        else:
            print("Status: Not operational")

        print("========================================")
        print("Expected validation error:")
        SpaceStation(
            station_id="ISS002",
            name="International Space Station",
            crew_size=38,
            power_level=85.5,
            oxygen_level=92.3,
            is_operational=True,
            last_maintenance="2013-11-04T11:11:11",
        )
    except ValidationError:
        print("Input should be less than or equal to 20")
    except Exception:
        print("Error")


if __name__ == "__main__":
    main()
