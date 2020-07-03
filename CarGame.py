print('''Enter the command to run the car
1. START = start the car
2. STOP = stop the car
3. EXIT = exit the car
4. HELP = controls
''')
command = ""
started = False
stopped = False
while command.upper() != "EXIT":
    command = input("> ")
    if command.upper() == "START":
        if started:
            print("Car is already started.....!!!")
        else:
            started = True
            print('Your car has started Running....')

    elif command.upper() == "STOP":
        if stopped:
            print("The car has already been stopped...")
        else:
            stopped = True
            print("The car has been stopped...")

    elif command.upper() == "HELP":
        print('''Enter the command to run the car
1. START = start the car
2. STOP = stop the car
3. EXIT = exit the car
4. HELP = controls
        ''')
    elif command.upper() == "EXIT":
        print("You have quit the game. ")
        break
    else:
        print("Sorry !! Can't understand invalid input")

