try:
    num1,num2=eval(input("enter two numbers separated by a comma: "))
    result=num1/num2
    print("the result is: ",result)
except ZeroDivisionError:
    print("a",ZeroDivisionError)
except SyntaxError:
    print("b")
else:
    print("c")
finally:
    print("d")