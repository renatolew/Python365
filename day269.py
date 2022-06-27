# Python program to implement matrix addition

X = [[8,5,1],
[9 ,3,2],
[4 ,6,3]]

Y = [[8,5,3],
[9,5,7],
[9,4,1]]

result = [[0,0,0],
[0,0,0],
[0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
for k in result:
    print(k)