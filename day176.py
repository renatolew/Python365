# Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

n = int(input("Type the number term for the series: "))

start = 2
sum_seq = 0

for i in range(0, n):
    print(start, end="+")
    sum_seq += start
    start = start * 10 + 2

print("\nSum of above series is:", sum_seq)