print('''                                                 
▄     ▄ ▄▄▄▄▄▄ ▄        ▄▄▄   ▄▄▄▄  ▄    ▄ ▄▄▄▄▄▄
█  █  █ █      █      ▄▀   ▀ ▄▀  ▀▄ ██  ██ █     
▀ █▀█ █ █▄▄▄▄▄ █      █      █    █ █ ██ █ █▄▄▄▄▄
 ██ ██▀ █      █      █      █    █ █ ▀▀ █ █     
 █   █  █▄▄▄▄▄ █▄▄▄▄▄  ▀▄▄▄▀  █▄▄█  █    █ █▄▄▄▄▄
                                                 
                                                 ''')
print('''                                                                             
▄▄▄▄▄▄▄  ▄▄▄▄        ▄▄▄▄▄▄▄ ▄▄▄▄▄  ▄▄▄▄▄▄   ▄▄    ▄▄▄▄  ▄    ▄ ▄▄▄▄▄  ▄▄▄▄▄▄
   █    ▄▀  ▀▄          █    █   ▀█ █        ██   █▀   ▀ █    █ █   ▀█ █     
   █    █    █          █    █▄▄▄▄▀ █▄▄▄▄▄  █  █  ▀█▄▄▄  █    █ █▄▄▄▄▀ █▄▄▄▄▄
   █    █    █          █    █   ▀▄ █       █▄▄█      ▀█ █    █ █   ▀▄ █     
   █     █▄▄█           █    █    ▀ █▄▄▄▄▄ █    █ ▀▄▄▄█▀ ▀▄▄▄▄▀ █    ▀ █▄▄▄▄▄
                                                                             
                                                                             ''')
print('''                                                 
 ▄▄▄▄▄   ▄▄▄▄  ▄        ▄▄   ▄▄   ▄ ▄▄▄▄     ▄   
   █    █▀   ▀ █        ██   █▀▄  █ █   ▀▄   █   
   █    ▀█▄▄▄  █       █  █  █ █▄ █ █    █   █   
   █        ▀█ █       █▄▄█  █  █ █ █    █   ▀   
 ▄▄█▄▄  ▀▄▄▄█▀ █▄▄▄▄▄ █    █ █   ██ █▄▄▄▀    █   
                                                 
                                                 ''')
choice1 = input("Now, do you want to go \"L\" or \"R\"?\n").lower()
if choice1 == "l":
    print("You walked right into a pit of spikes. You died. Game over.")
elif choice1 == "r":
    choice2 = input("Smart choice. You cross the Valley of Eternity and come across a horde of killer bears. \"Fight\" or \"play dead\"?\n").lower()
    if choice2 == "fight":
        print("Serisouly? You thought that you could take on a horde of killer bears? You don't even have a weapon. You died. Game over.")
    elif choice2 == "play dead":
        choice3 = input("The bears see you being stupid and leave you alone, as to not rub your stupidity on themselves. Once they leave, you come to a castle with a moat. \"Swim\" or \"yell\"?\n").lower()
        if choice3 == "swim":
            choice4 = input("Wow, you found a secret portal that teleports you directly to the treasure. But there is another adventurer there. Do you \"share\" the riches or \"fight\" for it?\n").lower()
            if choice4 == "share":
                print("You win! You found the treasure and shared it with another adventurer. You are a true hero.")
            elif choice4 == "fight":
                print("You suck at fighting and died. Game over.")
        elif choice3 == "yell":
            print("You yelled so loud that you woke up the dragon that was sleeping in the castle. The dragon eats you. Game over.")
else:
    print("That is not a valid choice. The Gods smite you. Game over.")            