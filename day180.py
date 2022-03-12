# Assign a different name to function and call it through the new name

def player_info(name, age):
    print(name, age)

player_info("João", 20)


display_player = player_info

display_player("João", 20)