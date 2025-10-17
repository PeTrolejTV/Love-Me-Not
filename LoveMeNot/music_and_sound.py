import pygame
import sys
import os

pygame.mixer.init()

def resource_path(relative_path):
    """Return the correct path to assets, works in PyInstaller EXE"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        # Running in normal Python
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

# Music
main_menu_music = pygame.mixer.Sound(resource_path("assets/Music/background_music/main_menu.mp3"))
in_game_music = pygame.mixer.Sound(resource_path("assets/Music/background_music/BGM.mp3"))
end_game_music = pygame.mixer.Sound(resource_path("assets/Music/background_music/EGM.mp3"))
celebration = pygame.mixer.Sound(resource_path("assets/Fonts/Celebration.mp3"))

# Sound Effects
letter_sound = pygame.mixer.Sound(resource_path("assets/Music/sound_effects/typing_sound_effect.wav"))
hit = pygame.mixer.Sound(resource_path("assets/Music/sound_effects/hit.wav"))
victory = pygame.mixer.Sound(resource_path("assets/Music/sound_effects/victory.wav"))

# Button Sound Effects
button_click = pygame.mixer.Sound(resource_path("assets/Music/sound_effects/button_select_sound_effect.wav"))
button_hover = pygame.mixer.Sound(resource_path("assets/Music/sound_effects/button_hover_sound_effect.wav"))
