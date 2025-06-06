from dataclasses import dataclass
from typing import Dict, List

@dataclass
class CharacterEvent:
    scene_id: str
    required_points: int
    triggered: bool = False

class Bookworm:
    def __init__(self):
        self.name = "Hanako"
        self.type = "Bookworm"
        self.relationship_points = 0
        self.likes = ["literature", "quiet spaces", "tea"]
        self.dislikes = ["loud noises", "spoilers", "dog-earing pages"]
        self.events = [
            CharacterEvent("bookworm_25_event", 25),
            CharacterEvent("bookworm_50_event", 50),
            CharacterEvent("bookworm_75_event", 75),
            CharacterEvent("bookworm_100_event", 100)
        ]
    
    def get_dialogue(self) -> str:
        if self.relationship_points < 25:
            return "*Looks up briefly, then returns to book*"
        elif self.relationship_points < 50:
            return "This passage... it reminds me of something..."
        else:
            return "Would you... like to borrow one of my books?"

    def get_events(self) -> Dict:
        return {
            "bookworm_25_event": {
                "text": "Hanako is struggling to reach a book on the top shelf.",
                "choices": [
                    {"text": "Offer to get it for her", "points": 10},
                    {"text": "Recommend an ebook instead", "points": -5}
                ],
                "background": "library"
            },
            "bookworm_50_event": {
                "text": "Hanako shows you her favorite poetry collection, with notes in the margins.",
                "choices": [
                    {"text": "Read her annotations carefully", "points": 15},
                    {"text": "Skip to the next chapter", "points": -10}
                ],
                "background": "library_afternoon"
            },
            "bookworm_75_event": {
                "text": "The library is closing. Hanako hesitates before leaving.",
                "choices": [
                    {"text": "Walk her home", "points": 20},
                    {"text": "Say goodnight and leave", "points": -5}
                ],
                "background": "library_night",
                "unlocks": ["hanako_home_visit"]
            }
        }
