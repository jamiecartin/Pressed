import pygame
import sys
import json
from typing import Dict, List, Tuple, Optional

class PressedGameState:
    """Core game state manager for the visual novel"""
    def __init__(self):
        self.relationships = {
            "Tsundere": {"points": 0, "events_unlocked": [], "flags": set()},
            "Bookworm": {"points": 0, "events_unlocked": [], "flags": set()},
            "Athlete": {"points": 0, "events_unlocked": [], "flags": set()},
            "Mysterious": {"points": 0, "events_unlocked": [], "flags": set()},
            "ChildhoodFriend": {"points": 0, "events_unlocked": [], "flags": set()}
        }
        self.current_scene = "start"
        self.visited_scenes = set()
        self.font = pygame.font.SysFont('Arial', 24)
        self.choice_rects = []  # Stores rects for clickable choices
        
    def add_relationship_points(self, character: str, points: int):
        """Modify relationship points with validation"""
        if character in self.relationships:
            self.relationships[character]["points"] = max(0, 
                min(100, self.relationships[character]["points"] + points))
            self.check_events(character)
            
    def check_events(self, character: str):
        """Check for milestone events"""
        points = self.relationships[character]["points"]
        milestones = [25, 50, 75, 100]
        
        for milestone in milestones:
            event_key = f"{milestone}_event"
            if (points >= milestone and 
                event_key not in self.relationships[character]["events_unlocked"]):
                self.relationships[character]["events_unlocked"].append(event_key)
                self.relationships[character]["flags"].add(f"reached_{milestone}")

    def save_game(self, filename: str = "save.sav"):
        """Serialize game state to file"""
        save_data = {
            "relationships": self.relationships,
            "current_scene": self.current_scene,
            "visited_scenes": list(self.visited_scenes)
        }
        with open(filename, 'w') as f:
            json.dump(save_data, f)
            
    def load_game(self, filename: str = "save.sav"):
        """Load game state from file"""
        try:
            with open(filename, 'r') as f:
                save_data = json.load(f)
            
            self.relationships = save_data["relationships"]
            self.current_scene = save_data["current_scene"]
            self.visited_scenes = set(save_data["visited_scenes"])
            return True
        except (FileNotFoundError, json.JSONDecodeError):
            return False

class PressedVisualNovel:
    """Main game engine class"""
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pressed Visual Novel")
        self.clock = pygame.time.Clock()
        self.state = PressedGameState()
        self.characters = self._load_characters()
        self.scenes = self._load_scenes()
        self.running = True
        
    def _load_characters(self) -> Dict:
        """Load character definitions"""
        return {
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
            }
            # Add other characters...
        }
    
    def _load_scenes(self) -> Dict:
        """Load game scenes and dialogues"""
        return {
            "start": {
                "text": "It's your first day at a new school. Where do you go first?",
                "choices": [
                    {"text": "The library", "next_scene": "library", 
                     "effects": [("Bookworm", 5)]},
                    {"text": "The gym", "next_scene": "gym", 
                     "effects": [("Athlete", 5)]},
                    {"text": "The courtyard", "next_scene": "courtyard", 
                     "effects": [("Tsundere", 5), ("Bookworm", -2)]}
                ]
            },
            "library": {
                "text": "You find a quiet girl reading in the corner. She glances up at you.",
                "choices": [
                    {"text": "Ask what she's reading", "next_scene": "library_book", 
                     "effects": [("Bookworm", 8)]},
                    {"text": "Sit nearby silently", "next_scene": "library_sit", 
                     "effects": [("Bookworm", 3)]},
                    {"text": "Make a joke about bookworms", "next_scene": "library_joke", 
                     "effects": [("Bookworm", -5)]}
                ]
            }
            # Add more scenes...
        }
    
    def handle_choice_selection(self, pos: Tuple[int, int]):
        """Process mouse clicks on choices"""
        for i, rect in enumerate(self.state.choice_rects):
            if rect.collidepoint(pos):
                self._execute_choice(i)
                break
                
    def _execute_choice(self, choice_index: int):
        """Apply all effects of a selected choice"""
        current = self.scenes[self.state.current_scene]
        choice = current["choices"][choice_index]
        
        # Apply relationship changes
        for char, points in choice.get("effects", []):
            self.state.add_relationship_points(char, points)
            
        # Move to next scene
        self.state.current_scene = choice["next_scene"]
        self.state.visited_scenes.add(self.state.current_scene)
        
    def render(self):
        """Draw all game elements"""
        self.screen.fill((240, 240, 250))
        self.state.choice_rects = []
        
        # Draw current scene text
        current = self.scenes[self.state.current_scene]
        text_surface = self.state.font.render(current["text"], True, (0, 0, 0))
        self.screen.blit(text_surface, (50, 50))
        
        # Draw choices
        for i, choice in enumerate(current["choices"]):
            choice_text = self.state.font.render(f"{i+1}. {choice['text']}", True, (0, 0, 0))
            text_rect = choice_text.get_rect(topleft=(50, 150 + i * 40))
            self.screen.blit(choice_text, text_rect)
            self.state.choice_rects.append(text_rect)
        
        # Draw relationship status
        rel_text = self.state.font.render("Relationships:", True, (0, 0, 0))
        self.screen.blit(rel_text, (500, 50))
        
        for i, (char, data) in enumerate(self.state.relationships.items()):
            char_text = self.state.font.render(
                f"{self.characters[char]['name']}: {data['points']}", True, (0, 0, 0))
            self.screen.blit(char_text, (500, 80 + i * 30))
        
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left click
                        self.handle_choice_selection(event.pos)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    elif event.key == pygame.K_s:
                        self.state.save_game()
                    elif event.key == pygame.K_l:
                        self.state.load_game()
            
            self.render()
            self.clock.tick(30)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = PressedVisualNovel()
    game.run()
