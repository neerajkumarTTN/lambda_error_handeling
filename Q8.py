try:
    string=input("Enter the string:")
    n=int(input("Enter the index:"))
    result=string[n]
    print(result)
except IndexError:
    print("Enter index in range of string size")

except ValueError:
    print("Enter the integer number") 