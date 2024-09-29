# # Define characters and narrator
# # define narrator = Character("Narrator", color="#A9A9A9")
# # define boy_story = Character("The Boy (Story)", color="#87CEFA")
# # define girl_story = Character("The Girl (Story)", color="#FF69B4")
# # define boy_current = Character("The Boy (Current)", color="#4682B4")
# # define girl_current = Character("The Girl (Current)", color="#FF6347")
# # define steve = Character("Steve", color="#ADFF2F")

# # # Define backgrounds and music
# # define bg_beginning = "backgrounds/beginning_of_time.png" # Add actual background image file names
# # define bg_pink = "backgrounds/pink_scene.png"
# # define bg_river = "backgrounds/river_scene.png"
# # define bg_moonlight = "backgrounds/moonlight_scene.png"
# # define bg_couch = "backgrounds/couch_scene.png"

# # define music_mellow = "music/mellow_music.mp3"
# # define music_steve = "music/steve_music.mp3"
# # define music_walk = "music/walk_by_river.mp3"
# # define music_drenched = "music/drenched_wanting.mp3"

# # Start of the game
# label start:
#     # Show the background and play mellow music
#     # scene bg_beginning
#     # play music music_mellow
    
#     # narrator "Once upon a time, there was a boy..."
    
# #     # Show the cartoonish hand-drawn boy and girl
# #     show boy_story
# #     narrator "A girl..."
    
# #     show girl_story
# #     narrator "And Steve."
    
# #     # Steve enters, with his own music
# #     play music music_steve
# #     show steve
# #     narrator "Steve was wholesome. Steve knew both the girl and the boy, and that's how they met."
    
# #     narrator "[Thank you Steve, now go away]"
# #     hide steve
# #     stop music

# #     narrator "The girl and the boy went for a late-night walk by the river. At that time, little they knew they'd be doing this every other day as long as they're together."

# #     narrator "Little they know they'd be like two entangled quantum states."

# #     show boy_story
# #     boy_story "Well technically..."

# #     show girl_story
# #     girl_story "[The you-know-I'll-kick-your-ass-if-you-interrupt-the-story kind of look.]"

# #     narrator "For the boy, the girl was just a girl. Maybe smarter and cuter, but still just a girl."
    
# #     boy_story "Also maybe smarter and cuter than other boys?"
# #     girl_story "Nah, just a boy."

# #     narrator "So let the story begin..."

# #     # Scene change to pink background with new music
# #     scene bg_pink
# #     play music "music/new_scene_music.mp3"
    
# #     narrator "Once upon a time, the boy met the girl."

# #     # Texting scene (using different fonts or styles for texting messages can be added)
# #     show boy_current
# #     show girl_current

# #     girl_current "Heard that you're not feeling well."
# #     girl_current "And that you're CRACKED."

# #     boy_current "What happened? lol :D"
# #     girl_current "I met James Blonde at an event. He said you have a headache."

# #     boy_current "James Blonde?"

# #     girl_current "Do you want to grab food or go for a walk sometime?"

# #     # Player makes a choice here
# #     menu:
# #         "How about now?":
# #             jump walk_now
# #         "I'm a little busy. Let me check my calendar.":
# #             jump walk_later

# # # Label for the walk now choice
# # label walk_now:
# #     narrator "They went for a walk that night."
# #     scene bg_river
# #     play music music_walk
# #     narrator "They walked and talked about dreams, James Blonde, and garbage collectors."

# #     # Continue the conversation...
# #     jump moonlight_scene

# # # Label for the walk later choice
# # label walk_later:
# #     narrator "The boy was busy coding, the girl went running."
# #     narrator "They probably went for a walk later, but that's another story."
# #     return  # End the story if the walk doesn't happen

# # # Moonlight scene
# # label moonlight_scene:
# #     scene bg_moonlight
# #     narrator "One late night, they decided to sit down on the grass and look at the moon."
    
# #     boy_story "Do you want to use my bag as a pillow?"
# #     girl_story "LMAO"
    
# #     # Continue dialogue...

# #     menu:
# #         "Confess":
# #             jump confession
# #         "Do not confess":
# #             jump no_confession

# # # Confession path
# # label confession:
# #     narrator "They confessed their feelings and held hands."
# #     # Play some emotional music, show new images
# #     play music "music/confession_theme.mp3"
# #     narrator "For the first time, the boy let himself fall."
# #     # Continue...

# # # No confession path
# # label no_confession:
# #     narrator "They decided to remain friends. They thought about each other for a while, but life moved on."
# #     narrator "They both became successful, and maybe, they'd meet again one day, among the stars."
# #     return  # End the story if the confession doesn't happen
