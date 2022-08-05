def calc(x,y):
    if z == str('+'):
        print(add(x, y))

    elif z == str('-'):
        print(sub(x, y))

    elif z == str('*'):
        print(multi(x, y))

    elif z == str('/'):
        print(div(x, y))

    elif z == str('%'):
        print(rem(x,y))

    elif z == str('>'):
        print(greater(x,y))

    elif z == str('<'):
        print(lower(x,y))

    elif z == str('pwr'):
        print(pwr(x,y))

    elif z == str('root'):
        print(root(x,y))
        
    else:
        print("Error. Please enter proper input.")

def add(a,b):
    return a + b
    
def sub(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
    return a / b

def rem(a,b):
    return a % b

def greater(a,b):
    return a > b

def lower(a,b):
    return a < b

def pwr(a,b):
    return a ** b

def root(a,b):
    return a ** (1/b)

x = float(input("Enter the first number : "))
z = input("Enter the operator : ")
y = float(input("Enter the second number : "))

calc(x,y)