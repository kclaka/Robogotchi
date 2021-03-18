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
    gameOptions = ["rock-paper-scissors", "numbers"]

    while True:
        choose_game = input("Which game would you like to play?")
        if not (choose_game.lower() in gameOptions):
            print("Please choose a valid option: Numbers or Rock-paper-scissors?")
            continue
        elif choose_game.lower() == gameOptions[0].lower():
            playRPS()
            break
        else:
            play_numbers()
            break


def unfortunateEvent(name, rust):
    message = ["sprinkler", "nothing", "nothing", "nothing", "puddle", "sprinkler", "pool", "nothing", "pool", "nothing", "nothing", "nothing"]

    choice = message[random.randint(0, len(message) - 1)]

    if choice == "puddle":
        rust += 10
        print(f"Oh no, {name} stepped into a puddle!")
    if choice == "sprinkler":
        rust += 30
        print(f"Oh, {name} encountered a sprinkler!")
    if choice == "pool":
        print(f"Guess what! {name} fell into the pool!")
        rust += 50

    return rust


def requestRecharge(name, battery, choice):
    if isBatteryEmpty(battery) and not choice == "recharge":
        print(f"The level of the battery is 0, {name} needs recharging!")
        return True
    return False


def isBatteryEmpty(battery):
    if battery <= 0:
        return True

    return False


def isFunEmpty(name, boredom, choice):
    if boredom == 100 and not choice == "play":
        print(f"{name} is too bored! {name} needs to have fun!")
        return True
    return False


def printRobotInfo(name, battery_level, over_heat, skills, boredom, rust):
    print(f"{name}'s stats are:\nthe battery is {battery_level},")
    print(f"overheat is {over_heat},")
    print(f"skill level is {skills},")
    print(f"boredom is {boredom},")
    print(f"rust is {rust}.")


def setName():
    name = input("How will you call your robot?")
    return name


def controlRobot():
    name = setName()

    battery_level = 100
    over_heat = 0
    skill = 0
    boredom = 0
    rust = 0

    choices = ["exit", "info", "recharge", "sleep", "play", "learn", "oil", "work"]

    while True:
        print(f"Available interactions with {name}:")
        print(
            "exit - Exit\n"
            "info - Check the vitals\n"
            "work - Work\n"
            "play - Play\n"
            "oil - Oil\n"
            "recharge - Recharge\n"
            "sleep - Sleep mode\n"
            "learn - Learn skills"

        )
        if over_heat >= 100:
            print(f"The level of overheat reached 100, {name} has blown up! Game over. Try again?")
            break
        if rust >= 100:
            print(f"{name} is too rusty! Game over. Try again?")
            break
        choice = input("Choose:")

        if not choice in choices:
            print("Invalid input, try again!")
            continue
        elif choice == choices[0]:
            break
        elif choice == choices[1]:
            printRobotInfo(name, battery_level, over_heat, skill, boredom, rust)
            continue
        elif requestRecharge(name, battery_level, choice):
            continue
        elif isFunEmpty(name, boredom, choice):
            continue
        elif choice == choices[4]:
            rust = unfortunateEvent(name, rust)
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
            continue
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
            prev_skill = skill
            if skill >= 100:
                print(f"There's nothing for {name} to learn!")
            else:
                skill += 10
            print(f"{name}'s level of skill was {prev_skill}. Now it is {skill}.")
            prev_heat = over_heat
            over_heat += 10
            print(f"{name}'s level of overheat was {prev_heat}. Now it is {over_heat}.")
            prev_batt = battery_level
            if battery_level - 10 < 0:
                battery_level = 0
            elif battery_level == 0:
                requestRecharge(name, battery_level, choice)
            else:
                battery_level -= 10
            print(f"{name}'s level of the battery was {prev_batt}. Now it is {battery_level}.")
            prev_bore = boredom
            boredom += 5
            print(f"{name}'s level of boredom was {prev_bore}. Now it is {boredom}.")
            print(f"{name} has become smarter!")
            continue
        elif choice == choices[6]:
            if rust == 0:
                print(f"{name} is fine, no need to oil!")
            else:
                prev_rust = rust
                rust -= 20
                if rust < 0:
                    rust = 0
                print(f"{name}'s level of rust was {prev_rust}. Now it is {rust}. {name} is less rusty!")
            continue
        elif choice == choices[7]:
            prev_rust = rust
            rust = unfortunateEvent(name, rust)
            if skill < 50:
                print(f"{name} has got to learn before working!")
            else:
                p_batt = battery_level
                p_heat = over_heat
                p_boredom = boredom
                if battery_level - 10 < 0:
                    battery_level = 0
                else:
                    battery_level -= 10
                    boredom += 10
                    over_heat += 10

                print(f"{name}'s level of boredom was {p_boredom}. Now it is {boredom}.")
                print(f"{name}'s level of overheat was {p_heat}. Now it is {over_heat}.")
                print(f"{name}'s level of the battery was {p_batt}. Now it is {battery_level}.")
                print(f"{name}'s level of rust was {prev_rust}. Now it is {rust}.")
                print(f"{name} did well!")

            continue
        elif choice == choices[8]:
            break

    print("Game over")


controlRobot()
