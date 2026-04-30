from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability


def test_healing_factory(factory: HealingCreatureFactory) -> None:
    """Test base and evolved Creatures with healing capability."""
    print("Testing Creature with healing capability")
    pairs = [("base", factory.create_base()), ("evolved", factory.create_evolved())]
    for label, creature in pairs:
        print(f"{label}:")
        print(creature.describe())
        print(creature.attack())
        if isinstance(creature, HealCapability):
            print(creature.heal())


def test_transform_factory(factory: TransformCreatureFactory) -> None:
    """Test base and evolved Creatures with transform capability."""
    print("Testing Creature with transform capability")
    pairs = [("base", factory.create_base()), ("evolved", factory.create_evolved())]
    for label, creature in pairs:
        print(f"{label}:")
        print(creature.describe())
        print(creature.attack())
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())


if __name__ == "__main__":
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    test_healing_factory(healing_factory)
    test_transform_factory(transform_factory)
