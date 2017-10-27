def main():
    print("A Story about a Dead man: A Choose your own Adventure")
    print("\nYou have just awoken in the brig of a ship in 1657; the last thing you remember is fighting aboard\n"
          "the black jewel, your pirate ship you run with a crew of a hundred. Many men fear you across the seven\n"
          "seas. You were sailing on your normal route to the caribbean returning from stealing british imports from\n"
          "the colonies up in North America when suddenly, an enemy ship attacked. It was a large british battle ship\n"
          ",which made no sense how they found you until your second mate pulled his gun on you. Calico Jack\n"
          "the second most feared pirate, cut a deal with the british. After trying to fight the battle ship, You \n"
          "realize you had no chance against the greatest army in\n"
          "the world so for the sake of your men you surrendered and vowed Calico Jack you would hunt him for as long \n"
          "as you live. You are in the brig rotting until you get transferred to a maximum security prison in london;\n"
          "news has already spread of your capture and the Dread Pirate Roberts name is beginning to lose its legacy\n"
          "\n1. you try to escape by stealing the keys from the guard sleeping in front of you\n"
          "\n2. you pretend to fake an injury and battle the guards who come to help\n"
          "\n3. you attempt to pick the lock on you cell door")
    choice = int(input())
    if choice == 1:
        escape1()
    elif choice == 2:
        escape2()
    elif choice == 3:
        escape3()
    else:
        print("Error invalid choice")
        main()


def escape1():
    print("you can hardly reach the keys but manage to take them out of the guards pocket\n"
          "you begin to start checking all the keys in the key ring on the door when, the other\n"
          "guards begin call yours up for a shift change"
          "\n1. you keep guessing keys"
          "\n2. you panic and put the keys back")
    choice = int(input())
    if choice == 1:
        guess1()
    elif choice == 2:
        panic1()
    else:
        print("Error invalid choice")
        escape1()


def escape2():
    print("the guard outside your cell wakes up and come into help and is completely surprised when you jump off the \n"
          "floor and attack him. The guard has been knocked out and the cell door is open. Then, you put on the \n"
          "guards clothes and proceed out of the cell door "
          "\n Where do you go now?"
          "\n1. You try and find the captain quarters to take him out first"
          "\n2. You look around the brig to try and find your belongings")
    choice = int(input())
    if choice == 1:
        infiltrate1()
    elif choice == 2:
        belongings1()
    else:
        print("Error invalid choice")
        escape2()


def escape3():
    print("you pick the lock easily and the guard in front of you is still sleeping. After sneaking past the guard\n"
          "you then go to"
          "\n1. You try and find the captain quarters to take him out first"
          "\n2. You look around the brig to try and find your belongings")
    choice = int(input())
    if choice == 1:
        infiltrate1()
    elif choice == 2:
        belongings1()
    else:
        print("Error invalid choice")
        escape3()


def guess1():
    print("you guess the right key after many tries but the guards replacement comes down sooner than expected \n"
          "you then grab the sword from the sleeping guard and move on to fighting the other guards that come your \n"
          " way. Then, you "
          "\n1. let the other prisoners loose to assist in the take over"
          "\n2. keep fighting guards until there are not any left")
    choice = int(input())
    if choice == 1:
        prisoners()
    elif choice == 2:
        fight()
    else:
        print("Error invalid choice")
        guess1()


def infiltrate1():
    print("you slowly creep around the ship looking for the captain's quarters when you see it with many \n"
          "guards and crewman surrounding it. Since you have a guards uniform on you proceed to get closer to the \n"
          "captain's quarters and you see the captain sitting in the captain's chair when you suddenly remember him\n"
          "from when you were captured. You overhear from some of the crewman that they will be stopping for \n"
          "supplies down in the virgin islands in 4 hours"
          "\n You"
          "\n1. Continue to try and kill the captain"
          "\n2. go hide until you dock in the islands then try to escape")
    choice = int(input())
    if choice == 1:
        captain2()
    elif choice == 2:
        hide()
    else:
        print("Error invalid choice")
        infiltrate1()


def belongings1():
    print("you look around the brig and find your belongings however, 3 guards come down and find the open cell\n"
          "they then alert the rest of the ship you are loose and all the guards are on high alert\n"
          "you"
          "\n1. Try and open the other cell doors for the other prisoners assistance"
          "\n2. you run around the ship looking for a place to hide ")
    choice = int(input())
    if choice == 1:
        prisoners()
    elif choice == 2:
        hide()
    else:
        print("Error invalid choice")
        belongings1()


def panic1():
    print("You are still stuck in the cell\n"
          "What do you do"
          "\n1. steal the guards keys for the door"
          "\n2. try and pick the lock")
    choice = int(input())
    if choice == 1:
        guess1()
    elif choice == 2:
        escape3()
    else:
        print("Error invalid choice")
        panic1()


def prisoners():
    print("You decide to help the other prisoners out in an attempt to take over the ship. None of them have weapons\n "
          "and the guards have now realized all the prisoners are gone. But you decide to fight anyway and the army\n "
          "of prisoners takes out all the guards except for the captain who surrenders.\n"
          "Being the leader of the army you decide if the captain lives or dies\n"
          "\n1. lives"
          "\n2. dies ")
    choice = int(input())
    if choice == 1:
        spare()
    elif choice == 2:
        murder()
    else:
        print("Error invalid choice")
        prisoners()


def hide():
    print("You feel the ship pull into dock and realize that you cannot escape without being seen. \n"
          "\n Do You "
          "\n1. make a break for it and run"
          "\n2. Wait even longer until it is dark"
          "\n3. go back and kill the captain ")
    choice = int(input())
    if choice == 1:
        run()
    elif choice == 2:
        wait()
    elif choice == 3:
        captain2()
    else:
        print("Error invalid choice")
        hide()


def run():
    print("You choose to go for it and you make it about 2 feet off the ship before being blasted by rifles\n"
          "\nGAME OVER"
          "\n1. Retry")
    choice = int(input())
    if choice == 1:
        hide()
    else:
        print("Error invalid choice")
        run()


def wait():
    print("As you are waiting for time to run out and the sun to go down you overhear some crewman\n"
          " Talking about the massive loot they are putting on the ship while they are docked here at the islands\n"
          " stored in the hull of the ship\n"
          "Do You\n"
          "\n1. Loot the treasure risking freedom for fame"
          "\n2. wait a little longer and get out while you can")
    choice = int(input())
    if choice == 1:
        loot()
    elif choice == 2:
        wait2()
    else:
        print("Error invalid choice")
        wait()


def wait2():
    print("The sun has gone down and you decide to make your move. You safely escape the ship undetected a poor man.\n"
          "You find your way around the islands and make your way over to Puerto Rico with a new name\n"
          "in fear of being hunted by the british noone knows who you are and the Dread Pirate roberts is dead\n"
          "\n You Lose")


def loot():
    print("You decide to risk it all and go for the treasure. You make your way to where the treasure \n"
          "was rumored to be and you take as much as you can carry off the ship. Then you steal a small boat and sail\n"
          "to Puerto Rico to live out your days as the richest Dead Man alive\n"
          "\nYOU WIN!!!! ")


def fight():
    print("there are too many guards for even you to handle and you die\n"
          "GAME OVER"
          "\n1. retry")
    choice = int(input())
    if choice == 1:
        guess1()
    else:
        print("Error invalid choice")
        fight()


def captain2():
    print("You make your way to the captain's quarters and surprise attack him\n "
          "killing him in front of his whole crew.\n"
          " The rest of the crew are stunned and accept you as their new captain. And the crew who does not\n "
          "are executed. The ship is now yours and the dread Pirate Roberts legacy continues\n"
          "\n YOU WIN!!")


def spare():
    print("the captain has been spared however, he would rather die than see you take over his ship\n"
          "so the captain lights a fuse that leads to the artillery blowing up the whole ship killing everyone\n"
          "\n1. retry")
    choice = int(input())
    if choice == 1:
        prisoners()
    else:
        print("Error invalid choice")
        spare()


def murder():
    print("You murder the captain in cold blood making the ship now yours to rule the seven seas once again\n"
          "\n YOU WIN!!")


main()