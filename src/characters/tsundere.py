from enum import Enum
from typing import Dict, List, Set, Tuple

class CharacterEvent:
    def __init__(self, scene_id: str, required_points: int):
        self.scene_id = scene_id
        self.required_points = required_points

class Tsundere:
    def __init__(self):
        self.name = "Akira"
        self.type = "Tsundere"
        self.relationship_points = 0
        self.likes = ["honesty", "challenges"]
        self.dislikes = ["flattery", "weakness"]
        self.events = [
            CharacterEvent("tsundere_25_event", 25),
            CharacterEvent("tsundere_50_event", 50),
            CharacterEvent("tsundere_75_event", 75),
            CharacterEvent("tsundere_100_event", 100)
        ]
    
    def get_dialogue(self) -> str:
        if self.relationship_points < 20:
            return "Hmph. What do you want?"
        elif self.relationship_points < 50:
            return "Don't misunderstand! I'm not being nice!"
        else:
            return "I... I guess you're not so bad..."

    def get_events(self) -> List[Dict]:
        return {
            "tsundere_25_event": {
                "text": "Akira drops her books. Do you help?",
                "choices": [
                    {"text": "Help pick them up", "points": 10},
                    {"text": "Tease her", "points": -5}
                ]
            },
            "tsundere_50_event": {
                "text": "Akira is practicing cooking. She offers you some.",
                "choices": [
                    {"text": "Honest feedback", "points": 15},
                    {"text": "Overly praise", "points": -10}
                ]
            }
        }
