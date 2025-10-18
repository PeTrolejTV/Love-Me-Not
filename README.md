# **Love Me Not - Game Design Document - EN**
In a world where love is deadly, survival means rejection. In Love Me Not, you must outwit an obsessive girl desperate for your affection. Use clever dialogue, strategic choices, and careful planning to break her heart before she breaks yours—literally. Will you escape her twisted love, or will your rejection lead to your demise?

**Author**: Peter Majerik

**Chosen theme**: Losing to win

---

## **1. Introduction**

*Love Me Not* is a narrative-driven survival game developed in **Pygame-CE** as part of the Object Technologies subject. The game creates a functional prototype that immerses the player in a world where romance hides lethal danger. Instead of winning hearts, your objective is to manipulate dialogue and choices to lower the affection of obsessive, dangerous yandere character—ensuring your survival.

In this game, you find yourself surrounded by a girl whose growing obsession can quickly turn deadly. The twist? You must actively reject her advances to keep her at bay. Your success depends on making smart decisions in dialogue and using environmental cues to reduce her dangerous affection levels.

The game fully embraces the theme **"Losing to Win"**—your survival hinges on causing the yander character to lose interest rather than forging a traditional romantic connection.

---

### **1.1 Inspiration**  

<ins>**Doki Doki Literature Club!**</ins>

*Doki Doki Literature Club!* starts as a seemingly innocent dating sim and gradually morphs into a psychological horror experience. The subtle interplay between charming interactions and dark, hidden agendas inspired *Love Me Not*’s narrative design, where emotional manipulation and survival under duress are key.

<p align="center">
  <img src="https://github.com/PeTrolejTV/Love-Me-Not/blob/main/LoveMeNot/gallery/doki_doki_literature.png" alt="Doki Doki Literature Club!">
  <br>
  <em>Figure 1 Preview of Doki Doki Literature Club!</em>
</p>

---

<ins>**Yandere AI Girlfriend Simulator ~ With You Til The End**</ins>

This simulation game places you in an increasingly dangerous relationship with an obsessive yandere character. The core mechanic—managing an AI’s overbearing affection through subtle interactions—inspired the gameplay of *Love Me Not*. Here, you must navigate conversations, dodge romantic traps, and use strategic dialogue choices to keep your would-be admirer’s obsession from escalating to violence.

<p align="center">
  <img src="https://github.com/PeTrolejTV/Love-Me-Not/blob/main/LoveMeNot/gallery/yandere_ai.png" alt="Yandere AI Girlfriend Simulator">
  <br>
  <em>Figure 2 Preview of Yandere AI Girlfriend Simulator ~ With You Til The End</em>
</p>

Both of these inspirations serve as the foundation for *Love Me Not*, combining psychological tension with the dark humor of a twisted dating sim.

---

### **1.2 Player Experience**

In *Love Me Not*, your goal is to survive. As her affection increases, so does the threat level. Instead of winning her heart, you must actively lower her interest by making carefully considered dialogue choices.

Key aspects include:
- **Dynamic Dialogue**: The narrative is delivered via a typewriter-style effect. Notably, lines spoken by the narrator (or “Unknown girl:”).
- **Emotional Management**: Your decisions directly influence an on-screen affection meter. Too high, and the girls obsession becomes lethal. Too low, and she will dispose of you.

Every interaction is a delicate dance between rejection and survival—the more you resist, the more you secure your escape.

--- 

### **1.3 Development Software**
- **Pygame-CE**: The core framework and language for game development.
- **PyCharm 2024.3 & Visual Studio Code**: The Integrated Development Environment (IDE) used for coding.
- **Adobe Photoshop**: For creating and editing game graphics.
- **Audacity**: For sound effects and audio editing.

---

## **2. Concept**

### **2.1 Gameplay Overview**
In *Love Me Not*, you are an ordinary person caught in a series of intense encounters with an obsessive yandere girl. Your task is not to gain her affection but to strategically diminish it through clever dialogue and situational choices. Each encounter determines if you slip further into danger or manage to break the grip of her obsession.

Key gameplay features:
- **Narrative Dialogue with a Twist**: Dialogue is rendered with a custom typewriter effect. Special logic ensures that narrator labels or identifiers (such as “Narrator:” or “Unknown girl:”) are displayed immediately, while the actual dialogue is typed out slowly.
- **Affection Management**: The game tracks the character’s affection level. Crossing certain thresholds escalates the threat, pushing them from mere infatuation to violent obsession.
- **Choice-Driven Outcomes**: Every dialogue option and environmental interaction carries consequences—manipulate emotions to lower dangerous affection levels and survive.

### **2.2 Theme Interpretation (Losing to Win)**
The theme **"Losing to Win"** encapsulates the paradox of achieving success through intentional failure. In traditional dating sims, winning someone’s heart is the ultimate goal; here, you must deliberately cause your admirer’s affection to falter. Each rejection, every strategic misstep in romance, is a calculated move toward survival. The game challenges conventional romantic narratives by showing that true victory lies in the art of emotional sabotage.

### **2.3 Primary Mechanics**
- **Emotional Manipulation**: Dialogue choices directly influence affection meters. Reject or subvert romantic advances to lower your target’s obsession.
- **Typewriter Dialogue System**: A custom-built effect displays text letter-by-letter—except for specific parts (e.g., character labels) which appear instantly—to enhance narrative tension.
- **Affection Thresholds**: Predefined limits trigger escalated, more dangerous behavior if crossed.
- **Consequences for Failure**: Allowing the affection meter to spike leads to game over scenarios, emphasizing the stakes of every choice.

### **2.4 Class Design**
- **Game Engine**: Manages the overall game loop, dialogue progression, music and sound effects, and the interplay between narrative and gameplay mechanics.
- **Dialogue Manager**: Controls the typewriter effect, splitting dialogue into instantly shown identifiers and slowly typed messages.
- **Button & UI Classes**: Handle interactive elements from menus to in-game dialogue choices.
- **Audio Controller**: Manages multiple background tracks and sound effects, with custom sliders to adjust volume dynamically.
- **Character**: Organizes character states, dialogue outcomes, and affection levels effectively.

This architecture creates a rich tapestry of strategy, suspense, and psychological tension—perfectly suited to the theme of subverted romance.

--- 

## **3. Art**  
The art of *Love Me Not* marries romantic allure with psychological horror. The hand-drawn visuals emphasize both the beauty and the underlying menace of the narrative.

- **Character Art**:
  - **Surface Appearance**: Characters are depicted with soft lines, gentle blushes, and vibrant details that initially charm the player.
  - **Hidden Depths**: Subtle hints—like an unsettling glint in the eye or a slightly off smile—reveal the dangerous obsession beneath.
  - **Dynamic Expressions**: As dialogue unfolds and choices are made, character portraits and body language shift to reflect increasing intensity or aggression.
    - *Characters were generated using Generative AI and later edited in photoshop*

- **Environmental Art**:  
  - The game features a single, striking gradient background that serves as the visual foundation for every scene.
  - This minimalist design employs a smooth transition of colors—ranging from deep, moody hues to soft, ambient tones—to evoke both serenity and underlying tension.
  - The subtle shifts in the gradient not only create an atmospheric backdrop but also mirror the evolving emotional landscape of the narrative, reinforcing the game's themes of hidden danger beneath a deceptively calm exterior.

- **Thematic Overlays**:  
  - As the tension escalates, elements evolve—during defeat, the screen smartly animates into a deep, blood-red fade, signaling a fatal outcome with striking visual impact.
  - Conversely, a successful escape is marked by a soothing green overlay, symbolizing victory and renewal.

<p align="center">
  <img src="https://github.com/PeTrolejTV/Love-Me-Not/blob/main/LoveMeNot/gallery/yandere_girl.png" alt="Yandere girl">
  <br>
  <em>Figure 3 Preview of Yandere girl</em>
</p>

The visual design reinforces the game’s central message: success is found in rejecting affection—a victory that comes at the cost of conventional romance.

---

### **3.1 Theme Interpretation: Losing to Win**  
The core theme of *Love Me Not*—losing to win—is woven through every artistic and narrative detail:  

- **Visual Symbolism**:  
  - The perfection of the characters becomes oppressive, visually communicating that true freedom comes from breaking away.
  
- **Narrative Impact**:  
  - Success is depicted as liberation, even as it comes with a bittersweet aesthetic.

- **Duality and Contrast**:  
  - Romantic visuals collide with dark, horror-inspired imagery, underlining the conflict between tender affection and dangerous obsession.

---

### **3.2 Design**
*Love Me Not* is crafted with a hand-drawn aesthetic that blends delicate romance with unsettling horror. The design emphasizes:

- **Character Details**:  
  - Exaggerated features that hint at both charm and menace.
  - Expressive animations and state changes that reveal the emotional and psychological evolution of the characters.

- **Backgrounds & Settings**:  
  - Idyllic locations that slowly morph into oppressive environments as danger escalates.
  - Use of color, light, and shadow to evoke a sense of impending doom even in everyday scenes.

- **User Interface**:  
  - Menus and dialogue boxes that combine soft pastel tones with sharp, unsettling details.
  - Interactive elements like buttons and sliders maintain the romantic theme while adapting to changes in narrative tone.

<p align="center">
  <img src="https://github.com/PeTrolejTV/Love-Me-Not/blob/main/LoveMeNot/gallery/design_concept.png" alt="Design concept">
  <br>
  <em>Figure 4 Design concept</em>
</p>

This distinctive art style creates an immersive atmosphere where beauty and danger coexist.

---

## **4. Audio**

### **4.1 Music**
Music plays a pivotal role in setting the mood in *Love Me Not*. The background tracks—sourced from royalty-free libraries on YouTube—are carefully chosen to reflect the game’s dual nature of romance and suspense.

#### **Music Themes and Styles**

- **Main Menu Theme**:  
  A haunting piano melody with melancholic undertones that immediately set the eerie, bittersweet tone.
  - https://www.youtube.com/watch?v=mnA2CRs7T9Q

- **In Game Background Music**:  
  Light, whimsical tunes with an eerie twist give way to dissonant strings and subtle electronics as encounters grow tense.
  - https://www.youtube.com/watch?v=3V-pYCGx0C4

- **Game Over & Victory Themes**:  
  Chilling, somber melodies underscore failure, while bittersweet orchestral pieces celebrate narrow escapes—each reinforcing the emotional weight of your choices.
  - https://www.youtube.com/watch?v=h1wSPmlZV-w
  - https://www.youtube.com/watch?v=3GwjfUFyY6M

### **4.2 Sound Effects**
Sound effects in *Love Me Not* are finely tuned to enhance the immersive, unsettling atmosphere:

- **Dialogue Interactions**:  
  Subtle typing sounds underscore the unique typewriter effect, with distinct audio cues for different characters (narrator vs. unknown girl).
  - https://www.youtube.com/watch?v=FP_TCP73h2I

- **Ending encounters**:  
  Slashing sound of the player, resulting in death, or a classic "tada" celebration sound of succes.
  - https://www.youtube.com/watch?v=4bJI-e28kFg
  - https://www.youtube.com/watch?v=1Qo7KTtO4MY

- **UI Feedback**:  
  Button clicks and hover sounds provide responsive feedback, enhancing the overall tactile feel of the game.
  - https://www.youtube.com/watch?v=YNSbL-Cek1c
  - https://www.youtube.com/watch?v=_vjTeR9iw8o

The audio design, much like the visuals, supports the game’s central narrative: survival through the deliberate subversion of traditional romance.

---

## **5. Game Experience**

### **5.1 UI**
The user interface in *Love Me Not* is designed to be both intuitive and atmospheric, blending elegant romantic motifs with subtle hints of horror.

#### **Main Menu**  
- **Title Screen**:  
  Features the game logo with a wilted rose motif against a haunting, whimsical background.

- **Menu Options**:  
  - **Start Game**: Begin your journey into the world of obsessive love.
  - **Options**: Adjust settings including volume sliders for both music and sound effects.
  - **Quit**: Exit the game.

#### **In-Game UI**  
- **Dialogue Box**:  
  - Displays conversation with a custom typewriter effect—instant identifiers (e.g., “Narrator:” or “Unknown girl:”) followed by slowly rendered dialogue.

- **Character Portraits**:  
  - Dynamic portraits that shift to reflect the emotional and physical states of character.

- **Affection Meter**: 
  - A bar that tracks the intensity of the yandere’s obsession.

#### **Pause Menu**  
- Activated by pressing **Escape**, it offers options to resume, change settings, or return to the main menu.

#### **End Screen**  
- Displays context-sensitive messages like game over or victory which is based on your performance.

---

### **5.2 Controls**
<ins>**Keyboard**</ins>
- **Escape**: Opens the pause menu / Back.
- **Enter / Space**: Skips dialogue or confirms a choice.
- **F11**: Go into windowed mode while in main menu or in game.

<ins>**Mouse**</ins> 
- **Left Click**: Skips dialogue or selects options.
- **Lower side button**: Opens the pause menu / Back.

---

## **6. Technical Details**

### **6.1 Core Engine**
*Love Me Not* is built using **Pygame-CE**, leveraging its capabilities for handling graphics, audio, and input. The engine supports:
- A dynamic dialogue system with a typewriter effect.
- Custom UI components including interactive buttons and volume sliders.
- Real-time audio management with multiple background tracks and sound effects.
- A branching narrative system that adjusts dialogue and outcomes based on player choices.

### **6.2 Audio Management**
The game uses `pygame.mixer.Sound` objects to manage multiple background tracks and sound effects. Custom volume sliders in the Options menu allow players to adjust the levels for music and effects independently, ensuring an immersive audio experience that adapts to the evolving narrative.

### **6.3 Dialogue System**
A key innovation in *Love Me Not* is its dialogue system. Using a combination of instantly rendered identifiers (e.g., "Narrator:" or "Unknown girl:") and a letter-by-letter typewriter effect for dialogue, the system creates a unique storytelling experience that heightens suspense and emotional engagement.

---

## **7. Conclusion**

*Love Me Not* subverts traditional romance by challenging players to succeed through rejection. In a world where love can be lethal, every choice matters—each moment is a battle against dangerous obsession. With its innovative dialogue system, striking art, and atmospheric audio, the game offers an unforgettable journey into the darker side of love.

Will you be able to break her heart before she breaks yours?

---

## 🎮 How to Play Love Me Not

1. **Download the project**
   - Click the green **"Code" → "Download ZIP"**, then extract it anywhere on your PC

2. **Open the folder**
   - Go to: `Love-Me-Not-main/LoveMeNot`

3. **Run the game**
   - To **build an EXE** → double-click `build_exe.bat`
   - To **Play** the game → open the newly created folder `dist` and double-click on `main.exe`
