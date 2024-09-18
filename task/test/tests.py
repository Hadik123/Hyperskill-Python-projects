from hstest import CheckResult, StageTest, dynamic_test, TestedProgram
import ast, math
import re

INVALID_RESULT = "No one is joining for the party"


class BillSplitterTest(StageTest):

    @dynamic_test(data=['0', '-1'])
    def test_noone(self, inp):
        pr = TestedProgram()
        pr.start()
        output = pr.execute(inp)
        lines = output.splitlines()
        non_empty_line_count = sum(1 for line in lines if line.strip())
        if non_empty_line_count != 1:
            return CheckResult.wrong('When a zero or negative input provided as a number of friends '
                                     f'your program should output only one non-empty line')
        if (re.sub(r"\s", '', INVALID_RESULT.strip().lower())
                not in re.sub(r"\s", '', output.strip().lower())):
            return CheckResult.wrong('When a zero or negative input provided as a number of friends '
                                     f'your program should output "{INVALID_RESULT}" string')
        return CheckResult.correct()

    test_data = [
        [5, ["Marc", "Jem", "Monica", "Anna", "Sam"], 100],
        [7, ["Marc", "Jem", "Monica", "Anna", "Jason", "Ben", "Ned"], 41],
        [3, ["Jake", "Sam", "Irina"], 109],
        [2, ["Jake", "Sam"], 109],
    ]

    @dynamic_test(data=test_data)
    def test(self, num, friends, total):
        pr = TestedProgram()
        pr.start()
        for inp in [str(num)] + friends:
            pr.execute(inp)
        output = pr.execute(str(total))

        try:
            user_dict = ast.literal_eval(output.lower())
        except ValueError:
            return CheckResult.wrong('Please check your last output, it should be a dictionary')
        except IndentationError:
            return CheckResult.wrong('There should not be any leading whitespace before your last output')
        except Exception:
            return CheckResult.wrong('Something wrong with your output. '
                                     'Make sure you print the dictionary like in examples!\n'
                                     f'Found dict: \n{output}')
        if not isinstance(user_dict, dict):
            return CheckResult.wrong('Please check your last output, it should be a dictionary')
        elif len(user_dict) != num:
            return CheckResult.wrong('Please check if you have added all your friends to dictionary '
                                     'after taking an user input')
        try:
            bill_list = list(user_dict.values())
            bill = sum(bill_list)
        except TypeError:
            return CheckResult.wrong("Dictionary values should be of integer type")

        if not all([k.lower() in user_dict.keys() for k in friends]):
            return CheckResult.wrong('Please check all friends are in dictionary keys')
        if math.ceil(bill) != float(total) and math.floor(bill) != float(total):
            return CheckResult.wrong("Please update dictionary with correct split values")
        if bill_list[0] != round(total / num, 2):
            return CheckResult.wrong("Please round off split values to two decimal places")

        return CheckResult.correct()


if __name__ == '__main__':
    BillSplitterTest().run_tests()
