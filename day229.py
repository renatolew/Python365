# Format variables using a string.format() method.

quantity = 10
total_money = 5000
price = 500

statement1 = "I have {1} dollars so I can buy {0} playstations for {2:.2f} dollars."

print(statement1.format(quantity, total_money, price))