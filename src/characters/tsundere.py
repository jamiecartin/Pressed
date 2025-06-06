class Tsundere:
    def __init__(self):
        self.name = "Akira"
        self.description = "Cold at first but warms up over time"
        self.stats = {
            "likes": ["honesty", "challenges"],
            "dislikes": ["flattery", "weakness"]
        }
    
    def get_dialogue(self, relationship_level):
        if relationship_level < 20:
            return "Hmph. What do you want?"
        elif relationship_level < 50:
            return "Don't misunderstand! I'm just being nice."
        else:
            return "I... I might enjoy your company sometimes."
