from typing import List, Any
from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult
from hstest.exceptions import WrongAnswerException
import re


class RobogotchiTestParent(StageTest):


    def prs_print_check(self, output, answer):
        parsed_output = output.split("\n")
        if not parsed_output:
            raise WrongAnswerException("Make sure your program outputs all required lines.")
        parsed_output = parsed_output[0].strip().split()
        if not parsed_output:
            raise WrongAnswerException("Make sure your program outputs results of the Rock-paper-scissors game in the required format.")
        robot_answer = parsed_output[-1].lower().strip('.')
        if robot_answer not in ['scissors', 'paper', 'rock']:
            raise WrongAnswerException(f"A problem occurred during the processing of the following output:\n"
                                       f"\"{output}\"\n"
                                       f"The last word in the first line of this output is supposed to contain an option name:\n"
                                       f"rock, paper or scissors.\n"
                                       f"However, the last word of the first line does not seem to be equal to any of these words.")

        try:
            ideal = self.check_who_won_ro(robot_answer=robot_answer,
                                          human_answer=answer).split('\n')
            ideal = [line for line in ideal if line]
            for i in ideal:
                if i.lower() not in output.lower():
                    return False
            return True
        except IndexError:
            pass

    def check_who_won_num(self, human_answer, robot_answer, goal):
        if abs(goal - human_answer) < abs(goal - robot_answer):
            self.won_numbers += 1
            return (f"The robot entered the number {robot_answer}."
                    f"\nThe goal number is {goal}."
                    f"\nYou won!")
        elif abs(goal - human_answer) > abs(goal - robot_answer):
            self.lost_numbers += 1
            return (f"The robot entered the number {robot_answer}."
                    f"\nThe goal number is {goal}."
                    f"\nRobot won!")
        else:
            self.draw_numbers += 1
            return (f"The robot entered the number {robot_answer}."
                    f"\nThe goal number is {goal}."
                    f"\nIt's a draw!")

    def check_who_won_ro(self, human_answer, robot_answer):
        if human_answer == 'paper':
            if robot_answer == 'scissors':
                self.lost_roshambo += 1
                return f"Robot chose {robot_answer}" \
                       f"\nRobot won!"
            elif robot_answer == 'rock':
                self.won_roshambo += 1
                return f"Robot chose {robot_answer}" \
                       f"\nYou won!"
            else:
                self.draw_roshambo += 1
                return f"Robot chose {robot_answer}" \
                       f"\nIt's a draw!"
        elif human_answer == 'rock':
            if robot_answer == 'paper':
                self.lost_roshambo += 1
                return f"Robot chose {robot_answer}" \
                       f"\nRobot won!"
            elif robot_answer == 'scissors':
                self.won_roshambo += 1
                return f"Robot chose {robot_answer}" \
                       f"\nYou won!"
            else:
                self.draw_roshambo += 1
                return f"Robot chose {robot_answer}" \
                       f"\nIt's a draw!"
        elif human_answer == 'scissors':
            if robot_answer == 'rock':
                self.lost_roshambo += 1
                return f"Robot chose {robot_answer}" \
                       f"\nRobot won!"
            elif robot_answer == 'paper':
                self.won_roshambo += 1
                return f"Robot chose {robot_answer}" \
                       f"\nYou won!"
            else:
                self.draw_roshambo += 1
                return f"Robot chose {robot_answer}" \
                       f"\nIt's a draw!"
        else:
            return 'No such option! Try again!\n'

    def interface_prints_check(self, output):
        pattern = '[––—]'
        interface_parsed = re.sub(pattern, '-', self.ideal_interface).split('\n')
        output = re.sub(pattern, '-', output.lower())
        for inter in interface_parsed:
            if inter.lower().strip() not in output:
                return False
        return True

    def recharge_what_prints(self, output):
        if self.battery == 100 and 'level' not in output:
            if "Daneel is charged" not in output:
                return False
        else:
            if self.battery != 100:
                message = '\nDaneel is recharged'
                text = f"Daneel's level of overheat was {self.overheat+5}. Now it is {self.overheat}." \
                                f"\nDaneel's level of the battery was {self.battery-10}. Now it is {self.battery}." \
                                f"\nDaneel's level of boredom was {self.boredom-5}. Now it is {self.boredom}.\n" \
                                f"{message}"
                text = text.split('\n')
                for tex in text:
                    if tex.lower() not in output.lower():
                        return False
        return True

    def sleep_what_prints(self, output):
        if self.overheat == 0 and self.overheat_previous == 0:
            if "Daneel is cool" not in output:
                return False
        else:
            if self.overheat != 0:
                insertion  = '\nDaneel cooled off'
            else:
                insertion = '\nDaneel is cool'
            text = f"Daneel's level of overheat was {self.overheat_previous}. Now it is {self.overheat}.\n" \
                   f"{insertion}"
            text = text.split('\n')
            for tex in text:
                if tex.lower() not in output.lower():
                    return False
        return True

    def game_statistics_prints_check(self, output, game):
        if game == 'numbers':
            ideal = f"You won: {self.won_numbers}," \
                    f"\nRobot won: {self.lost_numbers}," \
                    f"\nDraws: {self.draw_numbers}."
            ideal = ideal.split('\n')
            for i in ideal:
                if i.lower() not in output.lower():
                    return False
        else:
            ideal = f"You won: {self.won_roshambo}," \
                    f"\nRobot won: {self.lost_roshambo}," \
                    f"\nDraws: {self.draw_roshambo}."
            ideal = ideal.split('\n')
            for i in ideal:
                if i.lower() not in output.lower():
                    return False
        return True

    def increase_the_params(self, command):
        if command == 'play':
            self.boredom = self.boredom - 10 if self.boredom - 10 >= 0 else self.boredom - self.boredom
            self.overheat = self.overheat + 10 if self.overheat + 10 < 100 else 100
        elif command == 'sleep':
            self.overheat = self.overheat - 20 if self.overheat - 20 > 0 else self.overheat-self.overheat
        elif command == 'recharge':
            self.overheat = self.overheat - 5 if self.overheat - 5 > 0 else 0
            self.battery = self.battery + 10 if self.battery + 10 < 100 else 100
            self.boredom = self.boredom + 5 if self.boredom + 5 < 100 else 100


    def play_what_prints_check(self, output):
        if "which game would you like to play?" not in output.lower():
            return False
        return True

    def roshambo_what_prints_check(self, output):
        if "what is your move?" not in output.lower():
            return False
        return True

    def wrong_option_what_prints(self, output):
        check = "invalid input" in output.lower() and 'try again' in output.lower()
        if not check:
            return False
        return True

    def info_what_prints(self, output):
        text = f"Daneel's stats are:" \
               f"\nbattery is {self.battery}," \
               f"\noverheat is {self.overheat}," \
               f"\nskill level is {self.skills}," \
               f"\nboredom is {self.boredom}."
        text = text.split('\n')
        for tex in text:
            if tex.strip().lower() not in output.lower():
                return False
        return True

    def parse_the_output(self, output):
        parsed_output = output.split()
        check = len(parsed_output) >= 11 and isinstance(int(parsed_output[5].strip('.')), int) \
                and isinstance(int(parsed_output[10].strip('.')), int)
        if not check:
            raise WrongAnswerException("The result of the game is formatted incorrectly")
        else:
            robot_answer = int(parsed_output[5].strip('.'))
            goal_number = int(parsed_output[10].strip('.'))
        return robot_answer, goal_number

    def normal_number_prints_check(self, output, number):
        try:
            parsed_output = output.split()
            robot_answer = int(parsed_output[5].strip('.'))
            goal_number = int(parsed_output[10].strip('.'))
            ideal = self.check_who_won_num(number, robot_answer, goal_number).split('\n')
            ideal = [line for line in ideal if line][-1]
            if ideal.lower() not in output.lower():
                return False
            return True
        except ValueError:
            return False

    def numbers_what_prints_check(self, output):
        if 'what is your number?' not in output.lower():
            return False
        return True

    def numbers_exceptions(self, output, kind):
        output = [line for line in output.lower().split('\n') if line][0]
        if isinstance(kind, str):
            if "a string is not a valid input" not in output:
                return False
        elif kind > 1000000:
            if "the number can't be bigger than 1000000" not in output:
                return False
        elif kind < 0:
            if "number can't be negative" not in output:
                return False
        return True

    def knife_exception(self, output):
        check = 'no such option' in output.lower() and 'try again' in output.lower()
        if not check:
            return False
        return True

    def zerify_numbers_count(self, game):
        if game == 'numbers':
            self.won_numbers = 0
            self.lost_numbers = 0
            self.draw_numbers = 0
        else:
            self.won_roshambo = 0
            self.lost_roshambo = 0
            self.draw_roshambo = 0



class PreRobogotchiTest(RobogotchiTestParent):

    ideal_interface = f"\nAvailable interactions with Daneel:\nexit – Exit" \
               f"\ninfo – Check the vitals\nrecharge – Recharge" \
               f"\nsleep – Sleep mode\nplay – Play\n\nChoose:"

    won_roshambo = 0
    lost_roshambo = 0
    draw_roshambo = 0

    won_numbers = 0
    lost_numbers = 0
    draw_numbers = 0

    skills = 0
    overheat = 0
    boredom = 0
    battery = 100

    boredom_previous = 0
    overheat_previous = 0

    def generate(self) -> List[TestCase]:
        return [
            TestCase(stdin=[self.func1, self.func2, self.func3, self.func4, self.func5,
                            self.func6, self.func7, self.func8, self.func9, self.func10,
                            self.func11, self.func12, self.func13, self.func14, self.func15,
                            self.func16, self.func17, self.func18, self.func19, self.func20,
                            self.func21, self.func22, self.func23, self.func24, self.func25,
                            self.func26, self.func27, self.func28, self.func29, self.func30,
                            self.func31, self.func32, self.func33]),
            TestCase(stdin=[self.func34, self.func35, self.func36, self.func37, self.func38,
                            self.func39, self.func40, self.func41, self.func42, self.func43,
                            self.func44, self.func45, self.func46, self.func47, self.func48,
                            self.func49, self.func50, self.func51, self.func52, self.func53,
                            self.func54, self.func55, self.func56, self.func57, self.func58,
                            self.func59, self.func60, self.func61, self.func62, self.func63,
                            self.func64, self.func65, self.func66, self.func67, self.func68,
                            self.func69, self.func70, self.func71, self.func72, self.func73,
                            self.func74, self.func75, self.func76, self.func77, self.func78,
                            self.func79, self.func80],
                            check_function=self.check_boom)
        ]

    """Test 1"""

    def func1(self, output):
        if output.strip() != 'How will you call your robot?':
            return CheckResult.wrong("The program should suggest the user to name their robot")
        return 'Daneel'

    def func2(self, output):
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('play')
        return 'play'

    def func3(self, output):
        if not self.play_what_prints_check(output):
            return CheckResult.wrong("The program should offer to choose a game")
        return 'Numbers'

    def func4(self, output):
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong('The program should ask the user for the number')
        return '96753'

    def func5(self, output):
        if not self.normal_number_prints_check(output, 96753):
            return CheckResult.wrong("The result is incorrect or impossible to parse")
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong('The program should ask the user for the number')
        return '333'

    def func6(self, output):
        if not self.normal_number_prints_check(output, 333):
            return CheckResult.wrong("The result is incorrect or impossible to parse")
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong('The program should ask the user for the number')
        return '987659'

    def func7(self, output):
        if not self.normal_number_prints_check(output, 987659):
            return CheckResult.wrong("The result is incorrect or impossible to parse")
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong('The program should ask the user for the number')
        return 'exit game'

    def func8(self, output):
        if not self.game_statistics_prints_check(output, 'numbers'):
            return CheckResult.wrong("The statistics is incorrect")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.zerify_numbers_count('numbers')
        return 'info'

    def func9(self, output):
        if not self.info_what_prints(output):
            return CheckResult.wrong("The information provided is incorrect")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.overheat_previous = self.overheat
        self.increase_the_params('sleep')
        return 'sleep'

    def func10(self, output):
        if not self.sleep_what_prints(output):
            return CheckResult.wrong("The robot should cool off properly")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('play')
        return 'play'

    def func11(self, output):
        if not self.play_what_prints_check(output):
            return CheckResult.wrong("The program should ask the user which game to play")
        return 'Rock-paper-scissors'

    def func12(self, output):
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'rock'

    def func13(self, output):
        if not self.prs_print_check(output, 'rock'):
            return CheckResult.wrong("Make sure your output is correct and complete")
        return 'paper'

    def func14(self, output):
        if not self.prs_print_check(output, 'paper'):
            return CheckResult.wrong("Make sure your output is correct and complete")
        return 'scissors'

    def func15(self, output):
        if not self.prs_print_check(output, 'scissors'):
            return CheckResult.wrong("Make sure your output is correct and complete")
        return 'exit game'

    def func16(self, output):
        if not self.game_statistics_prints_check(output, 'roshambo'):
            return CheckResult.wrong("The statistics is incorrect")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.zerify_numbers_count('roshambo')
        self.increase_the_params('play')
        return 'play'

    def func17(self, output):
        if not self.play_what_prints_check(output):
            return CheckResult.wrong("The program should offer to choose a game")
        return 'Rock-paper-scissors'

    def func18(self, output):
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'rock'

    def func19(self, output):
        if not self.prs_print_check(output, 'rock'):
            return CheckResult.wrong("Make sure your output is correct and complete")
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'lightning'

    def func20(self, output):
        if not self.knife_exception(output):
            return CheckResult.wrong("The program should inform the user about invalid input")
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'exit game'

    def func21(self, output):
        if not self.game_statistics_prints_check(output, 'roshambo'):
            return CheckResult.wrong("The statistics is incorrect")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.zerify_numbers_count('roshambo')
        return 'info'

    def func22(self, output):
        if not self.info_what_prints(output):
            return CheckResult.wrong("The information provided is incorrect")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'recharge'

    def func23(self, output):
        if not self.recharge_what_prints(output):
            return CheckResult.wrong("The robot didn't recharge correctly")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('play')
        return 'play'

    def func24(self, output):
        if not self.play_what_prints_check(output):
            return CheckResult.wrong("The program should offer to choose a game")
        return 'Numbers'

    def func25(self, output):
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong('The program should ask the user for the number')
        return '579'

    def func26(self, output):
        if not self.normal_number_prints_check(output, 579):
            return CheckResult.wrong("The result is incorrect or impossible to parse")
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong('The program should ask the user for the number')
        return 'hamsa'

    def func27(self, output):
        if not self.numbers_exceptions(output, 'hamsa'):
            return CheckResult.wrong("The program should inform the user about invalid input")
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong('The program should ask the user for the number')
        return '11113'

    def func28(self, output):
        if not self.normal_number_prints_check(output, 11113):
            return CheckResult.wrong("The result is incorrect or impossible to parse")
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong('The program should ask the user for the number')
        return '7789'

    def func29(self, output):
        if not self.normal_number_prints_check(output, 7789):
            return CheckResult.wrong("The result is incorrect or impossible to parse")
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong('The program should ask the user for the number')
        return 'exit game'

    def func30(self, output):
        if not self.game_statistics_prints_check(output, 'numbers'):
            return CheckResult.wrong("The statistics is incorrect")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.overheat_previous = self.overheat
        self.increase_the_params('sleep')
        self.zerify_numbers_count('numbers')
        return 'sleep'

    def func31(self, output):
        if not self.sleep_what_prints(output):
            return CheckResult.wrong("The robot should cool off properly")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.overheat_previous = self.overheat
        self.increase_the_params('sleep')
        return 'sleep'

    def func32(self, output):
        if not self.sleep_what_prints(output):
            return CheckResult.wrong("The robot should cool off properly")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.overheat_previous = self.overheat
        return 'sleep'

    def func33(self, output):
        if not self.sleep_what_prints(output):
            return CheckResult.wrong("The robot should cool off properly")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        return 'exit'

    """Test 2"""

    def func34(self, output):
        if output.strip() != 'How will you call your robot?':
            return CheckResult.wrong("The program should suggest the user to name their robot")
        return 'Daneel'

    def func35(self, output):
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('play')
        return 'play'

    def func36(self, output):
        if not self.play_what_prints_check(output):
            return CheckResult.wrong("The program should offer to choose a game")
        return 'Numbers'

    def func37(self, output):
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong('The program should ask the user for the number')
        return '79'

    def func38(self, output):
        if not self.normal_number_prints_check(output, 457):
            return CheckResult.wrong("The result is incorrect or impossible to parse")
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong('The program should ask the user for the number')
        return '5098763'

    def func39(self, output):
        if not self.numbers_exceptions(output, 5098763):
            return CheckResult.wrong("The program should inform the user about invalid input")
        return 'exit game'

    def func40(self, output):
        if not self.game_statistics_prints_check(output, 'numbers'):
            return CheckResult.wrong("The statistics is incorrect")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('play')
        self.zerify_numbers_count('numbers')
        return 'play'

    def func41(self, output):
        if not self.play_what_prints_check(output):
            return CheckResult.wrong("The program should offer to choose a game")
        return 'Rock-paper-scissors'

    def func42(self, output):
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'scissors'

    def func43(self, output):
        if not self.prs_print_check(output, 'scissors'):
            return CheckResult.wrong("Make sure your output is correct and complete")
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'exit game'

    def func44(self, output):
        if not self.game_statistics_prints_check(output, 'roshambo'):
            return CheckResult.wrong("The statistics is incorrect")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.zerify_numbers_count('roshambo')
        self.increase_the_params('play')
        return 'play'

    def func45(self, output):
        if not self.play_what_prints_check(output):
            return CheckResult.wrong("The program should offer to choose a game")
        return 'Numbers'

    def func46(self, output):
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return '97825'

    def func47(self, output):
        if not self.normal_number_prints_check(output, 97825):
            return CheckResult.wrong("The result is incorrect or impossible to parse")
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'exit game'

    def func48(self, output):
        if not self.game_statistics_prints_check(output, 'numbers'):
            return CheckResult.wrong("The statistics is incorrect")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.zerify_numbers_count('numbers')
        self.increase_the_params('play')
        return 'play'

    def func49(self, output):
        if not self.play_what_prints_check(output):
            return CheckResult.wrong("The program should offer to choose a game")
        return 'Rock-paper-scissors'

    def func50(self, output):
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'paper'

    def func51(self, output):
        if not self.prs_print_check(output, 'paper'):
            return CheckResult.wrong("Make sure your output is correct and complete")
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'exit game'

    def func52(self, output):
        if not self.game_statistics_prints_check(output, 'roshambo'):
            return CheckResult.wrong("The statistics is incorrect")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.zerify_numbers_count('roshambo')
        self.increase_the_params('play')
        return 'play'

    def func53(self, output):
        if not self.play_what_prints_check(output):
            return CheckResult.wrong("The program should offer to choose a game")
        return 'bombers'

    def func54(self, output):
        if "please choose a valid option: numbers or rock-paper-scissors?" not in output.lower():
            return CheckResult.wrong("The user should be informed about an invalid choice")
        return 'Numbers'

    def func55(self, output):
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return '920853'

    def func56(self, output):
        if not self.normal_number_prints_check(output, 920853):
            return CheckResult.wrong("The result is incorrect or impossible to parse")
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return '740301'

    def func57(self ,output):
        if not self.normal_number_prints_check(output, 740301):
            return CheckResult.wrong("The result is incorrect or impossible to parse")
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return '619765'

    def func58(self, output):
        if not self.normal_number_prints_check(output, 619765):
            return CheckResult.wrong("The result is incorrect or impossible to parse")
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'exit game'

    def func59(self, output):
        if not self.game_statistics_prints_check(output, 'numbers'):
            return CheckResult.wrong("The statistics is incorrect")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.zerify_numbers_count('numbers')
        self.increase_the_params('play')
        return 'play'

    def func60(self, output):
        if not self.play_what_prints_check(output):
            return CheckResult.wrong("The program should offer to choose a game")
        return 'Rock-paper-scissors'

    def func61(self, output):
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'rock'

    def func62(self, output):
        if not self.prs_print_check(output, 'rock'):
            return CheckResult.wrong("Make sure your output is correct and complete")
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'rock'

    def func63(self, output):
        if not self.prs_print_check(output, 'rock'):
            return CheckResult.wrong("Make sure your output is correct and complete")
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'rock'

    def func64(self, output):
        if not self.prs_print_check(output, 'rock'):
            return CheckResult.wrong("Make sure your output is correct and complete")
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'exit game'

    def func65(self, output):
        if not self.game_statistics_prints_check(output, 'roshambo'):
            return CheckResult.wrong("The statistics is incorrect")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.zerify_numbers_count('roshambo')
        self.increase_the_params('play')
        return 'play'

    def func66(self, output):
        if not self.play_what_prints_check(output):
            return CheckResult.wrong("The program should offer to choose a game")
        return 'Numbers'

    def func67(self, output):
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return '995125'

    def func68(self, output):
        if not self.normal_number_prints_check(output, 995125):
            return CheckResult.wrong("The result is incorrect or impossible to parse")
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'exit game'

    def func69(self, output):
        if not self.game_statistics_prints_check(output, 'numbers'):
            return CheckResult.wrong("The statistics is incorrect")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.zerify_numbers_count('numbers')
        self.increase_the_params('play')
        return 'play'

    def func70(self, output):
        if not self.play_what_prints_check(output):
            return CheckResult.wrong("The program should offer to choose a game")
        return 'Rock-paper-scissors'

    def func71(self, output):
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'paper'

    def func72(self, output):
        if not self.prs_print_check(output, 'paper'):
            return CheckResult.wrong("Make sure your output is correct and complete")
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'exit game'

    def func73(self, output):
        if not self.game_statistics_prints_check(output, 'roshambo'):
            return CheckResult.wrong("The statistics is incorrect")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.zerify_numbers_count('roshambo')
        self.increase_the_params('play')
        return 'play'

    def func74(self, output):
        if not self.play_what_prints_check(output):
            return CheckResult.wrong("The program should offer to choose a game")
        return 'Numbers'

    def func75(self, output):
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong('The program should ask the user for the number')
        return '5563'

    def func76(self, output):
        if not self.normal_number_prints_check(output, 5563):
            return CheckResult.wrong("The result is incorrect or impossible to parse")
        if not self.numbers_what_prints_check(output):
            return CheckResult.wrong('The program should ask the user for the number')
        return 'exit game'

    def func77(self, output):
        if not self.game_statistics_prints_check(output, 'numbers'):
            return CheckResult.wrong("The statistics is incorrect")
        if not self.interface_prints_check(output):
            return CheckResult.wrong("The interface is different from the exemplary one")
        self.increase_the_params('play')
        return 'play'

    def func78(self, output):
        if not self.play_what_prints_check(output):
            return CheckResult.wrong("The program should offer to choose a game")
        return 'Rock-paper-scissors'

    def func79(self, output):
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'scissors'

    def func80(self, output):
        if not self.prs_print_check(output, 'scissors'):
            return CheckResult.wrong("Make sure your output is correct and complete")
        if not self.roshambo_what_prints_check(output):
            return CheckResult.wrong("The game should ask the user for their move")
        return 'exit game'

    def check(self, reply: str, attach: Any) -> CheckResult:
        if "game over" not in reply.lower():
            return CheckResult.wrong("The program should print that the game is over")
        return CheckResult.correct()

    def check_boom(self, reply: str, attach: Any) -> CheckResult:
        check = 'the level of overheat reached 100, daneel has blown up' in reply.lower()
        check2 = 'game over' in reply.lower() and 'try again?' in reply.lower()
        if not (check and check2):
            return CheckResult.wrong("The program should print that the game is over")
        return CheckResult.correct()

if __name__ == '__main__':
    PreRobogotchiTest().run_tests()
