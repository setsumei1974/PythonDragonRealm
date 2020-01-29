import random
import time

def displayIntro():
    print("""You have arrived in the Kingdom of Dragons.  You perceive before you,
    bathed in the light of day, the entrances to two mysterious caves.  One cave hides
    a noble dragon, who will grant you wisdom and treasure, while the other cave houses
    an evil dragon, lean and hungry, who will devour you at first sight.""")
    print()

def chooseCave():
    cave = ""
    while cave != "1" and cave != "2":
        print("Which cave shall you choose? (1 or 2)")
        cave = input()
    return cave

def checkCave(chosenCave):
    print("You approach the entrance to the cave . . .")
    time.sleep(2)
    print("A gloomy darkness begins to envelop you . . .")
    time.sleep(2)
    print("A dragon appears in front of you.  He opens his jaws, and you behold rows of shimmering teeth . . .")
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print("He gives you his treasure!")
    else:
        print("He devours you in one bite!")

playAgain = "Yes"
while playAgain == "Yes":
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print("Do you wish to play again? (Yes or No)")
    playAgain = input()