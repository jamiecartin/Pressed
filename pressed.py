import pygame
import sys
import os
from typing import Dict, List, Optional
from characters import get_character_classes

class SpriteManager:
    def __init__(self):
        self.sprites = {}
        
    def load_sprites(self, character_name: str, expressions: List[str]):
        """Load all sprites for a character"""
        self.sprites[character_name] = {}
        for expr in expressions:
            path = f"assets/sprites/{character_name.lower()}_{expr}.png"
            try:
                self.sprites[character_name][expr] = pygame.image.load(path).convert_alpha()
            except:
                # Fallback if sprite missing
                surf = pygame.Surface((300, 600), pygame.SRCALPHA)
                surf.fill((255, 0, 255, 128))  # Visible placeholder
                self.sprites[character_name][expr] = surf

class PressedGameState:
    def __init__(self):
        self.characters = {name: cls() for name, cls in get_character_classes().items()}
        self.current_scene = "start"
        self.active_event: Optional[Dict] = None
        
    def check_events(self):
        """Check all characters for new events"""
        new_events = []
        for char in self.characters.values():
            for event in char.events:
                if (char.relationship_points >= event.required_points 
                    and not event.triggered):
                    event.triggered = True
                    new_events.append(char.get_events()[event.scene_id])
        return new_events

class PressedVisualNovel:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.sprite_manager = SpriteManager()
        self.state = PressedGameState()
        self.scenes = self._load_all_scenes()
        
        # Load character sprites
        self._init_sprites()
        
    def _init_sprites(self):
        """Load sprites for all characters"""
        expressions = ["neutral", "happy", "angry", "blush"]
        for char_name in self.state.characters.keys():
            self.sprite_manager.load_sprites(char_name, expressions)

    def _load_all_scenes(self) -> Dict:
        """Combine scenes from all characters"""
        scenes = {
            "start": {
                "text": "Welcome to your first day!",
                "background": "school_gate.png",
                "choices": [
                    {"text": "Go to class", "next": "homeroom"},
                    {"text": "Explore campus", "next": "explore"}
                ]
            }
        }
        
        # Merge all character scenes
        for character in self.state.characters.values():
            scenes.update(character.get_events())
            
        return scenes

    def _render_character(self, character_name: str, expression: str = "neutral"):
        """Draw character sprite with expression"""
        sprite = self.sprite_manager.sprites[character_name][expression]
        # Position at right side of screen
        self.screen.blit(sprite, (800, 100))

    def _handle_event_trigger(self):
        """Process newly triggered events"""
        new_events = self.state.check_events()
        if new_events:
            self.state.active_event = new_events[0]  # Take first available event
            # Pause normal progression for event scene

    def run(self):
        while True:
            self._handle_event_trigger()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            # Clear screen
            self.screen.fill((0, 0, 0))
            
            # Draw background if available
            current_scene = self.scenes.get(self.state.current_scene, {})
            if "background" in current_scene:
                bg = pygame.image.load(f"assets/bg/{current_scene['background']}")
                self.screen.blit(bg, (0, 0))
            
            # Draw active character
            if self.state.active_event:
                char_type = self.state.active_event.get("character")
                if char_type:
                    self._render_character(char_type, "neutral")
            
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = PressedVisualNovel()
    game.run()
