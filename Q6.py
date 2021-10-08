def divide():
    try:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        result=a/b
        if(b<0):
            assert b>0
        print(result)
    except ValueError:
        print("Please enter whole number")
    except ZeroDivisionError:
        print("Enter a denomerator number greater than zero")
divide()
