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



def play():
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


play()
