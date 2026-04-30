from alchemy.elements import create_air  # absolute import
from ..potions import strength_potion  # relative import
import elements as root_elements  # root-level elements


def lead_to_gold() -> str:
    return (
        f"Recipe transmuting Lead to Gold: brew '{create_air()}'"
        f" and '{strength_potion()}'"
        f" mixed with '{root_elements.create_fire()}'"
    )
