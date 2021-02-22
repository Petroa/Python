# This a Loan Calculator

# The plan is next:
# imports
# call for argparse module
    # object
    # arguments
    # operations
        # check negative input
        # branch diff
            # check 'None percent'
            # type of compute: diff
        # branch annuity
            # types of compute: annuity
            # check 'None percent'
                # 1
                # 2
                # 3
import math
import argparse

# parser module
parser = argparse.ArgumentParser(description='This is a loan calculator')

# parser module arguments
parser.add_argument('-tp', '--type', choices=['diff', 'annuity'], help="type in: diff or annuity", required=True)  # type of counts
parser.add_argument('-pm', '--payment', help='how much shall i pay per mth?', type=float)  # how much shall i pay per mth? =mp
parser.add_argument('-pr', '--principal', help='this is a loan principal=sum of money', type=float)  # this is a loan principal=sum of money (1000 000) =lp
parser.add_argument('-pe', '--periods', help='this is sum of month', type=float)  # this is sum of month (10) =np
parser.add_argument('-i', '--interest', help='this is percent', type=float,)  # percent (10%) =li

# parser module main object
count = parser.parse_args()

# operations

if count.payment is not None and count.principal is not None and count.periods is not None and count.interest is not None:
    if count.payment < 0 and count.principal < 0 and count.periods < 0 and count.interest < 0:
        print('Incorrect parameters')

# branch diff
# check 'None percent'
# type of compute: diff
elif count.type == 'diff':
    if count.interest is None:
        print('Incorrect parameters')
    elif not count.payment:
        index = count.interest / (12 * 100)
        count_1 = 0
        for m in range(1, int(count.periods + 1)):
            month_payment = math.ceil((count.principal / count.periods) + index * (count.principal - ((count.principal * (m - 1)) / count.periods)))
            count_1 += month_payment
            print('Month ' + str(m) + ': payment is ' + str(month_payment))
        Overpay = math.ceil(count.principal - count_1)
        print()
        print("Overpayment = " + str(Overpay))
    else:
        print("Incorrect parameters")

# branch annuity
# types of compute: annuity
# check 'None percent'
# 1
# 2
# 3

elif count.type == 'annuity':
    if count.interest is None:
        print('Incorrect parameters')
    elif count.payment != None and count.principal != None:  # число периодов
        nominal_interest_rate = count.interest / (12 * 100)
        number_of_months2 = math.ceil(math.log(count.payment / (count.payment - (nominal_interest_rate * count.principal)), nominal_interest_rate + 1))
        yrs = number_of_months2 // 12
        # mnth = round(((number_of_months2 / 12) - yrs) / 0.083)

        nominal_interest_rate = count.interest / (12 * 100)

        Overpay1 = math.ceil((number_of_months2 * count.payment - count.principal))

        print('It will take ' + str(yrs) + 'to repay this loan!')
        print("Overpayment = " + str(Overpay1))
    elif (count.periods != None) and (count.principal != None):  # итого платеж составит
        nominal_interest_rate = count.interest / (12 * 100)
        x =  math.pow(nominal_interest_rate + 1, count.periods)
        mpm = math.ceil(count.principal * (nominal_interest_rate * x) / (x - 1))

        Overpay2 = math.ceil((mpm * count.periods) - count.principal)

        print('Your annuity payment = ' + str(mpm) + '!')
        print("Overpayment = " + str(Overpay2))
    elif count.payment != None and count.periods != None:   # ваш долг равен:
        nominal_interest_rate = count.interest / (12 * 100)
        x = math.pow(nominal_interest_rate + 1, count.periods)
        lop = math.ceil(count.payment / ((nominal_interest_rate * x) / (x - 1)))

        Overpay3 = math.ceil(count.payment * count.periods - lop)

        print('Your loan principal = ' + str(lop) + '!')
        print("Overpayment = " + str(Overpay3))
    elif count.interest is None:
        print('Incorrect parameters')
else:
    print('Incorrect parameters')
