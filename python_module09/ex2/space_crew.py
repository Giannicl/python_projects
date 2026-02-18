from pydantic import BaseModel, ValidationError, model_validator, Field
from datetime import datetime
from typing import List
from enum import Enum


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def mission_validation(self) -> "SpaceMission":

        if self.mission_id[0] != "M":
            raise ValueError("Mission ID must start with 'M'")

        has_leader = False
        for member in self.crew:
            if member.rank == Rank.COMMANDER or member.rank == Rank.CAPTAIN:
                has_leader = True
                break
        if not has_leader:
            raise ValueError("Must have at least one Commander or Captain")

        if self.duration_days > 365:
            count = 0
            length = 0
            for crew in self.crew:
                length = length + 1
            for member in self.crew:
                if member.years_experience >= 5:
                    count = count + 1
            if length / count > 2:
                raise ValueError(
                    "Long missions (> 365 days) need "
                    "50% experienced crew (5+ years)"
                )

        for member in self.crew:
            if member.is_active is False:
                raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    try:
        sarah = CrewMember(
            member_id="S10",
            name="Sarah Connor",
            rank="commander",
            age=30,
            specialization="Mission Command",
            years_experience=10,
        )
        john = CrewMember(
            member_id="J10",
            name="John Smith",
            rank="lieutenant",
            age=25,
            specialization="Navigation",
            years_experience=5,
        )
        alice = CrewMember(
            member_id="A10",
            name="Alice Johnson",
            rank="officer",
            age=29,
            specialization="Engineering",
            years_experience=8,
        )
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2015-01-01T01:01:01",
            duration_days=900,
            crew=[sarah, john, alice],
            budget_millions=2500.0,
        )

        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        size = 0
        for crew in mission.crew:
            size = size + 1
        print(f"Crew size: {size}")

        print("Crew members:")
        print(
            f"- {mission.crew[0].name} ({mission.crew[0].rank.value}) - "
            f"{mission.crew[0].specialization}"
        )
        print(
            f"- {mission.crew[1].name} ({mission.crew[1].rank.value}) - "
            f"{mission.crew[1].specialization}"
        )
        print(
            f"- {mission.crew[2].name} ({mission.crew[2].rank.value}) - "
            f"{mission.crew[2].specialization}"
        )

        print("=========================================")
        print("Expected validation error:")
        SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2015-01-01T01:01:01",
            duration_days=900,
            crew=[john, alice],
            budget_millions=2500.0,
        )
    except ValidationError:
        print("Mission must have at least one Commander or Captain")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
