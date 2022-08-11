# Add an if statement and a continue statement to the loop so that it skips when iterator equals "sun".

weather = ["snow", "rain", "sun", "clouds"]

for i in weather:
    if i == "sun":
        continue
    print(i)