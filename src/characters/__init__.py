from .tsundere import Tsundere
from .bookworm import Bookworm
from .athlete import Athlete
from .mysterious import Mysterious
from .childhood_friend import ChildhoodFriend

def get_character_classes():
    return {
        "Tsundere": Tsundere,
        "Bookworm": Bookworm,
        "Athlete": Athlete,
        "Mysterious": Mysterious,
        "ChildhoodFriend": ChildhoodFriend
    }
