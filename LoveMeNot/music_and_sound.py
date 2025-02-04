import pygame

pygame.mixer.init()

# Music
main_menu_music = pygame.mixer.Sound("assets/Music/background_music/main_menu.mp3") # https://www.youtube.com/watch?v=mnA2CRs7T9Q
in_game_music = pygame.mixer.Sound("assets/Music/background_music/BGM.mp3") # https://www.youtube.com/watch?v=3V-pYCGx0C4
end_game_music = pygame.mixer.Sound("assets/Music/background_music/EGM.mp3") # https://www.youtube.com/watch?v=W1i4mTyidOc
celebration = pygame.mixer.Sound("assets/Fonts/Celebration.mp3") # https://www.youtube.com/watch?v=3GwjfUFyY6M

# Sound Effects
letter_sound = pygame.mixer.Sound("assets/Music/sound_effects/typing_sound_effect.wav") # https://www.youtube.com/watch?v=FP_TCP73h2I
hit = pygame.mixer.Sound("assets/Music/sound_effects/hit.wav") # https://www.youtube.com/watch?v=4bJI-e28kFg
victory = pygame.mixer.Sound("assets/Music/sound_effects/victory.wav") # https://www.youtube.com/watch?v=1Qo7KTtO4MY

# Button Sound Effects
button_click = pygame.mixer.Sound("assets/Music/sound_effects/button_select_sound_effect.wav") # https://www.youtube.com/watch?v=YNSbL-Cek1c
button_hover = pygame.mixer.Sound("assets/Music/sound_effects/button_hover_sound_effect.wav") # https://www.youtube.com/watch?v=_vjTeR9iw8o