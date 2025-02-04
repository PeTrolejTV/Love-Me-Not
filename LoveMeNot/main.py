import sys

from button import *
from music_and_sound import *

# Initialize pygame
pygame.init()
pygame.display.set_caption("Love Me Not")

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GRAY = (150, 150, 150)
FPS = 60
SCORE = 0
target_score = 0

# Bools
in_main_menu = False
in_game = False
in_game_menu = False
in_options = False
in_end_game = False
win = False

# Initial volumes
bg_music_volume = 0.5
effects_volume = 0.5

# Global variables
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
clock = pygame.time.Clock()

# Assets
menu_background = pygame.image.load("dist/assets/Art/backgroundLMN.png")
game_background = pygame.image.load("dist/assets/Art/gradient.png")

# Character
ch_1 = pygame.image.load("dist/assets/Character_expressions/char_talk.png")
ch_2 = pygame.image.load("dist/assets/Character_expressions/char_talk2.png")
ch_3 = pygame.image.load("dist/assets/Character_expressions/char_talk3.png")
ch_knife = pygame.image.load("dist/assets/Character_expressions/char_knife.png")
ch_mad_knife = pygame.image.load("dist/assets/Character_expressions/char_mad_knife.png")
ch_sad = pygame.image.load("dist/assets/Character_expressions/char_sad.png")
ch_happy = pygame.image.load("dist/assets/Character_expressions/char_happy.png")
ch_fc_plm = pygame.image.load("dist/assets/Character_expressions/char_face_palm.png")

ch_active = ch_1

# Fonts
TITLE_FONT = pygame.font.Font("dist/assets/Fonts/BeautifulPeople.ttf", SCREEN_WIDTH // 10)
BUTTON_FONT = pygame.font.Font("dist/assets/Fonts/Comfort-Bold.ttf", SCREEN_WIDTH // 30)
OPTIONS_BUTTON_FONT = pygame.font.Font("dist/assets/Fonts/Comfort-Bold.ttf", SCREEN_WIDTH // 69)
CH_TEXT_FONT = pygame.font.Font("dist/assets/Fonts/Comfort-Bold.ttf", SCREEN_HEIGHT // 24)

# Icon
icon = pygame.image.load("dist/assets/Art/icon.png")
pygame.display.set_icon(icon)

def toggle_fullscreen():
    """Toggles fullscreen mode."""
    global screen, SCREEN_WIDTH, SCREEN_HEIGHT

    is_fullscreen = screen.get_flags() & pygame.FULLSCREEN

    def update_fonts():
        global TITLE_FONT, BUTTON_FONT, OPTIONS_BUTTON_FONT, CH_TEXT_FONT

        TITLE_FONT = pygame.font.Font("dist/assets/Fonts/BeautifulPeople.ttf", SCREEN_WIDTH // 10)
        BUTTON_FONT = pygame.font.Font("dist/assets/Fonts/Comfort-Bold.ttf", SCREEN_WIDTH // 30)
        OPTIONS_BUTTON_FONT = pygame.font.Font("dist/assets/Fonts/Comfort-Bold.ttf", SCREEN_WIDTH // 69)
        CH_TEXT_FONT = pygame.font.Font("dist/assets/Fonts/Comfort-Bold.ttf", SCREEN_HEIGHT // 24)

    if is_fullscreen:
        screen = pygame.display.set_mode((800, 600))
    else:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
    update_fonts()

def update_cursor(buttons):
    """Checks if any button is hovered and updates the cursor."""
    if buttons is None:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    elif any(button.hovered for button in buttons):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

def create_buttons(button_specs):
    """Creates buttons dynamically based on the provided specifications."""
    button_width = SCREEN_WIDTH // 4
    button_height = SCREEN_HEIGHT // 12
    spacing = SCREEN_HEIGHT // 8

    # Ensure spacing is adequate to prevent overlap
    if spacing <= button_height:
        spacing = button_height + 10  # Add a buffer to spacing

    buttons = []
    for i, (start_y, text, action) in enumerate(button_specs):

        # If button vertical position left empty pick default
        if start_y is None:
            start_y = SCREEN_HEIGHT // 2.4

        y_position = start_y + i * spacing
        button = Button(
            SCREEN_WIDTH // 2 - button_width // 2,
            y_position,
            button_width,
            button_height,
            text,
            BUTTON_FONT,
            WHITE,
            DARK_GRAY,
            action
        )
        buttons.append(button)
    return buttons

def create_options_buttons(button_specs):
    """Creates options buttons dynamically, positioned next to each other above the text box."""
    options_button_width = SCREEN_WIDTH // 3
    options_button_height = SCREEN_HEIGHT // 14

    spacing = SCREEN_WIDTH // 4.2  # Space between buttons
    start_y = SCREEN_HEIGHT - (SCREEN_HEIGHT // 4) - (options_button_height * 1.5)  # Above the text box
    start_x = (SCREEN_WIDTH - ((options_button_width + spacing) * len(button_specs) - spacing)) // 2

    buttons = []
    for i, (text, main_action, score_action) in enumerate(button_specs):
        x_position = start_x + i * (options_button_width + spacing)

        def combined_action(main=main_action, score=score_action):
            # Main first so it does not affect the losing logic
            if main:
                main()

            if score:
                score()

        button = Button(
            x_position,
            start_y,
            options_button_width,
            options_button_height,
            text,
            OPTIONS_BUTTON_FONT,
            WHITE,
            DARK_GRAY,
            combined_action
        )
        buttons.append(button)
    return buttons

def draw_text(text, font, color, surface, center_x, center_y):
    """Draws centered text at the specified position."""
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(center_x, center_y))
    surface.blit(text_surface, text_rect)

def main_menu_reset():
    """Reset main menu with the music"""
    main_menu_music.play(-1)
    main_menu()

def main_menu():
    """Main menu logic."""
    global SCORE, in_main_menu, in_game_menu, in_options, target_score, in_game, in_end_game, win
    SCORE = 50
    target_score = SCORE

    # Reset win and stop win music
    if win:
        win = False
        celebration.stop()

    # Stop in game and end game music if going back from the in-game menu or the end-game menu
    else:
        in_game_music.stop()
        end_game_music.stop()

    # Prevent playing the music again if going back from options or using F11
    if not in_options and in_main_menu:
        main_menu_music.play(-1)

    buttons = create_buttons([
        (None, "Start Game", start_game),
        (None, "Options", options),
        (None, "Quit", quit_game),
    ])

    # Displays background image and draws the title
    screen.blit(pygame.transform.scale(menu_background, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
    draw_text("Love Me Not", TITLE_FONT, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 5)

    in_main_menu = True
    in_game_menu = False
    in_options = False
    in_game = False
    in_end_game = False

    while in_main_menu:
        update_cursor(buttons)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                toggle_fullscreen()
                in_main_menu = False
                main_menu()

            for button in buttons:
                button.handle_event(event)
                button.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

def start_game():
    """Starts the game and handles the main game logic."""
    global in_game, in_game_menu, in_main_menu, SCORE, target_score, ch_active

    # Stops main menu music and starts in-game music
    main_menu_music.stop()
    in_game_music.play(-1)

    # Typing-related variables
    typing_speed = 30  # Letters per second
    max_lines = 4  # Max number of lines that fit in the text box

    # Bar settings
    SCORE_MAX = 100
    SCORE_MIN = 0

    # Bar variables
    bar_width = SCREEN_WIDTH // 20
    bar_margin = 10
    bar_x = SCREEN_WIDTH - bar_width - bar_margin
    bar_y = bar_margin
    bar_height = SCREEN_HEIGHT - bar_margin * 2

    def check_game_over():
        """Ends the game if SCORE is out of bounds."""
        global in_game, target_score
        nonlocal typing_speed

        # If girl angry
        if target_score <= SCORE_MIN:
            in_game_music.stop()
            typing_speed = 10
            set_next_text(100)

        # If girl too happy
        elif target_score >= SCORE_MAX:
            in_game_music.stop()
            typing_speed = 10
            set_next_text(105)

    # Change the score
    def increment_score(points):
        """Updates the global score."""
        global SCORE, target_score
        target_score = max(SCORE_MIN, min(SCORE_MAX, SCORE + points))
        check_game_over()

    def draw_score_bar():
        """Draws the score bar on the side of the screen."""
        # Calculate the filled portion of the bar based on SCORE
        filled_height = int(bar_height * (SCORE / SCORE_MAX))
        filled_y = bar_y + (bar_height - filled_height)

        # Draw the bar background (empty portion)
        pygame.draw.rect(screen, (50, 50, 50), (bar_x, bar_y, bar_width, bar_height))

        # Determine the bar color based on the score ranges
        if SCORE < 25:
            bar_color = (255, 0, 0)  # Red
        elif 25 <= SCORE <= 40:
            bar_color = (255, 165, 0)  # Orange
        elif 40 < SCORE <= 60:
            bar_color = (0, 255, 0)  # Green
        elif 60 < SCORE <= 75:
            bar_color = (255, 165, 0)  # Orange
        else:
            bar_color = (255, 0, 0)  # Red

        pygame.draw.rect(screen, bar_color, (bar_x, filled_y, bar_width, filled_height))

    def set_next_text(index):
        """Sets the next text and updates options buttons."""
        nonlocal current_text_index, show_buttons, buttons, current_story_text, typing_index, typing_finished

        # Ensure the index is within bounds
        if index not in storyline:
            return

        current_text_index = index

        # Reset typing variables
        current_story_entry = storyline[current_text_index]

        # Display the bars status to the player if needed
        if "{score}" in current_story_entry["text"]:  # Dynamically update SCORE in text
            current_story_text = current_story_entry["text"].format(score=SCORE)
        else:
            current_story_text = current_story_entry["text"]

        typing_index = 0
        typing_finished = False
        buttons = create_options_buttons(current_story_entry.get("options", []))

        # Automatically proceed if there are no options
        show_buttons = bool(current_story_entry.get("options"))
        if not show_buttons and typing_finished:
            # Automatically proceed to the next index if available
            next_index_is = current_text_index + 1
            if next_index_is in storyline:
                set_next_text(next_index_is)

    def wrap_text(font, text, max_width):
        """Wraps text into multiple lines to fit the dialog box."""
        words = text.split()
        lines = []
        current_line = []

        for word in words:
            current_line.append(word)
            line_width, _ = font.size(' '.join(current_line))

            if line_width > max_width:
                current_line.pop()
                lines.append(' '.join(current_line))
                current_line = [word]

        if current_line:
            lines.append(' '.join(current_line))

        # Replace text with "..." if it exceeds max lines
        if len(lines) > max_lines:
            lines = lines[:max_lines]
            lines[-1] = lines[-1][:-3] + "..."

        return lines

    def draw_text_box(text, letter_index):
        """Draws the text box and displays the current text with proper line breaks."""


        # Create the semi-transparent text box background
        dialog_overlay = pygame.Surface((SCREEN_WIDTH - text_box_margin * 2, text_box_height), pygame.SRCALPHA)
        dialog_overlay.fill((0, 0, 0, 180))
        screen.blit(dialog_overlay, (text_box_margin, SCREEN_HEIGHT - text_box_height - text_box_margin))

        # Check if text starts with "Narrator:" and contains a newline.
        if text.startswith("Narrator:") and "\n" in text:
            # Split into the narrator's part and the remainder.
            narrator_line, remainder_nar = text.split("\n", 1)
            # The narrator_line is shown instantly.
            # The remainder is typed letter-by-letter.
            displayed_text = narrator_line + "\n" + remainder_nar[:letter_index]

        elif text.startswith("Unknown girl:") and "\n" in text:
            narrator_line, remainder_girl = text.split("\n", 1)
            displayed_text = narrator_line + "\n" + remainder_girl[:letter_index]

        else:
            displayed_text = text[:letter_index]

        # Split text manually by \n and process each line separately
        split_text = displayed_text.split("\n")
        wrapped_lines = []

        for line in split_text:
            wrapped_lines.extend(wrap_text(CH_TEXT_FONT, line, SCREEN_WIDTH - text_box_margin * 4))

        y_offset = SCREEN_HEIGHT - text_box_height - text_box_margin + 20

        for line in wrapped_lines:
            text_surface = CH_TEXT_FONT.render(line, True, (255, 255, 255))
            screen.blit(text_surface, (text_box_margin * 2, y_offset))
            y_offset += text_surface.get_height() + 5  # Spacing between lines

    # Text box dimensions and character positioning
    text_box_height = SCREEN_HEIGHT // 4
    text_box_margin = 10
    update_cursor(None)

    char_width, char_height = SCREEN_WIDTH // 4, SCREEN_HEIGHT // 1.5
    char_x = (SCREEN_WIDTH - char_width) // 2
    char_y = SCREEN_HEIGHT - char_height - text_box_height - text_box_margin

    current_text_index = 0
    show_buttons = False
    buttons = []

    # Typing variables
    current_story_text = ""
    typing_index = 0
    typing_finished = False
    typing_timer = pygame.time.get_ticks()

    storyline = {
        0: {
            "text": "Narrator:\nYou notice a girl staring at you from across the room.",
            "options": [],
        },
        1: {
            "text": "Narrator:\nHer eyes glisten with an eerie intensity.",
            "options": [],
        },
        2: {
            "text": "Narrator:\nShe steps closer.",
            "options": [],
        },
        3: {
            "text": "Unknown girl:\nHey...",
            "options": [],
        },
        4: {
            "text": "Unknown girl:\nI've been watching you for a while now.",
            "options": [
                ("Uh, thanks?", lambda: set_next_text(5), lambda: increment_score(-10)),
                ("Oh? That’s… interesting.", lambda: set_next_text(10), lambda: increment_score(10)),
            ],
        },
        5: {
            "text": "Narrator:\nShe frowns slightly but keeps her smile.",
            "options": [],
        },
        6: {
            "text": "Unknown girl:\nYou don’t seem very excited to see me…",
            "options": [],
        },
        7: {
            "text": "Unknown girl:\nThat’s okay.",
            "options": [],
        },
        8: {
            "text": "Unknown girl:\nI’ll just have to show you how special I am.",
            "options": [],
        },
        9: {
            "text": "",
            "options": [],
        },
        10: {
            "text": "Narrator:\nHer cheeks turn pink.",
            "options": [],
        },
        11: {
            "text": "Unknown girl:\nYou think so?",
            "options": [],
        },
        12: {
            "text": "Unknown girl:\nNo one ever really notices me...",
            "options": [],
        },
        13: {
            "text": "Unknown girl:\nBut you…",
            "options": [],
        },
        14: {
            "text": "Unknown girl:\nYou’re different.",
            "options": [],
        },
        15: {
            "text": "Unknown girl:\nTell me, do you believe in fate?",
            "options": [
                ("I don’t know… maybe?", lambda: set_next_text(16), lambda: increment_score(5)),
                ("Not really.", lambda: set_next_text(20), lambda: increment_score(-5)),
            ],
        },
        16: {
            "text": "Unknown girl:\nThat’s a good answer~",
            "options": [],
        },
        17: {
            "text": "Narrator:\nShe giggles softly.",
            "options": [],
        },
        18: {
            "text": "Unknown girl:\nBecause I believe fate brought us together.",
            "options": [],
        },
        19: {
            "text": "",
            "options": [],
        },
        20: {
            "text": "Unknown girl:\nOh…",
            "options": [],
        },
        21: {
            "text": "Narrator:\nHer smile falters for a second before quickly returning.",
            "options": [],
        },
        22: {
            "text": "Unknown girl:\nI guess I’ll have to make you believe…",
            "options": [],
        },
        23: {
            "text": "Narrator:\nShe suddenly grabs your hand.",
            "options": [],
        },
        24: {
            "text": "Narrator:\nHer grip is surprisingly strong.",
            "options": [],
        },
        25: {
            "text": "Unknown girl:\nTell me, do you have someone you like?",
            "options": [
                ("No, not really.", lambda: set_next_text(26), lambda: increment_score(15)),
                ("That’s personal.", lambda: set_next_text(30), lambda: increment_score(-15)),
            ],
        },
        26: {
            "text": "Narrator:\nHer face lights up.",
            "options": [],
        },
        27: {
            "text": "Unknown girl:\nReally?",
            "options": [],
        },
        28: {
            "text": "Unknown girl:\nThat means I still have a chance…",
            "options": [],
        },
        29: {
            "text": "",
            "options": [],
        },
        30: {
            "text": "Narrator:\nHer grip tightens just a bit.",
            "options": [],
        },
        31: {
            "text": "Unknown girl:\nPersonal?",
            "options": [],
        },
        32: {
            "text": "Unknown girl:\nHmmm…",
            "options": [],
        },
        33: {
            "text": "Unknown girl:\nI don’t like secrets between us…",
            "options": [],
        },
        34: {
            "text": "Narrator:\nShe takes a step closer.",
            "options": [],
        },
        35: {
            "text": "Unknown girl:\nWhat kind of girls do you like?",
            "options": [
                ("Kind and sweet.", lambda: set_next_text(36), lambda: increment_score(5)),
                ("Why do you care?", lambda: set_next_text(40), lambda: increment_score(-30)),
            ],
        },
        36: {
            "text": "Unknown girl:\nKind and sweet, huh…?",
            "options": [],
        },
        37: {
            "text": "Unknown girl:\nI can be that!",
            "options": [],
        },
        38: {
            "text": "Unknown girl:\nI can be exactly what you need~",
            "options": [],
        },
        39: {
            "text": "",
            "options": [],
        },
        40: {
            "text": "Narrator:\nHer expression darkens for a second before she laughs softly.",
            "options": [],
        },
        41: {
            "text": "Unknown girl:\nWhatever.",
            "options": [],
        },
        42: {
            "text": "Unknown girl:\nI’m just being curious.",
            "options": [],
        },
        43: {
            "text": "Unknown girl:\nGetting to know each other a bit, you know.",
            "options": [],
        },
        44: {
            "text": "Narrator:\nHer eyes flicker with an intense glow as she leans in, closing the distance between you.",
            "options": [],
        },
        45: {
            "text": "Unknown girl:\nYou think I'm not interested, don't you?",
            "options": [
                ("Are you?", lambda: set_next_text(46), lambda: increment_score(5)),
                ("Please, don't get too close.", lambda: set_next_text(47), lambda: increment_score(-10)),
            ],
        },
        46: {
            "text": "Narrator:\nHer smile twists into something both alluring and unnerving.",
            "options": [],
        },
        47: {
            "text": "Unknown girl:\nI know exactly what you desire... and what you fear.",
            "options": [
                ("What is it?", lambda: set_next_text(48), lambda: increment_score(5)),
                ("I don't want to know.", lambda: set_next_text(49), lambda: increment_score(-5)),
            ],
        },
        48: {
            "text": "Narrator:\nA chill runs down your spine as her tone shifts subtly, hinting at hidden depths.",
            "options": [],
        },
        49: {
            "text": "Unknown girl:\nI can be gentle... or I can be dangerously fierce.",
            "options": [
                ("Dangerous can be exciting.", lambda: set_next_text(50), lambda: increment_score(10)),
                ("I prefer something softer.", lambda: set_next_text(51), lambda: increment_score(-10)),
            ],
        },
        50: {
            "text": "Narrator:\nHer words linger like a promise—both inviting and threatening.",
            "options": [],
        },
        51: {
            "text": "Unknown girl:\nDon't you ever wonder why I care so much?",
            "options": [
                ("Maybe I'm flattered.", lambda: set_next_text(52), lambda: increment_score(5)),
                ("It's a bit creepy.", lambda: set_next_text(54), lambda: increment_score(-15)),
            ],
        },
        52: {
            "text": "Narrator:\nThe air thickens with an unsettling mix of desire and dread.",
            "options": [],
        },
        53: {
            "text": "Unknown girl:\nPerhaps it's because I see something truly special in you.",
            "options": [],
        },
        54: {
            "text": "Narrator:\nHer voice softens, yet the intensity in her eyes remains unyielding.",
            "options": [],
        },
        55: {
            "text": "Unknown girl:\nI could protect you... or I could shatter everything around you.",
            "options": [
                ("Protect me, please.", lambda: set_next_text(56), lambda: increment_score(40)),
                ("As if you could.", lambda: set_next_text(57), lambda: increment_score(-25)),
            ],
        },
        56: {
            "text": "Narrator:\nHer piercing gaze forces you to confront your hidden desires.",
            "options": [],
        },
        57: {
            "text": "Unknown girl:\nWhat if I told you that I already know all your secrets?",
            "options": [
                ("I don't believe you.", lambda: set_next_text(58), lambda: increment_score(-10)),
                ("I have nothing to hide.", lambda: set_next_text(59), lambda: increment_score(5)),
            ],
        },
        58: {
            "text": "Narrator:\nThe room seems to close in as her obsessive aura becomes palpable.",
            "options": [],
        },
        59: {
            "text": "Unknown girl:\nI see the way you glance at me, even when you try to hide it.",
            "options": [],
        },
        60: {
            "text": "Narrator:\nEach word she utters sends a shiver down your spine.",
            "options": [],
        },
        61: {
            "text": "Unknown girl:\nI want to understand every hidden part of you.",
            "options": [
                ("Maybe that's too intimate.", lambda: set_next_text(62), lambda: increment_score(-5)),
                ("I enjoy the mystery.", lambda: set_next_text(63), lambda: increment_score(5)),
            ],
        },
        62: {
            "text": "Narrator:\nHer nearness is overwhelming, nearly suffocating in its intensity.",
            "options": [],
        },
        63: {
            "text": "Unknown girl:\nTell me, have you ever felt truly seen?",
            "options": [
                ("Yes, in moments like these.", lambda: set_next_text(64), lambda: increment_score(25)),
                ("No, it's frightening to be truly seen.", lambda: set_next_text(66), lambda: increment_score(-15)),
            ],
        },
        64: {
            "text": "Narrator:\nHer whisper carries secrets and promises, heavy with implication.",
            "options": [],
        },
        65: {
            "text": "Unknown girl:\nPerhaps I could be the one to see you completely.",
            "options": [],
        },
        66: {
            "text": "Narrator:\nA long pause fills the space, laden with unspoken threat.",
            "options": [],
        },
        67: {
            "text": "Unknown girl:\nBut if you dare push me away...",
            "options": [
                ("I won't push you away.", lambda: set_next_text(68), lambda: increment_score(25)),
                ("I need my space.", lambda: set_next_text(69), lambda: increment_score(-20)),
            ],
        },
        68: {
            "text": "Narrator:\nHer tone darkens, the warning unmistakable.",
            "options": [],
        },
        69: {
            "text": "Unknown girl:\nI promise, I won't ever let you go.",
            "options": [
                ("That's...", lambda: set_next_text(70), lambda: increment_score(0)),
                ("People say that, but they always leave.", lambda: set_next_text(72), lambda: increment_score(0)),
            ],
        },
        70: {
            "text": "Narrator:\nHer words cling to you, suffocating yet strangely tender.",
            "options": [],
        },
        71: {
            "text": "Unknown girl:\nYou understand, don't you? Some things are meant to last forever.",
            "options": [
                ("Maybe you're right.", lambda: set_next_text(73), lambda: increment_score(20)),
                ("Nothing lasts forever.", lambda: set_next_text(74), lambda: increment_score(-5)),
            ],
        },
        72: {
            "text": "Unknown girl:\nThen maybe you need someone who never will.",
            "options": [
                ("That’s an impossible promise.", lambda: set_next_text(75), lambda: increment_score(-10)),
                ("Do you really believe that?", lambda: set_next_text(76), lambda: increment_score(0)),
            ],
        },
        73: {
            "text": "Narrator:\nA small, satisfied smile plays on her lips.",
            "options": [],
        },
        74: {
            "text": "Unknown girl:\nIf you say that enough times, it might come true. But I don't believe it.",
            "options": [
                ("Belief doesn’t make something real.", lambda: set_next_text(77), lambda: increment_score(-5)),
                ("Maybe I don’t want it to be true.", lambda: set_next_text(78), lambda: increment_score(5)),
            ],
        },
        75: {
            "text": "Narrator:\nThe air around you thickens, tension settling like a storm about to break.",
            "options": [],
        },
        76: {
            "text": "Unknown girl:\nMore than anything.",
            "options": [
                ("That’s... intense.", lambda: set_next_text(79), lambda: increment_score(-5)),
                ("I admire your certainty.", lambda: set_next_text(80), lambda: increment_score(15)),
            ],
        },
        77: {
            "text": "Unknown girl:\nNeither does denial.",
            "options": [
                ("I’m not denying anything.", lambda: set_next_text(81), lambda: increment_score(0)),
                ("Maybe we’re both just pretending.", lambda: set_next_text(82), lambda: increment_score(10)),
            ],
        },
        78: {
            "text": "Narrator:\nA flicker of something—hope?—crosses her face.",
            "options": [],
        },
        79: {
            "text": "Unknown girl:\nIntensity is just another word for devotion.",
            "options": [
                ("And obsession?", lambda: set_next_text(83), lambda: increment_score(-15)),
                ("Then you must be very devoted.", lambda: set_next_text(84), lambda: increment_score(20)),
            ],
        },
        80: {
            "text": "Narrator:\nFor the first time, her expression softens.",
            "options": [],
        },
        81: {
            "text": "Unknown girl:\nThen why do you sound so uncertain?",
            "options": [
                ("Because certainty is dangerous.", lambda: set_next_text(85), lambda: increment_score(-5)),
                ("Maybe I need more time to understand.", lambda: set_next_text(86), lambda: increment_score(5)),
            ],
        },
        82: {
            "text": "Narrator:\nSilence stretches between you, heavy with meaning.",
            "options": [],
        },
        83: {
            "text": "Unknown girl:\nObsession is just love that refuses to die.",
            "options": [
                ("That’s not true love.", lambda: set_next_text(87), lambda: increment_score(-25)),
                ("I suppose it depends on the person.", lambda: set_next_text(88), lambda: increment_score(15)),
            ],
        },
        84: {
            "text": "Narrator:\nHer fingers tighten around the fabric of her sleeve.",
            "options": [],
        },
        85: {
            "text": "Unknown girl:\nSo is hesitation.",
            "options": [
                ("I just don’t want to get hurt.", lambda: set_next_text(89), lambda: increment_score(-25)),
                ("I just don’t want to hurt you.", lambda: set_next_text(90), lambda: increment_score(25)),
            ],
        },
        86: {
            "text": "Narrator:\nA fleeting moment of vulnerability flickers in her eyes.",
            "options": [],
        },
        87: {
            "text": "Unknown girl:\nThen tell me—what is true love to you?",
            "options": [
                ("Love is freedom.", lambda: set_next_text(91), lambda: increment_score(-15)),
                ("Love is commitment.", lambda: set_next_text(92), lambda: increment_score(25)),
            ],
        },
        88: {
            "text": "Narrator:\nShe tilts her head, considering your words carefully.",
            "options": [],
        },
        89: {
            "text": "Unknown girl:\nPain is inevitable. Love is what makes it worthwhile.",
            "options": [
                ("That sounds almost poetic.", lambda: set_next_text(93), lambda: increment_score(5)),
                ("That sounds dangerous.", lambda: set_next_text(94), lambda: increment_score(-10)),
            ],
        },
        90: {
            "text": "Narrator:\nSomething unreadable flashes across her face.",
            "options": [],
        },
        91: {
            "text": "Unknown girl:\nFreedom is just another word for loneliness.",
            "options": [
                ("Only if you’re alone.", lambda: set_next_text(95), lambda: increment_score(-15)),
                ("Maybe love should be a balance.", lambda: set_next_text(96), lambda: increment_score(5)),
            ],
        },
        92: {
            "text": "Narrator:\nHer expression darkens, as if she’s weighing the weight of your words.",
            "options": [],
        },
        93: {
            "text": "Unknown girl:\nMaybe you do understand, after all.",
            "options": [],
        },
        94: {
            "text": "Unknown girl:\nEverything worthwhile is.",
            "options": [],
        },
        95: {
            "text": "Narrator:\nA ghost of a smile tugs at her lips.",
            "options": [],
        },
        96: {
            "text": "Unknown girl:\nBalance is difficult when your heart is already full.",
            "options": [
                ("Maybe you should share the weight.", lambda: set_next_text(97), lambda: increment_score(25)),
                ("That sounds exhausting.", lambda: set_next_text(98), lambda: increment_score(-25)),
            ],
        },
        97: {
            "text": "Narrator:\nFor the first time, she seems to consider something beyond herself.",
            "options": [],
        },
        98: {
            "text": "Unknown girl:\nLove is meant to be all-consuming.",
            "options": [
                ("Not if it consumes everything else.", lambda: set_next_text(99), lambda: increment_score(-15)),
                ("You just need to learn when to stop.", lambda: set_next_text(99), lambda: increment_score(-15)),
            ],
        },
        99: {
            "text": "Unknown girl:\nIn the end, there is no escape from what you truly feel.",
            "options": [
                ("Maybe I have no choice.", lambda: set_next_text(109), lambda: increment_score(-5)),
                ("I refuse to surrender.", lambda: set_next_text(109), lambda: increment_score(-25)),
            ],
        },
        100: {
            "text": "Unknown girl:\nYou… ",
            "options": [],
        },
        101: {
            "text": "Unknown girl:\nYou don’t appreciate me at all, do you?",
            "options": [],
        },
        102: {
            "text": "Narrator:\nHer voice shakes.",
            "options": [],
        },
        103: {
            "text": "Unknown girl:\nI guess I have no use for you then.",
            "options": [],
        },
        104: {
            "text": "",
            "options": [],
        },
        105: {
            "text": "Unknown girl:\nYou’re perfect.",
            "options": [],
        },
        106: {
            "text": "Unknown girl:\nYou’re mine now.",
            "options": [],
        },
        107: {
            "text": "Unknown girl:\nForever and ever~",
            "options": [],
        },
        108: {
            "text": "",
            "options": [],
        },
        109: {
            "text": "",
            "options": [],
        },
        110: {
            "text": "Unknown girl:\nYou know, I'm really not interested—it's been a bore anyway.",
            "options": [],
        },
        111: {
            "text": "Narrator:\nA wave of relief washes over you as her indifferent tone confirms your escape.",
            "options": [],
        },
        112: {
            "text": "Unknown girl:\nGoodbye then... Enjoy your freedom.",
            "options": [],
        },
        113: {
            "text": "",
            "options": [],
        },
    }

    set_next_text(current_text_index)

    in_game = True
    in_game_menu = False
    in_main_menu = False
    reverse = False
    dialog_start = True

    while in_game:
        update_cursor(buttons)
        screen.blit(pygame.transform.scale(game_background, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))

        # Draw character upon arrival and till end
        if current_text_index in range(3, 200):
            screen.blit(pygame.transform.scale(ch_active, (char_width, char_height)), (char_x, char_y))

        jump_speed = 7

        # Character jumping animation
        if dialog_start and current_story_text.startswith("Unknown girl:") and "\n" in current_story_text:
            if char_y < SCREEN_HEIGHT - char_height - text_box_height - text_box_margin * 4:
                reverse = True
            elif char_y > SCREEN_HEIGHT - char_height - text_box_height - text_box_margin:
                reverse = False

            if reverse:
                char_y += jump_speed
            elif char_y > SCREEN_HEIGHT - char_height - text_box_height - text_box_margin:
                char_y = SCREEN_HEIGHT - char_height - text_box_height - text_box_margin
                dialog_start = False
            else:
                char_y -= jump_speed

        score_animation_speed = 1  # Adjust speed (higher = faster animation)

        if SCORE < target_score:
            SCORE += min(score_animation_speed, target_score - SCORE)  # Increment gradually
        elif SCORE > target_score:
            SCORE -= min(score_animation_speed, SCORE - target_score)  # Decrement gradually

        # Typing logic
        if not typing_finished:
            current_time = pygame.time.get_ticks()
            if current_time - typing_timer > 1000 // typing_speed:
                dialog_start = True

                # Determine how much of the text should be typed:
                if current_story_text.startswith("Narrator:") and "\n" in current_story_text:
                    # Split into narrator (displayed instantly) and remainder (typed)
                    _, remainder = current_story_text.split("\n", 1)
                    effective_length = len(remainder)

                elif current_story_text.startswith("Unknown girl:") and "\n" in current_story_text:
                    _, remainder = current_story_text.split("\n", 1)
                    effective_length = len(remainder)

                else:
                    effective_length = len(current_story_text)

                # Increment the typing index only for the remainder (or whole text)
                if typing_index < effective_length:
                    typing_index += 1
                    letter_sound.play()

                typing_timer = current_time

                if typing_index >= effective_length:
                    typing_finished = True
                    show_buttons = bool(storyline[current_text_index]["options"])

                if typing_index >= len(current_story_text):
                    typing_finished = True
                    show_buttons = bool(storyline[current_text_index]["options"])

        # Draw text box
        draw_text_box(current_story_text, typing_index)

        # Draw score bar with appearance of the character till end
        if current_text_index in range(3, 200):
            draw_score_bar()

        # Draw buttons if typing is finished
        if show_buttons:
            for button in buttons:
                button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_menu()

                elif event.key == pygame.K_F11:
                    toggle_fullscreen()

                    text_box_height = SCREEN_HEIGHT // 4
                    char_width, char_height = SCREEN_WIDTH // 4, SCREEN_HEIGHT // 1.5
                    char_x = (SCREEN_WIDTH - char_width) // 2
                    char_y = SCREEN_HEIGHT - char_height - text_box_height - text_box_margin

                    buttons = create_options_buttons(storyline[current_text_index]["options"])

                    bar_width = SCREEN_WIDTH // 20
                    bar_x = SCREEN_WIDTH - bar_width - bar_margin
                    bar_y = bar_margin
                    bar_height = SCREEN_HEIGHT - bar_margin * 2

                elif event.key in (pygame.K_SPACE, pygame.K_RETURN):
                    # Skip typing or proceed to the next text
                    if not typing_finished:
                        typing_finished = True
                        typing_index = len(current_story_text)
                        show_buttons = bool(storyline[current_text_index]["options"])

                    else:
                        # Proceed automatically if no options
                        if not show_buttons:
                            next_index = current_text_index + 1
                            if next_index in storyline:
                                set_next_text(next_index)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if not typing_finished:
                        typing_finished = True
                        typing_index = len(current_story_text)
                        show_buttons = bool(storyline[current_text_index]["options"])

                    else:
                        # Proceed automatically if no options
                        if not show_buttons:
                            next_index = current_text_index + 1
                            if next_index in storyline:
                                set_next_text(next_index)

                elif event.button == 6:
                    game_menu()

                # Continue the storyline
                if current_text_index == 8:
                    current_text_index = 14

                elif current_text_index == 18:
                    current_text_index = 22

                elif current_text_index == 28:
                    current_text_index = 34

                elif current_text_index == 38:
                    current_text_index = 44

            if show_buttons:
                for button in buttons:
                    button.handle_event(event)

        # Set different character states
        if current_text_index in [3, 15, 18, 32, 42, 54, 55, 67, 70, 71, 72]:
            ch_active = ch_1

        if current_text_index in [4, 8, 21, 22, 34, 43, 44, 45, 56, 57, 74, 76, 81, 82, 85]:
            ch_active = ch_2

        if current_text_index in [6, 7, 23, 24, 25, 33, 46, 47, 59, 61, 63, 79, 89]:
            ch_active = ch_3

        if current_text_index in [5, 20, 48, 51, 60, 66, 77, 83, 88, 89, 90, 92, 99, 110]:
            ch_active = ch_fc_plm

        if current_text_index in [30, 31, 40, 41, 49, 58, 62, 69, 74, 75, 87, 91, 95, 98, 100]:
            ch_active = ch_sad

        if current_text_index == 103:
            ch_active = ch_mad_knife

        if current_text_index == 105:
            ch_active = ch_knife

        # If player dies jump to killing text and show death screen
        if current_text_index == 104 or current_text_index == 108:
            hit.play()
            end_game_screen()

        # Stop music if player is about to win
        if current_text_index == 109:
            in_game_music.stop()

        # Show victory screen
        if current_text_index == 113:
            global win
            win = True
            victory.play()
            end_game_screen()

        pygame.display.flip()
        clock.tick(FPS)

def game_menu():
    """Displays an in-game menu with a transparent overlay and buttons."""
    global in_main_menu, in_game_menu, in_options

    # Resumes the game when paused
    def resume_game():
        global in_game_menu
        in_game_menu = False

    buttons = create_buttons([
        (SCREEN_HEIGHT //4, "Resume", resume_game),
        (SCREEN_HEIGHT //4, "Back to Menu", main_menu_reset),
        (SCREEN_HEIGHT //4, "Options", options),
        (SCREEN_HEIGHT //4, "Quit", quit_game),
    ])

    overlay_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay_surface.fill((0, 0, 0, 128))
    screen.blit(overlay_surface, (0, 0))

    in_game_menu = True
    in_main_menu = False
    in_options = False

    while in_game_menu:
        update_cursor(buttons)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                in_game_menu = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 6:
                in_game_menu = False

            for button in buttons:
                button.handle_event(event)
                button.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

def end_game_screen():
    """Displays the end game screen."""
    global in_game, in_end_game

    buttons = create_buttons([
        (SCREEN_HEIGHT // 2, "Back to Menu", main_menu_reset),
        (SCREEN_HEIGHT // 2, "Quit", quit_game),
    ])

    # Set the overlay on the whole screen
    end_overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)

    if not win:
        end_game_music.play(-1)
        end_overlay.fill((255, 0, 0, 1))
    else:
        celebration.play(-1)
        end_overlay.fill((0, 255, 0, 255))

    # Draw menu overlay
    screen.blit(end_overlay, (0, 0))

    if not win:
        draw_text("Game Over", TITLE_FONT, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 5)
    else:
        draw_text("Victory", TITLE_FONT, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 5)

    in_end_game = True
    in_game = False

    while in_end_game:
        update_cursor(buttons)

        # Redraw overlay creating an interesting fading animation if game lost
        if not win:
            screen.blit(end_overlay, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            for button in buttons:
                button.handle_event(event)

        for button in buttons:
            button.draw(screen)

        # Redraw text so it is always on top if game lost
        if not win:
            draw_text("Game Over", TITLE_FONT, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 5)

        pygame.display.flip()
        clock.tick(FPS)

def options():
    """Displays the options menu with volume sliders."""
    global bg_music_volume, effects_volume, in_options, in_game_menu, in_main_menu

    # Switches back to the previous screen from which the options were accessed
    def previous_screen():
        global in_main_menu, in_game_menu, in_options
        if in_main_menu:
            main_menu()
        else:
            in_options = False

    buttons = create_buttons([
        (SCREEN_HEIGHT - (SCREEN_HEIGHT // 12)*2, "Back", previous_screen),
    ])

    # Slider parameters
    slider_width = 300
    slider_height = 10
    slider_knob_radius = 15

    # Slider positions
    bg_slider_rect = pygame.Rect(
        SCREEN_WIDTH // 2 - slider_width // 2,
        SCREEN_HEIGHT // 3,
        slider_width,
        slider_height,
    )

    effects_slider_rect = pygame.Rect(
        SCREEN_WIDTH // 2 - slider_width // 2,
        SCREEN_HEIGHT // 2,
        slider_width,
        slider_height,
    )

    def draw_slider(rect, volume, label):
        """Draws a slider with the current volume."""
        # Draw slider line
        pygame.draw.rect(screen, (200, 200, 200), rect)

        # Draw slider knob
        knob_x = rect.x + int(volume * rect.width)
        knob_y = rect.y + rect.height // 2
        pygame.draw.circle(screen, (255, 255, 255), (knob_x, knob_y), slider_knob_radius)

        # Draw label
        font = pygame.font.Font("assets/Fonts/Comfort-Bold.ttf", 24)
        label_surface = font.render(f"{label}: {round(volume * 100)}%", True, (255, 255, 255))
        screen.blit(label_surface, (rect.x, rect.y - 40))

    in_options = True
    in_game_menu = False

    while in_options:
        update_cursor(buttons)
        # Background color
        screen.fill((30, 30, 30))

        # Draw sliders
        draw_slider(bg_slider_rect, bg_music_volume, "Music Volume")
        draw_slider(effects_slider_rect, effects_volume, "Effects Volume")

        for button in buttons:
            button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    previous_screen()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if bg_slider_rect.collidepoint(event.pos):
                        bg_music_volume = (event.pos[0] - bg_slider_rect.x) / slider_width
                        main_menu_music.set_volume(bg_music_volume)
                        in_game_music.set_volume(bg_music_volume)
                        end_game_music.set_volume(bg_music_volume)
                        celebration.set_volume(bg_music_volume)

                    elif effects_slider_rect.collidepoint(event.pos):
                        effects_volume = (event.pos[0] - effects_slider_rect.x) / slider_width
                        letter_sound.set_volume(effects_volume)
                        button_click.set_volume(effects_volume)
                        button_hover.set_volume(effects_volume)
                        hit.set_volume(effects_volume)
                        victory.set_volume(effects_volume)
                        letter_sound.play()

                elif event.button == 6:
                    previous_screen()

            # Dragging
            elif event.type == pygame.MOUSEMOTION and event.buttons[0]:
                if bg_slider_rect.collidepoint(event.pos):
                    bg_music_volume = max(0, min(1, (event.pos[0] - bg_slider_rect.x) / slider_width))
                    main_menu_music.set_volume(bg_music_volume)
                    in_game_music.set_volume(bg_music_volume)
                    end_game_music.set_volume(bg_music_volume)
                    celebration.set_volume(bg_music_volume)

                elif effects_slider_rect.collidepoint(event.pos):
                    effects_volume = max(0, min(1, (event.pos[0] - effects_slider_rect.x) / slider_width))
                    letter_sound.set_volume(effects_volume)
                    button_click.set_volume(effects_volume)
                    button_hover.set_volume(effects_volume)
                    hit.set_volume(effects_volume)
                    victory.set_volume(effects_volume)
                    letter_sound.play()

            for button in buttons:
                button.handle_event(event)
                button.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

def quit_game():
    """Quits the game."""
    pygame.quit()
    sys.exit()

def game_loop():
    """Main game loop."""
    # Start the game and play the main menu music
    main_menu_music.play(-1)
    main_menu()

if __name__ == "__main__":
    game_loop()