#count = 0  # Survival count needs to be implemented in all definitions
#inventory = ""
# All Story related texts have to be in seperate def function()
# This in order to not repeat unwanted text and only repeat 'count and questions + if-solutions'
# 'count and questions + if-solutions' have to be able to get called seperately ('in def function()')
# Calling needs to be more precise depending on importance of function
def Firstscene():
    userInput1 = input("What do you do? a) Walk out of room b) Stay in room ( <enter> a) or b) )\n:")
    # graphics
    if userInput1 == "a)":  # Solution Path!
        WalkoutRoom()
    elif userInput1 == "b)":  # Will return to Walkoutroom()
        StayinRoom()
def StayinRoom():   # Go back to the Firstscene()
        print("no one coming return to door")
        Firstscene()

def WalkoutRoom():#solution path
    userInput2 = input("The corona Zombie is coming for u, What do you do(A = fight, B = Run, C = Lock door)\n:")
    if userInput2 == "A":
        FightZombie()
    elif userInput2 == "B":
        RunAwayZombie()
    elif userInput == "C":
        WalkoutRoom()  # has to include text so maybe make seperate TextPart function = 1 more step
def FightZombie():  # graphics with objects
    userInput3 = input("Which of the objects could help you? ( A)Crutches, B)Wheelchair, C)Gun )\n:")
    if userInput3 == "Crutches":  # put to inventory
        print("You pick up crutches and want to use them but how?")
        userInput5 = input("How u wanna use crutch?(A = Hit, B = Use)")
        Inventory = Inventory + "Crutch"
        if userInput5 == "Hit":
            print("big fight but no effect")
            RunAwayZombie()
        elif userInput5 == "Use":
            print("kick had no effect on the corona zombie")
            RunAwayZombie()  # going back to
    elif userInput3 == "Wheelchair":  # put to inventory
        Inventory = Inventory + "Wheelchair"
        print("You tried to take advantage of the wheelchair but no effect on zombie")
        WalkoutRoom()
    elif userInput3 == "Gun":  # put to inventory
        print("Tricky ToyGun is no helping")
        WalkoutRoom()

def RunAwayZombie():
    userInput4 = input("txt")
    if userInput4 == "Right":
        if Inventory == "Crutches":
            print("you can defend yourself with your crutches")  # here no count
            print("txt")
            userInput6 = input("selecthowtousecrutches")
            if userInput6 == "Hit":
                print("txt")
                return userInput6
            elif userInput6 == "Use":
                print("txt")
        elif Inventory != "Crutches":  # if inventory does not contain 'crutches' return to runawayzombie() to pick left
            print("txt")
            RunAwayZombie()
    elif userInput4 == "Left":  # 2 chances continue running or hide in room
        print("txt")
        ShowCorridor()
def ShowCorridor():
    userInput7 = input("Show corridor")  # choose graphical corridor or room
    if userInput7 == "Continue running":  # solutions path
        print("txt")  # graphics for reception area
        ContinueRunning()
    elif userInput7 == "Hide in Room":  # you are locked in with zombies and need to return to Left- Show_Corridor graphics
        print("txt")
        ShowCorridor()
def ContinueRunning():  # solutions path
    userInput8 = input('Look or hide')  # graphical reception or text with items to pick up
    if userInput8 == "Look":  # look for items
        print("search for something")
        PickupMap()
    elif userInput8 == "Hide behind desk":
        print("Zombie is coming")
        ContinueRunning()
def PickupMap():
    UserInput9 = input("Pick up Map, Pencils ,Paper ,Staple ,paperclip,")  # look for items in reception desk#Maybe str() need
    while UserInput9 != "Map":
        print("This item will not help you")
        return PickupMap()
    if UserInput9 == "Map":
        Inventory = Inventory + "Map"
        RuntoQuiz()
def RuntoQuiz():
    userInput10 = input("Hide or Run?:")
    if userInput10 == "Hide":
        RuntoQuiz()
    elif userInput10 == "Run": # Graphical window quiz# select a)b)c) of pictures
        FinalDoor()
        #Input in graphics
def FinalDoor():
    userInput22 = input("Left door to freedom or Right door to freedom?")
    if userInput22 == "Left":
        print("HAHA Almost")
        FinaDoor()
    elif userInput22 == "Right":
        print("WIN")  # insert graphics picture win a nice finish

def main():
    count = 0
    Inventory = []
    Firstscene()
    StayinRoom()
    WalkoutRoom()
    FightZombie()
    RunAwayZombie()
    ShowCorridor()
    ContinueRunning()
    PickupMap()
    RuntoQuiz()
    FinalDoor()
main()
