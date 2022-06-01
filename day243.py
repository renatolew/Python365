# Calculate income tax for the given income by adhering to the below rules
# Taxable Income	Rate (in %)
# First $10,000	         0
# Next $10,000	        10
# The remaining	        20


income = int(input("Type your income: "))
tax_payable = 0
print("\nGiven income: ", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    x = income - 10000
    tax_payable = x * 10 / 100
else:
    tax_payable = 0

    tax_payable = 10000 * 10 / 100

    tax_payable += (income - 20000) * 20 / 100

print("Total tax to pay is", tax_payable)