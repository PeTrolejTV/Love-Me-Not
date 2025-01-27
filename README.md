# **Love Me Not - Game Design Document - EN**
In a world where love is deadly, survival means rejection. In Love Me Not, you must outwit obsessive yanderes desperate for your affection. Use clever dialogue, strategic choices, and careful planning to break their hearts before they break yours—literally. Will you escape their twisted love, or will your rejection lead to your demise?

**Author**: Peter Majerik

**Chosen theme**: Losing to win

---

## **1. Introduction**

The proposed game, **Love Me Not**, serves as a creative demonstration of the concept of survival in a unique emotional environment, developed as part of the Object Technologies subject. The game aims to create a functional prototype that showcases the player’s struggle against yandere characters who progressively become more obsessive and dangerous.

In this game, the player finds themselves surrounded by yandere girls, each driven by intense emotional fixation. The goal of the player is not to win their hearts, but to navigate the dangers of their obsessive love by making the right choices to lower their affection. The player must strategically avoid becoming the target of their affection while managing the escalating threat of violence as the characters grow increasingly obsessed.

The game meets the requirements of the theme "Losing to Win," as the player must actively work to make the yandere girls lose interest in order to survive. Instead of traditional combat or conflict resolution, the player’s success depends on their ability to manipulate emotions and outsmart the yandere characters within a time-limited encounter.

---

### **1.1 Inspiration**  

<ins>**Doki Doki Literature Club!**</ins>

**Doki Doki Literature Club!** is a visual novel that begins as a typical dating sim but gradually turns into a psychological horror experience. The player navigates through interactions with seemingly normal characters, but the game takes dark twists, revealing disturbing elements. The concept of **emotional manipulation** and **survival** is explored through the interactions with the characters, with the player needing to make careful choices to avoid harm. The game challenges the typical romantic tropes, much like how **Love Me Not** twists the concept of dating by making the player avoid gaining affection to survive.

<p align="center">
  <img src="https://github.com/PeTrolejTV/Love-Me-Not/blob/main/doki_doki_literature.png" alt="Doki Doki Literature Club!">
  <br>
  <em>Figure 1 Preview of Doki Doki Literature Club!</em>
</p>

---

<ins>**Yandere AI Girlfriend Simulator ~ With You Til The End**</ins>

**Yandere AI Girlfriend Simulator ~ With You Til The End** is a simulation game where the player interacts with an AI-powered yandere character who becomes increasingly obsessed with the player. The game revolves around managing the player's relationship with the yandere character, who will do anything to keep the player close, even resorting to violent actions. The **primary gameplay mechanic** involves navigating through different scenarios where the player must avoid intensifying the yandere’s affection, which could trigger dangerous consequences.

Inspiration for **Love Me Not** is drawn from this game’s focus on **emotional manipulation** and survival within a dangerous, obsessive relationship. The player in **Love Me Not** will similarly need to make calculated choices to lower the characters' affection levels and avoid escalating their obsession to the point of violence. Much like in **Yandere AI Girlfriend Simulator**, the player's success hinges on managing the emotional dynamics with the yandere characters, but the twist is that the player must break the characters' hearts in order to survive.

<p align="center">
  <img src="https://github.com/PeTrolejTV/Love-Me-Not/blob/main/yandere_ai.png" alt="Yandere AI Girlfriend Simulator">
  <br>
  <em>Figure 2 Preview of Yandere AI Girlfriend Simulator ~ With You Til The End</em>
</p>

These two games, **Doki Doki Literature Club!** and **Yandere AI Girlfriend Simulator ~ With You Til The End**, offer a strong thematic and gameplay foundation for **Love Me Not**, focusing on the psychological manipulation of characters and the tension of surviving emotionally intense and obsessive relationships.

---

### **1.2 Player Experience**

In **Love Me Not**, the player's goal is to survive each encounter with the increasingly obsessive yandere characters within a **set time frame** (e.g., one day or event). The yandere girls grow more obsessed as time passes, and their behavior becomes more aggressive. Instead of traditional combat, the player must focus on maintaining distance, avoiding romantic advances, and making choices to **lower the yandere characters' interest**. 

The player can move through various settings—such as cafes, parks, and bedrooms—while interacting with objects and making key decisions that influence the yandere characters’ emotions. As the obsession builds, the player must **strategize to survive** without triggering violent reactions. The yandere characters "rush" towards the player emotionally, attempting to manipulate or force the player into dangerous situations. If their affection level becomes too high, the player is in danger of being harmed.

To succeed, the player must **outmaneuver the yandere characters** by making the right choices and using the environment to avoid their lethal attention. While the player can attempt to eliminate their emotional connection with the yandere girls, failure to maintain distance can lead to disastrous consequences. Timing is critical, and strategic decision-making is necessary to escape each encounter unscathed.

--- 

### **1.3 Development Software**
- **Pygame-CE**: chosen programming language.
- **PyCharm 2024.3**: chosen IDE.
- **Adobe Photoshop**: graphical tool for creating graphics.
- **Audacity**: for editing sound effects.

---

## **2. Concept**

### **2.1 Gameplay Overview**
In **Love Me Not**, the player controls a character navigating through a series of intimate encounters with yandere characters. The goal is not to win their hearts, but rather to maintain enough distance and keep them from becoming dangerously obsessed. The player must cleverly sabotage these relationships within a **limited time frame** (e.g., each day or encounter), avoiding emotional manipulation, and making the right choices to keep the yandere girls uninterested before they resort to violence.

The player can explore the environment, interact with objects, and make choices that influence the characters' affection levels. However, as the yandere’s obsession grows, their behavior becomes increasingly erratic, and the player must strategize to avoid being caught in their deadly trap.

### **2.2 Theme Interpretation (Losing to Win)**
**"Losing to Win"** - The theme of **Love Me Not** revolves around the paradox of success through failure. Instead of typical dating sim mechanics where the player tries to win the affection of the characters, the player must instead make choices that make the yandere girls lose interest. The enemies—who are supposed to be romantic interests—become increasingly dangerous as the player progresses. Their obsession escalates into violent tendencies, and the player’s survival depends on their ability to break their hearts without directly confronting them. At higher levels, the intensity of their obsession increases, requiring the player to take more drastic actions to keep them at bay.

### **2.3 Primary Mechanics**
- **Emotional Manipulation**: The player’s interactions with the yandere characters influence their affection levels. Instead of positive reinforcement, the player must use actions like avoiding emotional closeness, rejecting romantic advances, or intentionally causing misunderstandings to lower affection levels.
- **Environment Interactions**: The player can use objects found within the environment to either distract, deceive, or create emotional distance between themselves and the yandere characters. For example, offering gifts that appear sincere but are intended to confuse or mislead.
- **Time Pressure**: The game is divided into days or encounters, and each is timed. The player must act quickly to make the right choices within the limited time frame, or they risk the yandere characters becoming dangerously obsessed.
- **Obstacles**: The environment may change in response to the player’s decisions, introducing obstacles like locked doors, barriers, or heightened surveillance by the yandere characters that the player must navigate to maintain their escape.
- **Fixed Affection Tracking**: The characters’ affection levels are tracked and have fixed thresholds at which they become more obsessive and violent. These thresholds are set based on prior interactions, preventing the player from simply avoiding the yandere girls at all times.
- **Consequences for Failure**: If the player fails to lower the yandere's interest in time, they face the ultimate consequence: the character’s deadly actions, resulting in the player’s “game over.”

### **2.4 Class Design**
- **Game**: A class that will manage the main game loop, including tracking time, managing player interactions, handling character states, and triggering game-ending scenarios based on player choices.
- **Player**: A class representing the player, managing movement, interaction with objects, decision-making, and managing the player's health, affection status, and available actions.
- **Yandere**: A class representing the yandere characters, controlling their behavior, emotional states, and interactions with the player. This class tracks the characters' obsession levels, makes them move towards the player, and governs their violent reactions when their obsession reaches critical points.

This structure ensures a dynamic blend of strategy, choice, and psychological tension, making **Love Me Not** an engaging and unpredictable experience.

--- 

## **3. Art**  
The art of **Love Me Not** is a perfect blend of romantic allure and psychological horror, capturing the bittersweet and twisted nature of the game’s narrative. The hand-drawn style adds an intimate, personal touch, emphasizing the emotional stakes and psychological depth of the story.  

- **Character Art**:  
  - Characters are drawn with exquisite attention to detail, highlighting their dual personalities.  
    - *Surface Appearance*: Soft, clean lines and vibrant colors reflect their charming, romantic facades. Gentle blushes, intricate hairstyles, and expressive eyes exude innocence and allure.  
    - *Hidden Depths*: Subtle hints of their darker side—such as a slightly unsettling glint in their eyes, an overly perfect smile, or faint scars—foreshadow the danger beneath their beauty.  
  - Body language is carefully crafted, shifting from inviting gestures to possessive or aggressive stances as the player’s actions influence their emotions.  

- **Environmental Art**:  
  - The game world starts with idyllic, picture-perfect settings: sunlit cafes, flower-filled parks, and cozy bedrooms adorned with pastel tones.  
  - As the narrative darkens, the environments subtly shift—colors become colder, shadows grow deeper, and once-inviting spaces feel confining or distorted.  
  - Small details, like cracked mirrors or overgrown vines, symbolize the unraveling relationships and the player’s struggle to escape.  

- **Thematic Overlays**:  
  - Romantic imagery like hearts, roses, and glowing sparkles dominate the early game but slowly deteriorate. Broken hearts, wilting flowers, and fading glows reflect the theme of disillusionment and loss.  
  - Special effects, such as glitch-like distortions or bloodied visuals, emphasize the horror of a yandere’s obsession.  

---

### **3.1 Theme Interpretation: Losing to Win**  
The central theme of **Love Me Not**—losing to win—is cleverly reinforced through every artistic and narrative choice:  

- **Visual Symbolism**:  
  - The characters’ appearances mirror the theme. Their perfection becomes oppressive, reminding players that true victory lies not in achieving their love but in escaping it.  
  - The world around the player reflects their progress. Bright, romantic colors fade to darker tones, showing that success comes not from traditional romantic tropes but from breaking free.  

- **Narrative and Emotional Impact**:  
  - The player must actively sabotage relationships, rejecting the typical dating sim goal. Every action, from speaking truthfully to intentionally avoiding romantic gestures, carries an emotional weight as it conflicts with ingrained expectations of love.  
  - The art amplifies this conflict—what should feel like “failure” (breaking hearts) is visually portrayed as a victory (regaining control, escaping danger).  

- **Contrasts and Duality**:  
  - Romantic moments, like confession scenes, are designed to feel suffocating rather than heartwarming. The art uses bright but claustrophobic framing to reflect the yandere’s possessiveness.  
  - Victory, meanwhile, is depicted as freeing yet bittersweet—muted colors and open, minimalist backdrops signify the player’s escape but also the lingering weight of their choices.  

<p align="center">
  <img src="https://github.com/PeTrolejTV/Love-Me-Not/main/yandere_girl.png" alt="Yandere girl">
  <br>
  <em>Figure 3 Preview of Yandere girl</em>
</p>

The art and theme in **Love Me Not** work in harmony to subvert expectations. By challenging the player to embrace loss as a form of triumph, the game delivers a uniquely emotional and unforgettable experience.

---

### **3.2 Design**
The visual design of **Love Me Not** reflects a hauntingly beautiful world where romance and danger intertwine. The artwork, meticulously hand-drawn, combines soft, delicate details with striking contrasts, echoing the duality of sweet affection and lurking menace.  

### **Art Style and Aesthetic**  
- **Character Design**:  
  - Each yandere character features an alluring, polished appearance with exaggerated features that subtly hint at their obsessive nature—wide, sparkling eyes that can turn menacing, delicate smiles that hide dark intentions, and outfits reflecting their unique personalities.  
  - Hair and clothing are intricately detailed, with highlights and shadows emphasizing the character's emotional states.  

- **Backgrounds**:  
  - Romantic settings like cafes, parks, and cozy bedrooms are drawn with warm, inviting colors that conceal an underlying unease, achieved through subtle off-kilter angles, dark corners, or unexpected details like cracks or stains.  
  - Key scenes (e.g., moments of danger or conflict) use muted palettes, sharp shadows, and fragmented imagery to heighten tension.  

- **UI Design**:  
  - Soft, pastel hues dominate the menus, accented by floral motifs and heart shapes to reinforce the romantic theme.  
  - As the game progresses and the player encounters danger, these elements subtly darken or distort, mirroring the descent into chaos.  

- **Special Effects**:  
  - Stylized overlays, like faint blood splatters or cracks in the screen, appear during high-stakes moments, blending seamlessly with the hand-drawn aesthetic.  
  - Romantic interactions are enhanced with glowing hearts, sparkles, or gentle light beams, contrasting sharply with the horror elements.  

<p align="center">
  <img src="https://github.com/PeTrolejTV/Love-Me-Not/main/design_concept.png" alt="Design concept">
  <br>
  <em>Figure 4 Design concept</em>
</p>

This approach gives **Love Me Not** a unique and personal charm, immersing players in a world that’s as beautiful as it is terrifying.

---

## **4. Audio**

### **4.1 Music**
The background music in **Love Me Not** is an integral part of its atmosphere, weaving together romantic charm with an undertone of suspense and dread. All tracks are sourced from royalty-free libraries on YouTube, ensuring a professional yet accessible soundscape.  

### **Music Themes and Styles**  

- **Main Menu Theme**:  
  - A hauntingly beautiful piano melody with soft, melancholic undertones. The piece sets the mood for the game, blending romance and unease from the start.  
- **Yandere Encounters**:  
  - Light, whimsical tracks with an eerie twist, featuring instruments like celesta and harp to reflect the deceptive sweetness of the characters.  
  - As the situation intensifies, the music shifts to dissonant strings or subtle electronic beats to heighten the tension.  

- **Calm Exploration**:  
  - Atmospheric, ambient tracks with gentle acoustic guitar or piano provide a false sense of security during quieter moments.  
  - Subtle background harmonies hint at the underlying danger, keeping players on edge.  

- **High-Stakes Moments**:  
  - Fast-paced and dramatic pieces, with driving percussion and intense violins, accompany chase scenes or pivotal decisions.  
  - Glitchy electronic effects or distorted melodies mirror the chaotic nature of a yandere’s obsession.  

- **Game Over**:  
  - A chilling, somber melody—featuring slow piano chords and faint strings—emphasizes the tragic end of the player’s journey.  

- **Victory Theme**:  
  - A bittersweet orchestral piece with rising crescendos and gentle harmonies celebrates the player’s escape, leaving them relieved yet contemplative.  

The carefully chosen music ensures that every moment in **Love Me Not** resonates emotionally, drawing players into its unique blend of love and terror.

---

### **4.2 Sound Efects**
The sound effects in **Love Me Not** are carefully curated to heighten the tension and immerse players in its chilling romantic world. Sourced from royalty-free libraries on YouTube, the soundscape balances moments of eerie suspense with unsettlingly sweet undertones.  

### **Key Sound Effect Elements**  

- **Dialogue Interactions**:  
  - Soft, subtle sounds like a gentle page turn or a faint heart thud accompany character dialogue to emphasize the romantic yet foreboding tone.  
  - Choices are highlighted with light, crystalline chimes or ominous low notes, depending on their significance.  

- **Affection Meter Changes**:  
  - When a yandere grows closer to obsession, a rising, distorted heartbeat or a subtle string crescendo signals the danger.  
  - Successfully lowering their interest triggers soft sighs of relief or gentle, fading tones.  

- **Tension and Conflict**:  
  - Sudden jumps in intensity—like slamming doors, glass breaking, or the scrape of a knife—underscore dangerous moments.  
  - Chase sequences or critical decisions are backed by rapid, sharp sound cues, like frantic footsteps or quickened breaths.  

- **Atmosphere and Ambiance**:  
  - Subtle background effects like rustling leaves, distant whispers, or faint dripping water create a sense of unease in quieter scenes.  
  - Romantic moments are accompanied by faint harp plucks or delicate piano keys, masking the underlying danger.  

- **Game Over and Victory**:  
  - A chilling, melancholic melody signals a yandere’s victory over the player.  
  - Successfully escaping triggers a triumphant yet bittersweet chime, reflecting relief mixed with the memory of danger.  

The sound effects add depth to the narrative, immersing players in a world where love and fear intertwine.

---
## **5. Game Experience**

### **5.1 UI**
The UI in **Love Me Not** is designed to enhance the eerie yet playful atmosphere of the game while keeping interactions intuitive and immersive. Here's what players will see:  

### **Main Menu**  
- **Title Screen**: Featuring the game logo with a wilted rose motif and a haunting yet whimsical background.  
- **Menu Options**:  
  - **Start New Game**: Begin your journey into the yandere-infested world.  
  - **Load Game**: Continue from your last save.  
  - **Settings**: Adjust audio, visuals, and gameplay preferences.  
  - **Quit**: Escape to the safety of the desktop (for now).  

### **In-Game UI**  
- **Dialogue Box**:  
  - Displays character conversations with clean text and subtle decorative flourishes, like sharp-edged borders or fading hearts.  
  - Player choices appear in distinct buttons below the text, making critical decisions easy to navigate.  
- **Character Portraits**:  
  - Dynamic and expressive, reacting to dialogue and events to emphasize emotions (or growing yandere tendencies).  
- **Status Indicators**:  
  - **Affection Meter**: A heart icon shows how dangerously close a yandere is to obsessing over you.  
  - **Sanity Warning**: A subtle vignette effect or warning icon appears as things get tense.  

### **Pause Menu**  
- Accessed by pressing **Esc**, it includes:  
  - **Resume**: Jump back into the action.  
  - **Save/Load**: Manage your progress.  
  - **Settings**: Tweak game options without leaving the story.  
  - **Main Menu**: Exit to the title screen.  

### **End Screen**  
- Features a unique message depending on your outcome: escape, rejection, or a fatal misstep.  

The UI balances simplicity with thematic elements, blending romantic elegance and unsettling undertones.

---

### **5.2 Controls**
<ins>**Keyboard**</ins>
- **Escape**: Pauses the game and shows the Pause-Menu.
- **Enter**: Skips dialoge or selects an option.
- **Space**: Skips dialoge or selects an option.

<ins>**Mouse**</ins> 
- **Left button**: Skips dialoge or selects an option.

---
