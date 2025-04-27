try:
    a=int(input("enter a number: "))
    print("The number is: ",a)
except ValueError as ex:
    print("a",ex)