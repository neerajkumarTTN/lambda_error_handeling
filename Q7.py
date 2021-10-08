while True:
    try:
        num=int(input("Enter a number:"))
    except ValueError:
        print("Try again")
    else:
        print(f"This is interger:{num}")
        break