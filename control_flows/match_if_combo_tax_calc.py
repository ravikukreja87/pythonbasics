# Tax Calculator
# If income is < 10,000 then tax is 10%
# If income is between 10,000 and 50,000 then tax is 20%
# If income is > 50,000 then tax is 30%

# Use Case - My income is 20,000/- Then how much should be the tax?
# First 10,000 Rs taxed at 10% = 1000
# Remaining 10,000 Rs will be taxed at 20% = 2000
# Total tax will be 3000/- Rs

# Use Case - My income is 60,000/- Then how much should be the tax?
# First 10,000 Rs taxed at 10% = 1000
# Next 40,000 Rs will be taxed at 20% = 8000
# Remaining 10,000 Rs will be taxed at 30% = 3000
# Total tax will be 12000/- Rs

# Use Case - My income is 1,00,000/- Then how much should be the tax?
# First 10,000 Rs taxed at 10% = 1000
# Next 40,000 Rs will be taxed at 20% = 8000
# Remaining 50,000 Rs will be taxed at 30% = 15000
# Total tax will be 24000/- Rs


def tax_calc(income):
    match income:
        case n if n <= 10000:
            tax = n * 10 / 100
        case n if 10000 < n <= 50000:
            tax = 10000 * 10 / 100 + (n - 10000) * 20 / 100
        case n if n > 50000:
            tax = 10000 * 10 / 100 + 40000 * 20 / 100 + (n - 50000) * 30 / 100
    print(f'Total tax is {tax} on income of {income}')

tax_calc(9000)
tax_calc(11000)
tax_calc(40000)
tax_calc(100000)
tax_calc(20000)
tax_calc(60000)
