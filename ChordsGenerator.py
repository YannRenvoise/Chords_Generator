# A Chords generator in Python

#--------- Change Log ----------#
# 23.03.2025   Created 0.1 (operational: keys/some tonic and non-tonic progressions/ the chromatic scales)
#
# Copyright (c) 2025-2030 by Yann Renvoisé.  All rights reserved.

import random
import time

# Variables
key_used = "" # the main key we play in
your_scale = [] # all the chords in the scale
your_progression_name = [] # the 'name" of the progression, which is the dictionary's key
your_progression = [] # the actual progression
your_chords = [] # the base chords if we follow the progression

# Lists and Dictionaries
ALL_KEYS = ("C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B")
all_major_progression = ("I", "ii", "iii", "IV", "V", "vi", "vii°")
all_minor_progression = ("i", "ii°", "III", "iv", "v", "VI", "VII")
progression_dictionary = {"I":1, "ii":2, "iii":3, "IV":4, "V":5, "vi":6, "vii°":7, "i":1, "ii°":2, "III":3, "iv":4, "v":5, "VI":6, "VII":7}

major_scales = {
    "C": ["C", "Dm", "Em", "F", "G", "Am", "Bdim"],
    "G": ["G", "Am", "Bm", "C", "D", "Em", "F#dim"],
    "D": ["D", "Em", "F#m", "G", "A", "Bm", "C#dim"],
    "A": ["A", "Bm", "C#m", "D", "E", "F#m", "G#dim"],
    "E": ["E", "F#m", "G#m", "A", "B", "C#m", "D#dim"],
    "B": ["B", "C#m", "D#m", "E", "F#", "G#m", "A#dim"],
    "F#": ["F#", "G#m", "A#m", "B", "C#", "D#m", "E#dim"],
    "C#": ["C#", "D#m", "E#m", "F#", "G#", "A#m", "B#dim"],
    "F": ["F", "Gm", "Am", "A#", "C", "Dm", "Edim"],
    "A#": ["A#", "Cm", "Dm", "D#", "F", "Gm", "Adim"],
    "D#": ["D#", "Fm", "Gm", "G#", "A#", "Cm", "Ddim"],
    "G#": ["G#", "A#m", "Cm", "C#", "D#", "Fm", "Gdim"],
    "C#": ["C#", "D#m", "Fm", "F#", "G#", "A#m", "Cdim"],
    "F#": ["F#", "G#m", "A#m", "B", "C#", "D#m", "Fdim"],
    "B#": ["B#", "C#m", "D#m", "E#", "F#", "G#m", "A#dim"],
}

minor_scales = {
    "A": ["Am", "Bdim", "C", "Dm", "Em", "F", "G"],
    "E": ["Em", "F#dim", "G", "Am", "Bm", "C", "D"],
    "B": ["Bm", "C#dim", "D", "Em", "F#m", "G", "A"],
    "F#": ["F#m", "G#dim", "A", "Bm", "C#m", "D", "E"],
    "C#": ["C#m", "D#dim", "E", "F#m", "G#m", "A", "B"],
    "G#": ["G#m", "A#dim", "B", "C#m", "D#m", "E", "F#"],
    "D#": ["D#m", "E#dim", "F#", "G#m", "A#m", "B", "C#"],
    "A#": ["A#m", "B#dim", "C#", "D#m", "E#m", "F#", "G#"],
    "D": ["Dm", "Edim", "F", "Gm", "Am", "A#", "C"],
    "G": ["Gm", "Adim", "A#", "Cm", "Dm", "D#", "F"],
    "C": ["Cm", "Ddim", "D#", "Fm", "Gm", "G#", "A#"],
    "F": ["Fm", "Gdim", "G#", "A#m", "Cm", "C#", "D#"],
    "A#": ["A#m", "Cdim", "C#", "D#m", "Fm", "F#", "G#"],
    "D#": ["D#m", "Fdim", "F#", "G#m", "A#m", "B", "C#"],
    "G#": ["G#m", "A#dim", "B", "C#m", "D#m", "E#", "F#"],
}

major_progressions = {
    "Classic Pop": ["I", "V", "vi", "IV"],
    "Rock Ballad": ["I", "IV", "V", "I"],
    "Blues Standard": ["I", "IV", "I", "V", "IV", "I"],
    "Jazz Turnaround": ["I", "vi", "ii", "V"],
    "Upbeat Folk": ["I", "V", "vi", "iii", "IV"],
    "Catchy Pop": ["I", "IV", "vi", "V"],
    "Folk Revival": ["I", "V", "vi", "iii", "IV", "I"],
    "Classic Country": ["I", "IV", "V", "I", "vi", "IV"],
    "Modern Pop": ["I", "vi", "IV", "V", "I"],
    "Bright Jazz": ["I", "II", "V", "I"],
    "Swing Blues": ["I", "IV", "V", "IV", "I"],
    "Happy Bounce": ["I", "vi", "IV", "V"],
    "Upbeat Indie": ["IV", "V", "I", "vi"],
    "Contemporary Pop": ["I", "V", "IV", "vi"],
    "Cinematic Anthem": ["I", "IV", "V", "vi", "IV"],
    "Retro Funk": ["I", "IV", "vi", "ii", "V"],
    "Indie Pop": ["I", "ii", "V", "IV", "vi"],
    "Soul Groove": ["I", "IV", "V", "vi", "IV"],
    "Dynamic Pop": ["I", "IV", "V", "vi", "ii"]
}

minor_progressions = {
    "Melancholic Ballad": ["i", "VI", "III", "VII"],
    "Dramatic Cinematic": ["i", "iv", "v", "i"],
    "Dark Rock": ["i", "VII", "VI", "V"],
    "Suspenseful": ["i", "ii°", "V", "i"],
    "Latin Dance": ["i", "iv", "V", "i"],
    "Mournful Jazz": ["i", "VII", "VI", "VII", "i"],
    "Gothic Metal": ["i", "VI", "VII", "iv", "i"],
    "Emotional Pop": ["i", "iv", "VII", "i"],
    "Epic Soundtrack": ["i", "iv", "V", "VI", "VII", "i"],
    "Mysterious": ["i", "ii°", "iv", "v", "i"],
    "Cinematic Horror": ["i", "VI", "iv", "VII", "i"],
    "Sad Blues": ["i", "v", "i", "iv"],
    "Gothic Ballad": ["i", "VI", "iv", "VII", "i"],
    "Dark Jazz": ["i", "VII", "v", "i"],
    "Cinematic Tension": ["i", "iv", "VII", "VI", "i"],
    "Doom Metal": ["i", "VII", "VI", "v", "i"],
    "Grief-stricken": ["i", "VI", "iv", "V", "i"],
    "Chilling Drama": ["i", "VII", "v", "ii°", "i"],
    "Bleak Soundtrack": ["i", "iv", "VI", "VII", "i"],
    "Lamenting Soul": ["i", "VI", "v", "iv", "i"],
    "Cinematic Epic": ["i", "VII", "VI", "iv", "i"]
}

non_tonic_major_progressions = {
    "Majestic Modulation": ["IV", "V", "I", "vi"],
    "Dreamy Jazz": ["ii", "V", "I", "vi"],
    "Bluesy Rock": ["V", "IV", "I", "V"],
    "Soft Soul": ["vi", "ii", "V", "I"],
    "R&B Groove": ["IV", "vi", "V", "I"],
    "Chill Pop": ["ii", "IV", "V", "I"],
    "Funky Feel": ["IV", "V", "vi", "I"],
    "Latin Jazz": ["V", "I", "IV", "ii"],
    "Cinematic Drama": ["IV", "I", "V", "vi"],
    "Lush Ballad": ["ii", "V", "I", "IV"],
    "Suspenseful Build": ["vi", "IV", "ii", "V"],
    "Anthemic Rock": ["IV", "V", "vi", "iii"],
    "Epic Progression": ["V", "IV", "vi", "I"],
    "Expressive Jazz": ["ii", "V", "I", "vi", "IV"],
    "Uplifting Pop": ["vi", "V", "IV", "I"],
    "Dramatic Swing": ["V", "vi", "ii", "I"],
    "Emotional Film Score": ["IV", "vi", "V", "ii", "I"],
    "Laid-Back Groove": ["ii", "IV", "vi", "V"],
    "Modern Indie": ["vi", "ii", "V", "IV"],
    "Soulful Ballad": ["IV", "vi", "V", "ii", "I"],
}

non_tonic_minor_progressions = {
    "Dark Waltz": ["iv", "v", "i", "VI"],
    "Tense Thriller": ["ii°", "v", "i", "VII"],
    "Gothic Drama": ["VI", "iv", "v", "i"],
    "Mystical Jazz": ["iv", "VII", "i", "V"],
    "Doom Metal": ["VII", "VI", "v", "i"],
    "Haunting Soundtrack": ["v", "i", "iv", "VI"],
    "Mysterious Vibes": ["iv", "VI", "VII", "i"],
    "Tearful Ballad": ["VI", "v", "i", "VII"],
    "Folk Lament": ["VII", "iv", "v", "i"],
    "Deep Blues": ["v", "VII", "i", "iv"],
    "Cinematic Tension": ["VI", "ii°", "v", "i"],
    "Emotional Solo": ["iv", "VI", "VII", "v", "i"],
    "Horror Theme": ["VII", "v", "VI", "i"],
    "Epic Chase": ["v", "i", "VII", "iv"],
    "Suspense Build": ["VI", "v", "iv", "i"],
    "Sad Reflection": ["VII", "VI", "v", "iv", "i"],
    "Shadowy Ambiance": ["v", "iv", "VII", "i"],
    "Chilling Descent": ["VI", "VII", "iv", "v", "i"],
    "Wistful Longing": ["iv", "VII", "VI", "v", "i"],
    "Melancholic Journey": ["VII", "VI", "v", "i", "iv"],
}

# Start of the program

while True:

    # Whe choose (or not) the mood
    while True:
        mood_choice = input("Do you want a Major or minor progression? (Major/minor/either): ").strip().lower()
        if mood_choice:  # If it's not empty, continue
            if mood_choice in ["major", "minor", "either"]: # If it's a good answer, continue
                    break
            else:
                print("It has to be one of the intended choice !")
        else:
            print("Oops! You must enter something!")
        
    if mood_choice == "either":
        mood_choice = random.choice(["major","minor"])

    # Whe choose (or not) the key
    while True:
        key_choice = input("Do you want to choose the key? (yes/no): ").strip().lower()
        if key_choice:  # If it's not empty, continue
            if key_choice in ["yes", "no"]: # If it's a good answer, continue
                    break
            else:
                print("It has to be one of the intended choice !")
        else:
            print("Oops! You must enter something!")

    if key_choice == "no":
        key_used = random.choice(ALL_KEYS)
    else:
        while True:
            key_used = input(f"Choose the key you want in {ALL_KEYS}: ").strip().upper() # !!! use .upper() to get the right key
            if key_used:  # If it's not empty, continue
                if key_used in ALL_KEYS: # If it's a good answer, continue
                    break
                else:
                    print("It has to be one of the intended choice !")
            else:
                print("Oops! You must enter something!")

    # Whe choose (or not) if the progression starts with the tonic
    while True:
        tonic_choice = input("Do you want the progression to start with the tonic (yes/no/either): ").strip().lower()
        if tonic_choice:  # If it's not empty, continue
            if tonic_choice in ["yes", "no", "either"]: # If it's a good answer, continue
                    break
            else:
                print("It has to be one of the intended choice !")
        else:
            print("Oops! You must enter something!")

    if tonic_choice == "either":
        tonic_choice = random.choice(["yes","no"])


    # Algorithm
    if mood_choice == "major":
        your_scale = major_scales.get(key_used)
        if tonic_choice == "yes":
            your_progression_name = random.choice(list(major_progressions.keys()))
        else:
            your_progression_name = random.choice(list(non_tonic_major_progressions.keys()))
    else:
        your_scale = minor_scales.get(key_used)
        if tonic_choice == "yes":
            your_progression_name = random.choice(list(minor_progressions.keys()))
        else:
            your_progression_name = random.choice(list(non_tonic_minor_progressions.keys()))

    if your_progression_name in major_progressions:
        your_progression = major_progressions.get(your_progression_name)
    elif your_progression_name in minor_progressions:
        your_progression = minor_progressions.get(your_progression_name)
    elif your_progression_name in non_tonic_major_progressions:
        your_progression = non_tonic_major_progressions.get(your_progression_name)
    else:
        your_progression = non_tonic_minor_progressions.get(your_progression_name)


    for step in your_progression:
        if mood_choice == "major":
            your_chords.append(major_scales.get(key_used)[int(progression_dictionary.get(step)-1)]) # we make sure to start at 0
        if mood_choice == "minor":
            your_chords.append(minor_scales.get(key_used)[int(progression_dictionary.get(step)-1)]) # we make sure to start at 0
    
    time.sleep(1)
    print()
    print("---------- Results ----------")
    print()
    time.sleep(1)
    print(f"So you will do a {mood_choice.capitalize()} progression in the key of {key_used} !")
    print()
    time.sleep(1)
    print(f"Your scale is: {your_scale}")
    print(f"Your progression is: {your_progression_name} |", end= " ")
    print(your_progression)
    print()
    time.sleep(1)
    print(f"Therefore, your default chords will be: ", end="")
    time.sleep(1) 
    print(f"{your_chords} !")
    time.sleep(1) 
    print("Good practice !")
    print()
    time.sleep(1) 
    print("---------- End ----------")
    print()
    time.sleep(1) 

    # Do again
    while True :
        answer = input(f"Do you want another set of chords ? Y/N : ").strip().lower()
        if answer in ["y","n"]:
             break
        print(f"No, you have to answer by either Y (for Yes) or N (for No) ...")

    if answer == "n":
        print("Alright, see you soon !")
        break
        
    print("Okay ! Let's restart !")