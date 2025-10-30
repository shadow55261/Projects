print(""" Welcome to the haunted library game😈👻
─────█─▄▀█──█▀▄─█─────
────▐▌──────────▐▌────
────█▌▀▄──▄▄──▄▀▐█────
───▐██──▀▀──▀▀──██▌───
──▄████▄──▐▌──▄████▄──

""")
game=input("Start the game yes, no\n").lower()
if game=="yes":
    print("Now you are inside a dark Old Library, and the doors" \
" are locked. To get out you" \
" have to solve puzzles either " \
"to survive...Or for a trap 😈 👻 ")
elif game=="no":
   print("Try it later in our time👋👋👋")
else:
   print("Sorry, your choice is incomprehensible🤷‍♂️🤷‍♂️🤷‍♂️")
game1=input("""Head to the library in the room you have three 
shelves in the library shelf (A) you find a 📕book،
Shelf (B) where you find a roll📜
Shelf (C) where you find a ghost asking you,
ask if you answered wrong, the doors close!😱😱😱
""")
if game1.upper()=="A":
    print("Good, now open the book and solve the mystery")
    soul=input("""I am not alive... yet I move at night
        I dwell inshadows and vanish in the light
        I have no soul, yet I follow your sight
        What am I?\n""")
    if soul.lower()=="shadow":
        print("Congratulations, he got the key 🔑"
         "and finished the haunted library 🎉 🎉 🎉 ")  
    else:
        print("The answer you entered is wrong❌❌❌" \
        "You will be locked in the haunted library forever")
if game1.upper()=="B":
    print("""The contents of the scroll📜 two doors are waiting
    for you at the end of this corridor...One guards the 
    flame that has been extinguished , the other hides the 
    eyes that do not sleep light or darkness...Choose your 
    destiny""")
    scroll=input("""Choose your fate, from which there is no escape,
            ither to injure or disappoint, decide which of the
            two doors you will choose the door 🚪(D) Or 
            the door🚪 (S)\n""")
    if scroll.upper()=="S":
            print("""You've lost the game, you've made a mistake, 
            you've been captured by the creepy entity that 
            owns the haunted library😈😈😈💀""")
    elif scroll.upper()=="D":
            print("""Excellent, good choice, you have chosen the right way,
            take the lamp in the room 🔦 and make your way to the exit
            and escape""")
    else:
            print("Sorry your choice is unknown🤷‍♂️🤷‍♂️🤷‍♂️")
if game1.upper()=="C":
        print("You have freed the ghost 👻" \
        "you must answer his questions to survive"
        " or you will be locked up forever 😱 😱 😱 ")
        forever=input("I am the end of every road...And " \
            "the beginning of every sleep, Who Am I?😈👻\n")
        if forever.lower()=="death":
            print("Now you can run away and wake yourself up🏃‍♂️🏃‍♂️🏃‍♂️")
        else:
            print("The ghost will dress you with a curse all the time"
            " and lock you up forever in the haunted library☠️☠️☠️")     