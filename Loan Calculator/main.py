import math
import argparse
import sys

def print_error_and_exit():
    print("Incorrect parameters")
    sys.exit()

parser = argparse.ArgumentParser(description="Loan Calculator")
parser.add_argument("--type", help="Indicates the type of payment: 'annuity' or 'diff' (differentiated)")
parser.add_argument("--payment", type=float, help="Monthly payment amount")
parser.add_argument("--principal", type=float, help="Loan principal")
parser.add_argument("--periods", type=int, help="Number of months to repay the loan")
parser.add_argument("--interest", type=float, help="Annual interest rate")

args = parser.parse_args()

# Check if fewer than four arguments are provided
if len(sys.argv) < 5:
    print_error_and_exit()

# Check for negative values
if any(value is not None and value < 0 for value in [args.payment, args.principal, args.periods, args.interest]):
    print_error_and_exit()

# Check for valid --type
if args.type not in ["annuity", "diff"]:
    print_error_and_exit()

if args.interest is None:
    print_error_and_exit()
else:
    nominal_interest_rate = args.interest / (12 * 100)

    if args.type == "diff":
        if args.payment is not None or args.principal is None or args.periods is None:
            print_error_and_exit()
        else:
            total_payment = 0
            for m in range(1, args.periods + 1):
                diff_payment = math.ceil(args.principal / args.periods + nominal_interest_rate * (args.principal - (args.principal * (m - 1)) / args.periods))
                total_payment += diff_payment
                print(f"Month {m}: payment is {diff_payment}")
            overpayment = total_payment - args.principal
            print(f"\nOverpayment = {int(overpayment)}")
    elif args.type == "annuity":
        if args.principal is None:
            loan_principal = args.payment / ((nominal_interest_rate * math.pow(1 + nominal_interest_rate, args.periods)) / (math.pow(1 + nominal_interest_rate, args.periods) - 1))
            print(f"Your loan principal = {round(loan_principal)}!")
            overpayment = args.payment * args.periods - loan_principal
            print(f"Overpayment = {int(overpayment)}")
        elif args.payment is None:
            annuity_payment = math.ceil(args.principal * ((nominal_interest_rate * math.pow(1 + nominal_interest_rate, args.periods)) / (math.pow(1 + nominal_interest_rate, args.periods) - 1)))
            print(f"Your annuity payment = {annuity_payment}!")
            overpayment = annuity_payment * args.periods - args.principal
            print(f"Overpayment = {int(overpayment)}")
        elif args.periods is None:
            number_of_payments = math.ceil(math.log(args.payment / (args.payment - nominal_interest_rate * args.principal), 1 + nominal_interest_rate))
            years, months = divmod(number_of_payments, 12)
            if years == 0:
                print(f"It will take {months} months to repay this loan!")
            elif months == 0:
                print(f"It will take {years} years to repay this loan!")
            else:
                print(f"It will take {years} years and {months} months to repay this loan!")
            overpayment = args.payment * number_of_payments - args.principal
            print(f"Overpayment = {int(overpayment)}")
        else:
            print_error_and_exit()
    else:
        print_error_and_exit()
