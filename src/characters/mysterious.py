from dataclasses import dataclass
from typing import Dict

@dataclass
class CharacterEvent:
    scene_id: str
    required_points: int
    triggered: bool = False

class Mysterious:
    def __init__(self):
        self.name = "Kuro"
        self.type = "Mysterious"
        self.relationship_points = 0
        self.likes = ["nighttime", "puzzles", "black coffee"]
        self.dislikes = ["questions", "bright lights", "small talk"]
        self.events = [
            CharacterEvent("mysterious_25_event", 25),
            CharacterEvent("mysterious_50_event", 50),
            CharacterEvent("mysterious_75_event", 75),
            CharacterEvent("mysterious_100_event", 100)
        ]
    
    def get_dialogue(self) -> str:
        if self.relationship_points < 40:
            return "..."
        elif self.relationship_points < 70:
            return "You're... persistent."
        else:
            return "The moon is beautiful tonight..."

    def get_events(self) -> Dict:
        return {
            "mysterious_25_event": {
                "text": "You catch Kuro feeding stray cats behind the school.",
                "choices": [
                    {"text": "Approach quietly", "points": 10},
                    {"text": "Bring cat food next day", "points": 15}
                ],
                "background": "school_back"
            },
            "mysterious_50_event": {
                "text": "Kuro leaves a cryptic note in your locker.",
                "choices": [
                    {"text": "Decipher it carefully", "points": 20},
                    {"text": "Ask directly about it", "points": -10}
                ],
                "background": "classroom"
            },
            "mysterious_75_event": {
                "text": "Kuro shows you a hidden rooftop garden at midnight.",
                "choices": [
                    {"text": "Admire the view silently", "points": 25},
                    {"text": "Ask who created this", "points": -15}
                ],
                "background": "rooftop_night",
                "unlocks": ["midnight_meetings"]
            }
        }
