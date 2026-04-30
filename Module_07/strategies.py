from abc import ABC, abstractmethod
from typing import Union
from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    """Raised when a strategy is used with an incompatible Creature."""
    pass


class BattleStrategy(ABC):
    """Abstract strategy for how a Creature acts during a tournament battle."""

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Return True if the Creature is compatible with this strategy."""
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        """Execute the strategy's actions for the given Creature."""
        pass


class NormalStrategy(BattleStrategy):
    """Simple strategy: just attack. Valid for any Creature."""

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this normal strategy"
            )
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    """Aggressive strategy: transform, attack, revert. Only for TransformCapability."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this aggressive strategy"
            )
        tc: Union[Creature, TransformCapability] = creature
        assert isinstance(tc, TransformCapability)
        print(tc.transform())
        print(creature.attack())
        print(tc.revert())


class DefensiveStrategy(BattleStrategy):
    """Defensive strategy: attack then heal. Only for HealCapability."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this defensive strategy"
            )
        print(creature.attack())
        hc: Union[Creature, HealCapability] = creature
        assert isinstance(hc, HealCapability)
        print(hc.heal())
