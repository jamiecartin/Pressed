import pygame
import sys
import json

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Romance Visual Novel")
clock = pygame.time.Clock()

# Game state
class GameState:
    def __init__(self):
        self.relationships = {
            "Tsundere": {"points": 0, "events_unlocked": []},
            "Bookworm": {"points": 0, "events_unlocked": []},
            "Athlete": {"points": 0, "events_unlocked": []},
            "Mysterious": {"points": 0, "events_unlocked": []},
            "ChildhoodFriend": {"points": 0, "events_unlocked": []}
        }
        self.current_scene = "start"
        self.font = pygame.font.SysFont('Arial', 24)
        
    def add_relationship_points(self, character, points):
        self.relationships[character]["points"] += points
        self.check_events(character)
        
    def check_events(self, character):
        points = self.relationships[character]["points"]
        if points >= 25 and "25_event" not in self.relationships[character]["events_unlocked"]:
            self.relationships[character]["events_unlocked"].append("25_event")
        if points >= 50 and "50_event" not in self.relationships[character]["events_unlocked"]:
            self.relationships[character]["events_unlocked"].append("50_event")
        # Add more thresholds as needed

# Character definitions
characters = {
    "Tsundere": {
        "name": "Akira",
        "description": "Cold at first but warms up over time",
        "likes": ["honesty", "challenges"],
        "dislikes": ["flattery", "weakness"]
    },
    "Bookworm": {
        "name": "Hanako",
        "description": "Shy but deeply thoughtful",
        "likes": ["literature", "quiet places"],
        "dislikes": ["loud noises", "rudeness"]
    },
    # Add other characters similarly
}

# Scenes and dialogues
scenes = {
    "start": {
        "text": "It's your first day at a new school. Where do you go first?",
        "choices": [
            {"text": "The library", "next_scene": "library", "effects": [("Bookworm", 5)]},
            {"text": "The gym", "next_scene": "gym", "effects": [("Athlete", 5)]},
            {"text": "The courtyard", "next_scene": "courtyard", "effects": [("Tsundere", 5), ("Bookworm", -2)]}
        ]
    },
    "library": {
        "text": "You find a quiet girl reading in the corner. She glances up at you.",
        "choices": [
            {"text": "Ask what she's reading", "next_scene": "library_book", "effects": [("Bookworm", 8)]},
            {"text": "Sit nearby silently", "next_scene": "library_sit", "effects": [("Bookworm", 3)]},
            {"text": "Make a joke about bookworms", "next_scene": "library_joke", "effects": [("Bookworm", -5)]}
        ]
    },
    # Add more scenes
}

# Main game loop
def main():
    game_state = GameState()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Handle choice selection here
                pass
        
        # Clear screen
        screen.fill((240, 240, 250))
        
        # Display current scene
        current = scenes[game_state.current_scene]
        text_surface = game_state.font.render(current["text"], True, (0, 0, 0))
        screen.blit(text_surface, (50, 50))
        
        # Display choices
        for i, choice in enumerate(current["choices"]):
            choice_text = game_state.font.render(f"{i+1}. {choice['text']}", True, (0, 0, 0))
            screen.blit(choice_text, (50, 150 + i * 40))
        
        # Display relationship status
        rel_text = game_state.font.render("Relationships:", True, (0, 0, 0))
        screen.blit(rel_text, (500, 50))
        
        for i, (char, data) in enumerate(game_state.relationships.items()):
            char_text = game_state.font.render(
                f"{characters[char]['name']}: {data['points']}", True, (0, 0, 0))
            screen.blit(char_text, (500, 80 + i * 30))
        
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
