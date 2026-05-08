#!/usr/bin/env python3

from datetime import datetime
from enum import Enum
from typing import List
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission_rules(self) -> 'SpaceMission':
        # Règle 1 : l'ID doit commencer par "M"
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        # Règle 2 : au moins un Commander ou Captain
        high_ranks = {Rank.commander, Rank.captain}
        has_leader = any(member.rank in high_ranks for member in self.crew)
        if not has_leader:
            raise ValueError("Mission must have at least one Commander or Captain")

        # Règle 3 : missions longues (> 365 jours) → 50% expérimentés (5+ ans)
        if self.duration_days > 365:
            experienced = sum(1 for m in self.crew if m.years_experience >= 5)
            ratio = experienced / len(self.crew)
            if ratio < 0.5:
                raise ValueError(
                    "Long missions (> 365 days) require at least 50% experienced crew (5+ years)"
                )

        # Règle 4 : tous les membres doivent être actifs
        inactive = [m.name for m in self.crew if not m.is_active]
        if inactive:
            raise ValueError(
                f"All crew members must be active. Inactive: {', '.join(inactive)}"
            )

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 41)

    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date="2024-06-01T09:00:00",
        duration_days=900,
        budget_millions=2500.0,
        crew=[
            CrewMember(
                member_id="SC001",
                name="Sarah Connor",
                rank=Rank.commander,
                age=42,
                specialization="Mission Command",
                years_experience=18,
            ),
            CrewMember(
                member_id="JS002",
                name="John Smith",
                rank=Rank.lieutenant,
                age=35,
                specialization="Navigation",
                years_experience=10,
            ),
            CrewMember(
                member_id="AJ003",
                name="Alice Johnson",
                rank=Rank.officer,
                age=28,
                specialization="Engineering",
                years_experience=6,
            ),
        ],
    )

    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f"  - {member.name} ({member.rank.value}) - {member.specialization}")

    print("=" * 41)

    # Cas invalide : aucun Commander ou Captain
    try:
        SpaceMission(
            mission_id="M2024_FAIL",
            mission_name="Doomed Mission",
            destination="Venus",
            launch_date="2024-07-01T09:00:00",
            duration_days=180,
            budget_millions=500.0,
            crew=[
                CrewMember(
                    member_id="AB001",
                    name="Alex Brown",
                    rank=Rank.officer,
                    age=30,
                    specialization="Science",
                    years_experience=3,
                ),
                CrewMember(
                    member_id="CD002",
                    name="Chris Davis",
                    rank=Rank.cadet,
                    age=22,
                    specialization="Engineering",
                    years_experience=1,
                ),
            ],
        )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
