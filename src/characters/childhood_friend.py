from dataclasses import dataclass
from typing import Dict

@dataclass
class CharacterEvent:
    scene_id: str
    required_points: int
    triggered: bool = False

class ChildhoodFriend:
    def __init__(self):
        self.name = "Sora"
        self.type = "ChildhoodFriend"
        self.relationship_points = 0
        self.likes = ["nostalgia", "honesty", "shared memories"]
        self.dislikes = ["lies", "forgetting promises", "change"]
        self.events = [
            CharacterEvent("childhood_25_event", 25),
            CharacterEvent("childhood_50_event", 50),
            CharacterEvent("childhood_75_event", 75),
            CharacterEvent("childhood_100_event", 100)
        ]
    
    def get_dialogue(self) -> str:
        if self.relationship_points < 35:
            return "Hey, remember when we... oh never mind."
        elif self.relationship_points < 65:
            return "Some things never change, huh?"
        else:
            return "I've missed this... missed us..."

    def get_events(self) -> Dict:
        return {
            "childhood_25_event": {
                "text": "Sora finds an old photo of you two as kids.",
                "choices": [
                    {"text": "Reminisce together", "points": 15},
                    {"text": "Joke about childhood", "points": 5}
                ],
                "background": "park_day"
            },
            "childhood_50_event": {
                "text": "Sora suggests visiting your old elementary school.",
                "choices": [
                    {"text": "Go together after class", "points": 20},
                    {"text": "Say you're busy", "points": -10}
                ],
                "background": "school_gates"
            },
            "childhood_75_event": {
                "text": "At your secret childhood spot, Sora seems emotional.",
                "choices": [
                    {"text": "Hold their hand", "points": 30},
                    {"text": "Talk about the past", "points": 20}
                ],
                "background": "treehouse",
                "unlocks": ["confession_scene"]
            }
        }
