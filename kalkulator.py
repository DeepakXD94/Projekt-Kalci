def calc(x,y):
    if z == str('+'):
        print(add())
    elif z == str('-'):
        print(sub())
    else:
        print(multi(x,y))

def add(a,b):
    return a + b
    
def sub(a,b):
    return a - b

def mult(a,b):
    return a * b

x = float(input("Enter the first number : "))
z = input("Enter the operator")
y = float(input("Enter the second number : "))

calc(x,y)