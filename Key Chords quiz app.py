import random
import time
import threading
#Each chord and their correct answers
key_C = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C']
key_Cs = ['C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#']
key_Df = ['Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db']
key_D = ['D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D']
key_Ds = ['D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#']
key_E = ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E']
key_F = ['F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F']
key_Fs = ['F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#']
key_Gf = ['Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb']
key_G = ['G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G']
key_Gs = ['G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
key_A = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A']
key_As = ['A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#']
key_Bf = ['Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb']
key_B = ['B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

#Currently inactive save state to save your best score
bestincorrect = None

def startup():
    print("Welcome to the Key Cords Quiz")
    print("Keep in mind that accidentals as answers will always count as sharp(#) by default unless the key is a flat(b)")
    print("This quiz is case sensitive, enter all of your answers with capital letters, and use lowercase b to indicate flats")
    cont = input("Press Enter to continue")
    return cont

def quiz_setup():
    key = random.randint(1, 15)
    if key == 1:
        key = key_C
        k = 'C'
    elif key == 2:
        key = key_Cs
        k = 'C#'
    elif key == 3:
        key = key_Df
        k = 'Db'
    elif key == 4:
        key = key_D
        k = 'D'
    elif key == 5:
        key = key_Ds
        k = 'D#'
    elif key == 6:
        key = key_E
        k = 'E'
    elif key == 7:
        key = key_F
        k = 'F'
    elif key == 8:
        key = key_Fs
        k = 'F#'
    elif key == 9:
        key = key_Gf
        k = 'Gb'
    elif key == 10:
        key = key_G
        k = 'G'
    elif key == 11:
        key = key_Gs
        k = 'G#'
    elif key == 12:
        key = key_A
        k = 'A'
    elif key == 13:
        key = key_As
        k = 'A#'
    elif key == 14:
        key = key_Bf
        k = 'Bb'
    elif key == 15:
        key = key_B
        k = 'B'
    first = key[0]
    second = key[2]
    third = key[4]
    fourth = key[5]
    fifth = key[7]
    sixth = key[9]
    seventh = key[11]
    misc = [key[1], key[3], key[6], key[8], key[10]]
    correct1 = first
    correct2 = second
    correct3 = third
    correct4 = fourth
    correct5 = fifth
    correct6 = sixth
    correct7 = seventh
    print(f"\nThe key for this quiz is the key of {k}\n")
    return k, key, first, second, third, fourth, fifth, sixth, seventh, misc, correct1, correct2, correct3, correct4, correct5, correct6, correct7

def quiz():
    quiz_key = [first, second, third, fourth, fifth, sixth, seventh]
    random.shuffle(quiz_key)
    n = None
    totalincorrect = {}
    for i in quiz_key:
        wrong = 0
        if i == first:
            n = '1st'
        if i == second:
            n = '2nd'
        if i == third:
            n = '3rd'
        if i == fourth:
            n = '4th'
        if i == fifth:
            n = '5th'
        if i == sixth:
            n = '6th'
        if i == seventh:
            n = '7th'
        #Where the magic happens
        guess = input(f"What is the {n} note in the key of {k}? ")
        if guess != i:
            while guess != i:
                wrong = incorrect(guess, wrong)
                time.sleep(1)
                guess = input(f"What is the {n} note in the key of {k}? ")
        print("Correct.")
        totalincorrect[n] = wrong
        time.sleep(1)
    return totalincorrect
    
def incorrect(x, wrong):
    if x == first:
        print("Incorrect, that's the first note of this key. Try again.\n")
        wrong += 1
    elif x == second:
        print("Incorrect, that's the second note of this key. Try again.\n")
        wrong += 1
    elif x == third:
        print("Incorrect, that's the third note of this key. Try again.\n")
        wrong += 1
    elif x == fourth:
        print("Incorrect, that's the fourth note of this key. Try again.\n")
        wrong += 1
    elif x == fifth:
        print("Incorrect, that's the fifth note of this key. Try again.\n")
        wrong += 1
    elif x == sixth:
        print("Incorrect, that's the sixth note of this key. Try again.\n")
        wrong += 1
    elif x == seventh:
        print("Incorrect, that's the seventh note of this key. Try again.\n")
        wrong += 1
    else:
        for i in misc:
            if x == i:
                print("Incorrect, you don't even play that note in this key. Try again.\n")
                return wrong
        if x == 'E#' or x == 'Fb' or x == 'B#' or x == 'Cb':
            print("Notes that don't exist are E#/Fb and B#/Cb.\n")
        elif x == '':
            print("C'mon man, you gotta enter something.")
        else:
            print("Invalid input, make sure your answer is a capital letter from A-G, with # if necessary (unless the key is a flat, which you put b)\n")
    return wrong


def results():
    print(f"You correctly guessed all the notes in the key of {k}")
    total = 0
    for v, value in totalincorrect.items():
        print(f"You had {value} incorrect attempts on guessing the {v} note.")
        total += value
        time.sleep(1)
    print(f"In total, you had guessed the incorrect note {total} times.\n")
    time.sleep(1)
    """
    #Saving your best results to your device (not implemented yet)
    if totalincorrect < bestincorrect:
        print("That was the least incorrect guesses you've ever had!")
        bestincorrect = totalincorrect (this would be saved in a file for future attempts)
    """
    return total
#Main loop
cont = startup()
while cont == "":
    wrong = 0
    k, key, first, second, third, fourth, fifth, sixth, seventh, misc, correct1, correct2, correct3, correct4, correct5, correct6, correct7 = quiz_setup()
    time.sleep(2)
    totalincorrect = quiz()
    total = results()
    cont = input("Would you like to go again for better results? (Press Enter to try again, fill in anything then Enter to quit out)")
