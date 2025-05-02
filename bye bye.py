valid = False
while not valid:
    try:
        a=int(input("enter a value: "))
        while a%2==0:
          print("bye bye")
          valid=True
    except ValueError:
        print("b")