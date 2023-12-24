print("Welcome to the rollercoaster!")
price = 0
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        price = 5
        # print("Child tickets are $5.")
    elif age <= 18:
        price = 7
        # print("Youth tickets are $7.")
    elif age > 18:
        price = 12
        # print("Adult tickets are $12.")

    wants_photo = input("Do you want your photo taken? Y or N? ")
    if wants_photo == "Y" or "y":
        price += 3
    # you DON'T need an else statement here, because you want nothing to happen anyhow and it already defaults to
    # nothing, so that's PERFECT!!
    print(f"Yes photo? Your total price is: ${price}")  # because this is indented BEFORE price += 3, this block doesn't
    # actually run at all until that block has finished, and this new indented line starts up as a separate entity

else:
    print("Sorry, you cannot ride it yet.")
