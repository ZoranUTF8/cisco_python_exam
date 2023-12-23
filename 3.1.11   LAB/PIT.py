# Once upon a time there was a land – a land of milk and honey, inhabited by happy and prosperous people. The people paid taxes, of course – their happiness had limits. The most important tax, called the Personal Income Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:
#
# if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was what they called tax relief)
# if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
# Your task is to write a tax calculator.
#
# It should accept one floating-point value: the income.
# Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which will do the rounding for you – you'll find it in the skeleton code in the editor.
# Note: this happy country never returned any money to its citizens. If the calculated tax was less than zero, it would only mean no tax at all (the tax was equal to zero). Take this into consideration during your calculations.
#
# Look at the code in the editor – it only reads one input value and outputs a result, so you need to complete it with some smart calculations.
#


def calculate_surplus(amount):
    surplus = max(0, amount - 85528)
    return surplus


def calculate_percentage_of_surplus(amount):
    surplus = calculate_surplus(amount)
    percentage_of_surplus = 0.32 * surplus
    return percentage_of_surplus


# def calculate_tax_amount(income=0, tax_rate=0, tax_relief=0, surpulus=0, taxToAdd=0):
#     tax_amount = income * tax_rate
#     tax_amount -= tax_relief
#
#     if taxToAdd:
#         tax_amount = income + taxToAdd
#
#     if surpulus:
#         tax_amount += surpulus
#
#     print(f"The tax is: ${tax_amount}")
#
#     return tax_amount

def calculate_tax_amount(income=0, tax_rate=0, tax_relief=0, surplus=0, taxToAdd=0):
    tax_amount = income * tax_rate
    tax_amount -= tax_relief

    if taxToAdd:
        tax_amount += taxToAdd  # Add taxToAdd instead of replacing tax_amount

    if surplus:
        tax_amount += surplus

    # Ensure tax_amount is not negative
    tax_amount = max(0, tax_amount)

    print(f"The tax is: ${tax_amount}")

    return tax_amount


def getTotalTax():
    limit = 85528
    tax = 0
    totalTaxAmout = 0

    try:
        totalEarnings = float(input("Enter earnings:..."))
    except ValueError as ve:
        print(f"Value error, check your input: {ve}")

    if limit > totalEarnings:
        tax = 0.18
        taxRelief = 556.02
        totalTaxAmout = calculate_tax_amount(income=totalEarnings, tax_rate=tax, tax_relief=taxRelief)
        if totalEarnings == 0:
            print("The tax is: 0.0 thalers")
    else:
        taxToAdd = 14839.02
        surpulus = calculate_percentage_of_surplus(totalEarnings)
        totalTaxAmout = calculate_tax_amount(income=totalEarnings, surplus=surpulus, taxToAdd=taxToAdd)

    return round(totalTaxAmout)


res = getTotalTax()

print(res)
