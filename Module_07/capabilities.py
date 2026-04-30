from abc import ABC, abstractmethod


class HealCapability(ABC):
    """Abstract class for Creatures with a healing capability."""

    @abstractmethod
    def heal(self) -> str:
        """Return a string describing the healing action."""
        pass


class TransformCapability(ABC):
    """Abstract class for Creatures with a transform/revert capability."""

    def __init__(self) -> None:
        self.transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        """Return a string describing the transformation."""
        pass

    @abstractmethod
    def revert(self) -> str:
        """Return a string describing the reversion."""
        pass
