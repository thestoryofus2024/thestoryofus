# Define characters and narrator
define n = Character("Narrator", color="#A9A9A9")
define bs = Character("The Boy", color="#87CEFA")
define gs = Character("The Girl", color="#FF69B4")
define bc = Character("The Boy (Now)", color="#4682B4")
define gc = Character("The Girl (Now)", color="#FF6347")

# Define backgrounds and music
define bg_pink = "backgrounds/pink_scene.png"
define bg_river = "backgrounds/river_scene.png"
define bg_moonlight = "backgrounds/moonlight_scene.png"
define bg_couch = "backgrounds/couch_scene.png"

define music_mellow = "music/mellow_music.mp3"
define music_steve = "steve.mp3"
define music_walk = "music/walk_by_river.mp3"
define music_drenched = "music/drenched_wanting.mp3"
define music_all_Iv_ever_known = "music/all_I've_ever_known.mp3"
define bg_music = "music/Is It Fate.mp3" # make it a list later

image white = "#f0dfb1"
image black = "#000000"

transform fit_screen:
    size (config.screen_width, config.screen_height)

transform left_center:
    xpos 0.0  # Aligns the image to the far left
    yalign 0.5  # Vertically center the image

transform right_center:
    xpos 1.0  # Aligns the image to the far right
    xanchor 1.0  # Ensures the image is anchored to the right edge
    yalign 0.5  # Vertically centers the image


label start:
label cartoonish_opening:     
    scene white

    stop music fadeout 3.0
    
    "Once upon a time"
    
    # Show the cartoonish hand-drawn boy and girl
    show boy cartoonish at left_center with moveinbottom
    "there was a boy..."

    show girl cartoonish at right_center with moveinbottom
    "A girl..."


    "they were totally NOT real"

    "oh and also one more person:"

    # Steve enters, with his own music
    play sound ["steve_longer.mp3"] fadeout 1.0 fadein 1.0 noloop
    show steve at center with moveintop
    "Steve."

    show steve
    "Steve was wholesome"
    
    "Steve knew both the girl and the boy, and that's how they met."
    
    "Thank you Steve, now go away"
    
    hide steve
    stop sound fadeout 1.0

    show boy cartoonish at truecenter with moveinright

    play music bg_music fadein 3.0 loop

    "The girl and the boy went for a late-night walk by the river."
    
    "At that time, little they knew they'd be doing this every other day as long as they're together."

    "Little they know they'd be like two entangled quantum states."

    bc "Well technically..."

    gc "a you-know-I'll-kick-your-ass-if-you-interrupt-the-story kind of look."

    "Ahem Ahem. so..."

    "For the boy, the girl was just a girl. Maybe smarter and cuter, but still just a girl."
    
    "For the boy, the girl was just a girl."
    
    "Ok, maybe smarter and cuter than other girls, but still just a normal girl."

    "and for the girl, the boy was just a boy."

    bc "Also maybe smarter and cuter than other boys?"
    gc "Naaaaah, just a boy."

    "and this is how the story began..."

    jump texting

label texting:
    scene rockefeller_center at truecenter

    
    show boy at left_center
    show girl at right_center

    show girl grins
    gs "Heard that you're not feeling well."
    gs "And that you're CRACKED."

    show boy surprised
    bs "What happened? lol :D"
    gs "I met James Blonde at an event. He said you have a headache."

    bs "James Blonde?"

    show girl curious
    gs "yeah yeah. The frat dude with typical white name. Idk if it was Alex or James"

    show boy panics
    bs "whaaaat"

    show girl smiles
    gs "Also do you want to grab food or go for a walk some time?"

    show boy grinsopen
    bs "I just had dinner, but we can go for a walk when you're back."

    show girl
    gs "sure, when?"

    # Player makes a choice here
    menu:
        "How about now?":
            jump walk_now
        "I'm a little busy. Let me check my calendar.":
            jump walk_later

label walk_now:
    scene black

    "They went for a walk that night."
    
    scene river at truecenter

    "They walked and talked about their dreams, James Blonde, and garbage collectors!!!"

    "They continued doing that for many other nights."
    
    "Every night the boy would write about the girl in his diaries."

    "and everything he learned from her"

    "They were both high achievers with big dreams for the future."

    "Although they were both stressed and under a lot of pressure,
    they couldn't feel tiredness nor the passage of time when they were together."

    show boy at left_center
    show girl at right_center
    show girl tired
    gc "sleep is for the losers! I haven't slept in a week and I'm totally fine."
    show boy panics
    bc "ummmm, ooook"
    show girl grins
    gc "In fact, I was reading a book about ..."
    show girl sleeps
    gc "Zzz..."
    show boy deeplook
    bc "psst, psst, you just fell asleep"
    gc "garbage collectors Zzz... Kubernetes config Zzz..."
    show boy panics
    bc "I guess this is normal :D"

    jump moonlight_scene


label walk_later:
    "The boy was busy coding, and the girl was running in the gym"

    "They probably went for a walk later, and had an interesting conversation"

    "and that's it"

    jump exit


label moonlight_scene:
    scene black

    "days passed..."

    "One late night, as they were walking, they decided to sit down on the grass and look at the bright moon."

    scene moonlight_prev at truecenter

    "the boy laid down"

    "the girl laid down too"

    show boy at left_center
    show girl at right_center
    show boy curious
    bs "Do you want to use my bag as a pillow?"
    show girl grins
    gs "LMAO, nope"
    show boy smallsmile
    gs "btw,..."
    show girl smallsmile

    "the boy look at her as she was talking."
    "he still clearly remembers what she was talking about as he was memorizing every movement of her lips."

    "in his head, he was wondering what was happening to him."

    "Something was different, something was off."

    "She looked back at him."

    "The boy looked at her eyes."

    "He wanted to know more about the mysterioy of those eyes."

    "Behind those glasses, behind her pupils, the boy wanted to see her soul."

    show girl grins
    gs "I'm really glad that I met you."
    show girl

    "the boy was still staring... with a quite voice he responded"

    show boy grinsopen
    bs "me too!"

    show boy deeplook

    scene moonlight at truecenter
    show boy at left_center
    show girl at right_center
    show boy deeplook

    "He thought he had put his heart in a cage and hid it somewhere deep inside so that no one can find it."

    "He thought he had forbod himself to get attached to anyone."

    "But somehow, those eyes..."

    "The boy was still confused about his emotions."

    "Was this a really good friendship? a potential work partner? or something more?"

    show boy grinsopen
    bs "yes! me too! I mean I met a lot of people this summer, but I don't think I can call any of them real friends."

    show boy grins
    bs "except for you."

    show girl grins
    gs "same with me. So many people I say hi to every day. So many people I say I'd miss,
        but then each of one of just go our own way and never see others again. You just forget they existed."

    show boy abouttocry

    bs "I don't want to forget you"

    show girl sadsurprised
    gs "I don't want to forget you either"

    "They had 10 more days. Each second passing by felt like one step closer to goodbye."

    "Suddenly the boy felt his world is collapsing."

    "He tried to be strong, pushing down the deep saddness that he was drowning in."

    show boy embarrasedangry

    bs "If it's strong enough, it'll find it's way through time and distance"

    # confused look
    gs "what do you mean?"

    show boy grinsopen
    bs "our friendship. it'll find it's way..."

    show girl curious
    gs "really?"

    bs "really! (with accent)"

    "they decided to remember that day by the code word mochi."

    "somehow in their brain the word embedding for mochi is associated with the moon, singing random songs on the street."

    bc "and also pain"
    gc "aww"
    bc "no I mean physical pain. my foot still hearts from that bad landing."
    gc "WHAT?"
    bc "It was two meters high. I couldn't walk for a week. I told everyone I fell when I was rock climbing."
    gc ":/"
    bc "grin"
    gc "mochi"
    bc "mochi! :D"

    jump last_day


label last_day:
    scene black

    "many days passed."

    "many memories formed that the boy could never forget."

    scene missing_bus at truecenter

    bc "for instance, we went for a one day trip. We happen to miss the bus for the first time in my life and that was really really exciting."
    gc "another I-will-kick-your-ass-if-you-interrupt-the-story again kinda look"
    bc "no seriously, I really enjoyed that trip. Especially,..."
    gc "WHAT?"
    bc "the mango cheese cake!"
    play sound "punch.mp3" volume 2.0
    bc "ouch ouch, stoooop."

    pause 1.0
    stop sound


    scene coding at truecenter

    "They even had a little hackethon..."

    gc "and we still haven't finished that project"
    bc "well..."
    gc "WHAT"
    bc "I'm still too scared to change your code. You know, historically speaking it has always resulted in physical and emotional damage!"
    gc ":/"
    bc "so I decided to write my own version with gradio and langchain."
    gc "WHAT DID YOU DO??!!"
    bc "I said ..."

    menu:
        "punches him":
            jump punches_him
        "kicks him":
            jump punches_him
        "slaps him":
            jump punches_him           
        "thanks him":
            jump thanks_him

label punches_him:
    play sound "punch.mp3"
    bc "ouch"
    bc "ok, ok, I actually haven't done that yet."
    jump after_punch_or_slap

label thanks_him:
    bc "ummm, ok."
    bc "so when I said I did that, I ment I'm planning to do it."
    jump after_punch_or_slap

label after_punch_or_slap:
    bc "...but I'll do it as soon as I find some time to sleep. :D"

    "cough cough, back to the story..."    

    scene last_day at truecenter

    "Like any other good thing in the world, this chapter also had to come to an end."

    "The boy was really scared now. Something had changed. Now he had something to lose."

    "He didn't want to let her go. He wanted to see those eyes again."

    "He wanted to watch that glimmer of hope and happiness in her eyes forever."

    "Is this the last time he's having a conversation with her?"


    show boy at left_center
    show girl at right_center
    show boy abouttocry
    show girl curious

    gs "so what was the thing that you didn't want to tell me."

    bs "oh I can't tell you, I'm sorry."

    gs "What? Whyyyyy? You promised to tell me." 
    
    bs "no I didn't."

    show girl frustrated
    gs "yes you did."

    bs "no I didn't."

    gs "arghhh, ok. Would you at least tell me in a month when I see you in a hackethon?"

    show boy curious
    bs "ummm, no. I don't think so."

    gs "ahhhh. at least tell me that second thing that you didn't want to tell me."

    "the boy thought in silence."

    show girl frustrated
    gs "WHAT!"

    show boy deeplook
    bs "ok, ok. you're ready?"

    gs "JUST TELL ME."

    show boy abouttocry
    bs "I cried two times in the last week."

    show girl curious

    gs "Why?"

    bs "well, last one was the tear of happiness."

    gs "oh! (not interested)."

    bs "but another one was the first time I cried in the office."

    show girl surprised
    gs "oh! (interested again)."

    show boy embarrasedangry
    bs "I just couldn't imagine you'd be gone in a week. I didn't want our friendship to be over."

    show boy abouttocry
    bs "I just met you. Why should all the good things in the world end so quickly."

    "silence"

    "more silence"

    "even more silence"

    show girl embarrased
    gs "I should tell you something"

    menu:
        "tells what her hearts says":
            jump confess
        "hides her emotions":
            show girl tired
            gs "I'm really tired. I need to go back home."
            show boy surprised
            bs "wait!"
            "they stared..."
            show boy abouttocry
            bs "I mean yes, you should go..."
            "They shook hands as always and said goodbye"
            jump exit

label confess:
    show boy abouttocry at left_center
    show girl emotional at right_center

    gs "I think"

    "silence"

    gs "I think I"

    "the boy silently looked at her for a one minute or two"

    show girl frustrated
    gs "never mind"

    show boy curious
    bs "no tell me. PLEASE"

    gs "I can't"

    bs "I'm really patient. I can wait here forever until you're ready"

    "the boy knew what she wanted to say"

    "the boy wanted to scream: I like you too"

    "that was the one thing he couldn't tell the girl"

    "He was just too scared to take any step. Not because of the fear of rejection"

    "But because he didn't know what would happen if she also likes her back."

    "He was very confused by his emotions..."

    "Minutes passed... each second felt like an hour"

    gs "I think I like you"

    "The boy's heart was beating really really fast"

    "as if his heart was trying to open the cage and fly out of his chest"

    "three words came out of his mouth. The three words that had been waiting there for such a long time..."

    show boy grinsopen
    bs "I like you too"
    show girl grins

    "and the rest is history..."

    pause 2.0

    scene fire_and_rose at truecenter with pixellate # change it to holding hands scene?

    stop music fadeout 1.0
    play music "music/all_I've_ever_known.mp3" fadein 1.0

    "They held each other's hands"

    "Her hands were warm. He felt a stream of energy flowing through their hands."

    "It was a pure and innoscent feeling. Like a little child."

    "they hugged"

    "For the first time the boy let himself fall."
    "For the first time he had all his gaurds down." 
    "For the first time he felt like he can let all his thoughts go away and just lose himself in the moment. The moment that every second of it felt like an eternity."

    "He felt warm, safe and secure. He had found her. Nothing else mattered anymore."

    "And that eternity finally ended, for a new chapter to begin..."

    jump the_gift


label the_gift:
    scene the_gift at truecenter

    play music "music/World_to_Paradise.mp3"

    "for his birthday the boy had the best gift ever"

    "the new life she had given him"

    "and also this song"

    "he could wear it like a jacket, to keep his heart warm whenever it gets cold"

    "and it did get cold, many times..."

    "but those sweet words kept him safe"

    show boy at truecenter with moveinbottom

    bc "I also wanted to give you a song"
    show boy deeplook
    bc "I tried so hard, but it wasn't as good as yours..."
    show boy grinsopen
    bc "so I decided to tell you a story"
    bc "the actual story is much much longer, and I could only tell an infinitesimally small fraction of it"
    bc "but this is not just the story of the past, but it's also for the future"
    bc "our future"
    bc "I wanted us to always remember us this way"
    bc "especially when it gets dark outside and our hope gets dimmer"
    
label final_question:
    bc "will you take my hands and help me write a bright future together?"

    menu:
        "yes!":
            jump the_beginning_of_the_end
        "no":
            show boy abouttocry
            bc "let me ask one more time"
            jump final_question


label the_beginning_of_the_end:
    scene the_beginning at truecenter

    pause 3.0

    show boy at truecenter with moveinbottom
    bc "psst, psst, it's me again"
    bc "as I was making this I had an idea..."
    bc "an LLM based story telling engine which is totally interactive"
    show boy grinsopen
    bc "like the story line is fixed but the user is a character of the story and interacts with others"
    bc "might be exciting to explore..."
    bc "I wish I had all the time in the world to make all those ideas happen"
    show boy
    bc "or maybe I would use all that time to tell you how much I like you :D"
    pause
    return

return

label exit:
    scene night_sky at truecenter

    "years passed"

    "they both persued their dreams"

    "and worked hard"

    "and changed the world"

    "and they met each other one day,"

    "when they were shining brightly among the stars"

    scene the_end
    return
