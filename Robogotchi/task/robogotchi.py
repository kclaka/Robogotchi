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


startConsole()
