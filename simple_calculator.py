def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def modulus(x, y):
    return x % y
def exponent(x, y):
    return x ** y
def floor_division(x, y):
    return x // y
print("1.Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Modulus \n6. Exponentiation \n7. Floor Division")
sel=int(input("Select operation: "))
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
if sel==1:
    print("Result: "+str(n1)+" + "+str(n2)+" = "+str(add(n1, n2)))
elif sel==2:
    print("Result: "+str(n1)+" - "+str(n2)+" = "+str(subtract(n1, n2)))
elif sel==3:
    print("Result: "+str(n1)+" * "+str(n2)+" = "+str(multiply(n1, n2)))
elif sel==4:
    print("Result: "+str(n1)+" / "+str(n2)+" = "+str(divide(n1, n2)))
elif sel==5:
    print("Result: "+str(n1)+" % "+str(n2)+" = "+str(modulus(n1, n2)))
elif sel==6:
    print("Result:  "+str(n1)+" ** "+str(n2)+" = "+str(exponent(n1, n2)))
elif sel==7:
    print("Result: "+str(n1)+" // "+str(n2)+" = "+str(floor_division(n1, n2)))
else:
    print("Invalid selection.")
