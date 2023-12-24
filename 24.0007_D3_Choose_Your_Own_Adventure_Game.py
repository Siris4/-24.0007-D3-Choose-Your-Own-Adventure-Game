#Treasure Island - Choose your Own Adventure:

print("Welcome to Treasure Island. Your mission is to find the treasure.")

left_or_right = input("Where would you like to start off? L or R?")
if left_or_right == "L":
    print("Someone pushes you into a Taxi. The doors are locked. He's driving like crazy.")
    boat_or_plane = input(
        "You get dropped off at an airport, and they force you to get on a boat or a plane (B or P), Which do you pick?")
    if boat_or_plane == "B":
        print("You get on, but a small meteor sinks a burning hole into the boat. The boat sinks immediately. Better luck next time.")
    else:
        print("You fly away and land in Wisconsin a few hours later.")
        colored_doors = input("In the airport, you only have 4 doors to pick from? 1, 2, 3, or 4?")
        if colored_doors == "1":
            print("You died.")
        elif colored_doors == "2":
            print("You died x 2.")
        elif colored_doors == "3":
            print("You died x 3.")
        else:
            print("YOU MADE IT!!! ENJOY YOUR VACATION!! And be careful with strangers.")
else:
    print("You got hit by a bus. That sucks.")