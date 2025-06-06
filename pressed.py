import pygame
import sys
from characters import get_character_classes

class PressedGameState:
    def __init__(self):
        self.characters = {
            name: cls() for name, cls in get_character_classes().items()
        }
        self.current_scene = "start"
        
    def get_character(self, name: str):
        return self.characters.get(name)
    
    def check_events(self):
        """Check all characters for unlocked events"""
        events = []
        for char in self.characters.values():
            for event in char.events:
                if (char.relationship_points >= event.required_points and 
                    not hasattr(event, 'triggered')):
                    events.append(event.scene_id)
                    event.triggered = True
        return events

class PressedVisualNovel:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.state = PressedGameState()
        self.load_scenes()
        
    def load_scenes(self):
        """Combine character scenes with shared scenes"""
        self.scenes = {
            "start": {
                "text": "Where do you want to go?",
                "choices": [
                    {"text": "Library", "next": "bookworm_intro"},
                    {"text": "Sports Field", "next": "athlete_intro"}
                ]
            }
        }
        
        # Load character-specific scenes
        for char in self.state.characters.values():
            self.scenes.update(char.get_events())

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.render()
        
        pygame.quit()
        sys.exit()

    def render(self):
        self.screen.fill((240, 240, 250))
        # Render current scene
        scene = self.scenes.get(self.state.current_scene, {})
        font = pygame.font.SysFont('Arial', 24)
        
        if "text" in scene:
            text = font.render(scene["text"], True, (0, 0, 0))
            self.screen.blit(text, (50, 50))
        
        pygame.display.flip()

if __name__ == "__main__":
    game = PressedVisualNovel()
    game.run()
