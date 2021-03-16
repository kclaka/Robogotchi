# Write your code here
import random

def getUserInput():
    done = False
    number = input("What is your number? ")
    while not done:
        if number == "exit game":
            break
        try:
            number = int(number)
            if number < 0:
                print("The number can't be negative!")
                break
            elif number > 1000000:
                print("Invalid input! The number can't be bigger than 1000000")
                break
            else:
                return number
        except ValueError:
            print("A string is not a valid input!")
            break

    return number


def getRobotNumber():
    return random.randint(0, 1000000)


def getGoalNumber():
    return random.randint(0, 1000000)


def printsummary(userscore, robotscore, draw):
    print()
    print(f"You won: {userscore}, ")
    print(f'The robot won: {robotscore}, ')
    print(f'Draws: {draw}. ')


def play_numbers():
    userScore = 0
    robotScore = 0
    draw = 0

    while True:
        user = getUserInput()

        if user == 'exit game':
            printsummary(userScore, robotScore, draw)
            break
        elif type(user) == str:
            continue
        elif int(user) < 0:
            continue
        elif int(user) > 1000000:
            continue
        else:
            robot = getRobotNumber()
            print(f"The robot entered the number {robot}.")
            goal = getGoalNumber()
            print(f"The goal number is {goal}.")

            userDiff = abs(user - goal)
            robotDiff = abs(robot - goal)

            if userDiff < robotDiff:
                print("You Won!")
                userScore += 1
                continue
            elif userDiff > robotDiff:
                print("The robot won!")
                robotScore += 1
            else:
                print("it's a draw!")
                draw += 1


def checkRPSwinner(user_input, robot_input):
    if ((user_input == "rock" and robot_input == "scissors") or
            (user_input == "paper" and robot_input == "rock") or
            (user_input == "scissors" and robot_input == "paper")):
        return "user"
    elif user_input == robot_input:
        return "draw"
    else:
        return "robot"


def playRPS():
    user_score = 0
    robot_score = 0
    draw = 0
    moves = ["rock", "paper", "scissors"]

    while True:
        user_input = input("What is your move?")
        if user_input == "exit game":
            break
        if user_input not in moves:
            print("No such option! Try again!")
            continue
        else:
            robot_input = moves[random.randint(0, 2)]
            print(f"The robot chose {robot_input}")
            winner = checkRPSwinner(user_input, robot_input)
            if winner == "user":
                print("You won!")
                user_score += 1
            elif winner == "robot":
                print("The robot won!")
                robot_score += 1
            else:
                print("It's a draw!")
                draw += 1
    printsummary(user_score, robot_score, draw)


def startConsole():
    gameOptions = ["Rock-paper-scissors", "Numbers"]

    while True:
        choose_game = input("Which game would you like to play?")
        if not (choose_game in gameOptions):
            print("Please choose a valid option: Numbers or Rock-paper-scissors?")
            continue
        elif choose_game.lower() == gameOptions[0].lower():
            playRPS()
            break
        else:
            play_numbers()
            break


def getBattery():
    pass


def printRobotInfo(name, battery_level, over_heat, skills, boredom):
    print(f"{name}'s stats are: the battery is {battery_level},")
    print(f"overheat is {over_heat},")
    print(f"skill level is {skills},")
    print(f"boredom is {boredom}.")


def setName():
    name = input("How will you call your robot?")
    return name


def getHeat():
    pass


def getSkill():
    pass


def changeRobotState():
    pass


def controlRobot():
    name = setName()

    battery_level = 100
    over_heat = 0
    skills = 0
    boredom = 0

    choices = ["exit", "info", "recharge", "sleep", "play", "exit"]

    while True:
        print(f"Available interactions with {name}:")
        print(
            "exit - Exit\n"
            "info - Check the vitals\n"
            "recharge - Recharge\n"
            "sleep - Sleep mode\n"
            "play - Play"
        )
        if over_heat == 100:
            print(f"The level of overheat reached 100, {name} has blown up! Game over. Try again?")
            break

        choice = input("Choose:")

        if not choice in choices:
            print("Invalid input, try again!")
            continue
        elif choice == choices[0]:
            break
        elif choice == choices[1]:
            printRobotInfo(name, battery_level, over_heat, skills, boredom)
        elif choice == choices[4]:
            startConsole()
            prev_boredom = boredom
            prev_overheat = over_heat
            if boredom - 10 < 0:
                boredom = 0
            else:
                boredom -= 10
            over_heat += 10
            print(f"{name}'s level of boredom was {prev_boredom}. Now it is {boredom}.")
            print(f"{name}'s level of overheat was {prev_overheat}. Now it is {over_heat}.")
            if boredom == 0:
                print(f"{name} is in a great mood!")
        elif choice == choices[3]:
            prev_value = over_heat
            if over_heat == 0:
                print(f"{name} is cool!")

            else:
                over_heat -= 20
                if over_heat < 0:
                    over_heat = 0
                    print(f"{name} is cool!")
                    print(f"{name}'s level of overheat was {prev_value}. Now it is {over_heat}.")
                else:
                    print(f"{name} cooled off!")
                    print(f"{name}'s level of overheat was {prev_value}. Now it is {over_heat}.")
        elif choice == choices[2]:
            if battery_level == 100:
                print(f"{name} is charged!")
            else:
                temp_battery = battery_level
                battery_level += 10
                temp_overheat = over_heat
                over_heat -= 5
                temp_boredom = boredom
                boredom += 5
                print(
                    f"{name}'s level of overheat was {temp_overheat}. Now it is {over_heat}."
                    f"{name}'s level of the battery was {temp_battery}. Now it is {battery_level}."
                    f"{name}'s level of boredom was {temp_boredom}. Now it is {boredom}."
                    f"{name} is recharged!"
                )

        elif choice == choices[5]:
            break
        print("Game over")



controlRobot()
