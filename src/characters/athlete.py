from dataclasses import dataclass
from typing import Dict

@dataclass
class CharacterEvent:
    scene_id: str
    required_points: int
    triggered: bool = False

class Athlete:
    def __init__(self):
        self.name = "Rin"
        self.type = "Athlete"
        self.relationship_points = 0
        self.likes = ["sports", "protein shakes", "competition"]
        self.dislikes = ["laziness", "excuses", "rainy days"]
        self.events = [
            CharacterEvent("athlete_25_event", 25),
            CharacterEvent("athlete_50_event", 50),
            CharacterEvent("athlete_75_event", 75),
            CharacterEvent("athlete_100_event", 100)
        ]
    
    def get_dialogue(self) -> str:
        if self.relationship_points < 30:
            return "Hey! Spot me on the bench press!"
        elif self.relationship_points < 60:
            return "Not bad for a beginner!"
        else:
            return "You're my favorite training partner!"

    def get_events(self) -> Dict:
        return {
            "athlete_25_event": {
                "text": "Rin challenges you to a race around the track.",
                "choices": [
                    {"text": "Accept the challenge", "points": 10},
                    {"text": "Suggest a different activity", "points": 5}
                ],
                "background": "track_field"
            },
            "athlete_50_event": {
                "text": "Rin is icing a sprained ankle after practice.",
                "choices": [
                    {"text": "Offer to help her to the nurse", "points": 15},
                    {"text": "Tease her about being careless", "points": -20}
                ],
                "background": "gym"
            },
            "athlete_75_event": {
                "text": "The big tournament is coming up. Rin looks nervous.",
                "choices": [
                    {"text": "Promise to cheer her on", "points": 25},
                    {"text": "Give her a pep talk", "points": 20}
                ],
                "background": "stadium",
                "unlocks": ["tournament_arc"]
            }
        }
