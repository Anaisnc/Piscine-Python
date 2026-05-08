from abc import ABC, abstractmethod
from ex0.creatures import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    """Abstract factory for creating Creatures of a given family."""

    @abstractmethod
    def create_base(self) -> Creature:
        """Create and return the base Creature of the family."""
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Create and return the evolved Creature of the family."""
        pass


class FlameFactory(CreatureFactory):
    """Factory for the Flame family: Flameling and Pyrodon."""

    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    """Factory for the Aqua family: Aquabub and Torragon."""

    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
