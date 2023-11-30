age = 0
while age >= 0:
    try:
        age = int(input("Please input an age (-1 to quit):"))
    except ValueError:
        print("Not a number")
        continue

    if age<0:
        print("Quit")
    elif age < 13:
        print("Child")
    elif age < 20:
        print("Teenager")
    else:
        print("Adult")        