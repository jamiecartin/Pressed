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
                    {"text": "Explore campus", "next":
