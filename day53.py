# Write a python program to find heights of the top three building in descending order from eight given buildings.

print("Input the heights of eight buildings:")

building_heights = [int(input()) for i in range(8)]

print("Heights of the top three buildings:")

building_heights  = sorted(building_heights )

print(*building_heights [:4:-1], sep='\n')