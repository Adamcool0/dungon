currentRoom = "heal room"

def move():
    global currentRoom



    while True:
        print("which way do you go: ")
        for direction in rooms[currentRoom]:
            print(direction)
        cake: str = input("")
        if cake in rooms[currentRoom].keys():
            currentRoom = rooms[currentRoom][cake]
            print("you went in to " + currentRoom)
            if currentRoom == "cody boss":
                    codyboss = 50000
                    classhelath = 2000

                    while True:
                        import random

                        null_list = ["cody used code  did 100 ", "cody used c++ code  did 100",
                                     "cody used java code  did 100", "cody used python code  did 100 "]
                        random_item = random.choice(null_list)
                        print(random_item)

                        active_player = "Null"

                        if random_item == "cody used code  did 100 ":
                            classhelath -= 100
                            print("class lost 100 ")
                        elif random_item == "cody used java code  did 100":
                            classhelath -= 100
                            print("class lost 100 ")
                        elif random_item == "cody used c++ code  did 100":
                            classhelath -= 100
                            print("class lost 100 ")
                        elif random_item == "cody used python code  did 100 ":
                            classhelath -= 100
                            print(" class lost 100 ")

                        classturn = True

                        def attack():

                            class_list = [" gun", " nice shovel 600",
                                          " shotgun"]

                        print("\ngun ")
                        print("nice shovel")
                        print("shotgun")
                        print("gun")
                        userinput = input("what is the attack you want ot use")

                        active_player = "class"

                        if userinput == "gun ":
                            codyboss -= 500
                            print("cody lost 500")
                        elif userinput == "nice shovel":
                            codyboss -= 600
                            print("cody lost 600")
                        elif userinput == "shotgun":
                            codyboss -= 400
                            print("cody lost 400")
                        elif userinput == "forbidden number":
                            codyboss -= 10000
                            print("cody boss lost 10000 ")

                        if codyboss <= 0:
                            print("cody was defeated and you won!!!!!!")
                            print("you wake up in class from sleeping")
                            break
                        elif classhelath <= 0:
                            print("you died and cody won")
                            break

            if currentRoom == "67 boss room":
                numberboss = 5000
                classhelath = 2000

                while True:
                    import random

                    null_list = ["67 67 did 50 ", "67 670 did 100",
                                     "67 bad number did 75","67 used 67 trap did 10 " ]
                    random_item = random.choice(null_list)
                    print(random_item)

                    active_player = "67"

                    if random_item == "67 67 did 100 ":
                        classhelath -= 100
                        print("class lost 100 ")
                    elif random_item == "67 670 did 100":
                        classhelath -= 100
                        print("class lost 100 ")
                    elif random_item == "67 bad number did 75":
                        classhelath -= 75
                        print("class lost 100 ")
                    elif random_item == "67 used 67 trap did 10 ":
                        classhelath -= 10
                        print(" class lost 100 ")

                        classturn = True



                        print("\ngun ")
                        print("nice shovel")
                        print("shotgun")
                        print("gun")
                        userinput = input("what is the attack you want ot use")

                        active_player = "class"

                        if userinput == "gun ":
                            numberboss -= 500
                            print("67 lost 500")
                        elif userinput == "nice shovel":
                            numberboss -= 600
                            print("67 lost 600")
                        elif userinput == "shotgun":
                            numberboss -= 400
                            print("67 lost 400")
                        elif userinput == "forbidden number":
                            numberboss -= 10000
                            print("67 boss lost 10000 ")


                        if numberboss <= 0:
                            print("67 was defeated and you won!!!!!!")
                            print("67 89")
                            break
                        elif classhelath <= 0:
                            print("you died and 67 won")
                            break
                        break
        elif cake == "up up down down left right left right a b start":
                print("you found secret")
        break


rooms = {
                'start':{'south': ' bomb '},
                'bomb': {'south': ' room'},
                'heal room': {'south': 'room','west': 'room2','east':'room3'},
                'room':{'south': 'room3','east':'room4','west':'67 boss room'},
                'room3':{'south': 'room4','east': 'room','west':'heal room'},
                'room4':{'north': 'room 3','west':'room','south':'cody boss'},
                'room2':{'east': 'heal room','west':'room5'},
                'room5':{'east':'room2','west':'room4'},


            }
while True:

    print("""██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗      ██████╗ ██████╗ ██████╗ ██╗   ██╗███████╗    ██╗███████╗██╗      █████╗ ███╗   ██╗██████╗ 
             ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗    ██╔════╝██╔═══██╗██╔══██╗╚██╗ ██╔╝██╔════╝    ██║██╔════╝██║     ██╔══██╗████╗  ██║██╔══██╗
             ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║    ██║     ██║   ██║██║  ██║ ╚████╔╝ ███████╗    ██║███████╗██║     ███████║██╔██╗ ██║██║  ██║
             ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║    ██║     ██║   ██║██║  ██║  ╚██╔╝  ╚════██║    ██║╚════██║██║     ██╔══██║██║╚██╗██║██║  ██║
             ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝    ╚██████╗╚██████╔╝██████╔╝   ██║   ███████║    ██║███████║███████╗██║  ██║██║ ╚████║██████╔╝
              ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝      ╚═════╝ ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝    ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ 
       """)
    print("you landed on the island after a big storm and you are the only one to survive the crash you here a voice say " )


    user_input = input("pleas enter name")
    print("hello " + user_input)

    print("you look through the recage and find a gun")
    user_input = input("you see a cave do you go in to it??")

    if user_input == "yes":
         print("you went in the cave")
         print("the cave door blow up")
    elif user_input == "no":
            print("you did not go in cave and die because you dont find food")
            print("game over")
            print("do you want to restart do it your self")
            break

    while True:

        move()


