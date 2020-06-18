# name: William Gibson
# date: 2018-03-08
# description: Text-based adventure game
import random
import time


def main():
    level1 = open("TextFiles/LevelOne/LevelOne.txt", "r")
    level2 = open("TextFiles/LevelTwo/ChapterTwoA.txt", "r")
    level3A = open("TextFiles/LevelThree/ChapterThreeA.txt", "r")
    level3B = open("TextFiles/LevelThree/ChapterThreeB.txt", "r")
    level4 = open("TextFiles/LevelFour/Levelfour.txt", "r")
    questions = open("TextFiles/Questions.txt", "r")
    decisionmade = open("TextFiles/LevelTwo/DecisionMade.txt", "r")
    room = open("TextFiles/LevelThree/Rooms.txt", "r")
    item = open("TextFiles/LevelThree/Item.txt", "r")
    nav = open("TextFiles/Navigate.txt", "r")
    greet = open("TextFiles/Greeting.txt", "r")
    riddle = open("TextFiles/LevelFour/Riddle.txt", "r")
    completed = open("TextFiles/Completed.txt", "r")
    room4description = open(
        "TextFiles/LevelThree/RoomsDescriptions/Room4Description.txt", "r")
    room5description = open(
        "TextFiles/LevelThree/RoomsDescriptions/Room5Description.txt", "r")
    room6description = open(
        "TextFiles/LevelThree/RoomsDescriptions/Room6Description.txt", "r")
    room8description = open(
        "TextFiles/LevelThree/RoomsDescriptions/Room8Description.txt", "r")
    room9description = open(
        "TextFiles/LevelThree/RoomsDescriptions/Room9Description.txt", "r")
    room10description = open(
        "TextFiles/LevelThree/RoomsDescriptions/Room10Description.txt", "r")

    RidLines = riddle.readlines()
    Rlines = room.readlines()
    Qlines = questions.readlines()
    Ilines = item.readlines()
    Nlines = nav.readlines()
    Dlines = decisionmade.readlines()
    Glines = greet.readlines()

    def msg(room):
        if room['msg'] == '':
            # entering room for first time
            return Nlines[9] + ' ' + room['name'] + room['des']
        else:
            return room['msg']

    def get_choice(room, dir):
        # Directions
        if dir == 'North' or dir == 'north':
            choice = 0
        elif dir == 'East' or dir == 'east':
            choice = 1
        elif dir == 'South' or dir == 'south':
            choice = 2
        elif dir == 'West' or dir == 'west':
            choice = 3
        else:
            return -1

        if room['directions'][choice] == 0:
            return 4
        else:
            return choice

    def playAgain():

        print(Qlines[1])
        playAgain = input('Prompt: ' )
        if playAgain == "yes" or playAgain == "y":

            main()
        else:
            exit()

    def chooseDecision():
        decision = ""
        while decision != "1" and decision != "2":  # input vailidation
            print (Qlines[0])
            decision = input('Prompt: ' )
        
        return decision

    def checkDecision(chosenDecision):
        chosen_int = int(chosenDecision)
        print(Dlines[0])
        time.sleep(2)
        print(Dlines[1])
        time.sleep(2)
        correctDecision = 1
        if chosen_int == correctDecision:
            levelThree()
        elif chosen_int == 2:
            print (level3B.read())
            print (Glines[2] + ' ' + player)
            playAgain()

    def levelOne():
        print(level1.read())
        global player
        player = input('Prompt: ' )
        print(Glines[0]+" " + player)
        levelTwo()

    def levelTwo():
        print(Glines[1]+" " + player + " " + level2.read())
        choice = chooseDecision()
        checkDecision(choice)  # choice is equal to "1" or "2"

    def levelThree():

        print(level3A.read())

        dirs = (0, 0, 0, 0)

        room1 = {'name': Rlines[1], 'directions': dirs, 'msg': '', 'des': ''}
        room2 = {'name': Rlines[2], 'directions': dirs, 'msg': '', 'des': ''}
        room3 = {'name': Rlines[3], 'directions': dirs, 'msg': '', 'des': ''}
        room4 = {'name': Rlines[4], 'directions': dirs,
                 'msg': '', 'des': room4description.read()}
        room5 = {'name': Rlines[5], 'directions': dirs,
                 'msg': '', 'des': room5description.read()}
        room6 = {'name': Rlines[6], 'directions': dirs,
                 'msg': '', 'des': room6description.read()}
        room7 = {'name': Rlines[7], 'directions': dirs, 'msg': '', 'des': ''}
        room8 = {'name': Rlines[8], 'directions': dirs,
                 'msg': '', 'des': room8description.read()}
        room9 = {'name': Rlines[9], 'directions': dirs,
                 'msg': '', 'des': room9description.read()}
        room10 = {'name': Rlines[10], 'directions': dirs,
                  'msg': '', 'des': room10description.read()}

        room1['directions'] = (room2, 0, 0, 0)
        room2['directions'] = (room3, room4, room1, 0)
        room3['directions'] = (room6, room7, room2, room5)
        room4['directions'] = (0, 0, 0, room2)
        room5['directions'] = (0, room3, 0, 0)
        room6['directions'] = (0, 0, room3, 0)
        room7['directions'] = (room10, room9, room8, room3)
        room8['directions'] = (room7, 0, 0, 0)
        room9['directions'] = (0, 0, 0, room7)
        room10['directions'] = (0, 0, room7, 0)

        # rooms for where the body might bewest
        rooms = [room4, room5, room6, room8, room9, room10]
        room_of_item = random.choice(rooms)
        item_found = False
        room = room1
        print("")
        while True:
            if item_found and room['name'] == Rlines[1]:
                # back at room1 with item found
                print(Nlines[7]+" "+Rlines[1]+" "+Nlines[8])
                levelFour()
                break
            elif not item_found and room['name'] == room_of_item['name']:
                # found item
                item_found = True
                print(msg(room) + " " + player + " " +
                      Ilines[2] + " " + Ilines[1] + " " + Ilines[3])
                # back in room with item already found
                room['msg'] = Nlines[2] + room['name'] + \
                    Nlines[5] + Ilines[1] + Nlines[6]
            else:
                # returning to a room
                print(msg(room))
                room['msg'] = Nlines[2] + room['name']

            stuck = True
            while stuck:
                print (Nlines[1])
                dir = input('Prompt: ' )
                choice = get_choice(room, dir)
                if choice == -1:
                    # entered invalid command
                    print (Nlines[3])
                elif choice == 4:
                    # leads to a dead end
                    print (Nlines[4])
                else:
                    room = room['directions'][choice]
                    stuck = False

    def levelFour():
        print(level4.read())
        guess = 5
        while True:
            print (RidLines[0])
            answer = input('Prompt: ' )
            guess -= 1
            if answer == "piano":
                print (completed.read())
                playAgain()
                break
            elif guess < 0:
                print (RidLines[4])
                print (Glines[2] + ' ' + player)
                playAgain()
                break
            else:
                print (RidLines[2]+" " + str(guess) + " " + RidLines[3])

    levelOne()


main()
