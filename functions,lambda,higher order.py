#EARLY RETURN

 # Division calculator

def divide(a,b):
    if b == 0:
        print("Cannot divided by zero")
        return
    print("Result:",a / b)
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
divide(a, b)

#LOGIN SYSTEM

def login(username,password):
    if username == "admin":
        if password == "python123":
            print("Login Successful.")
            return
    print("Invalied Creditails.")
        
username = input("Enter username:")
password = input("Enter password:")

#AGE VALIDATION

login(username, password)
def register(age):
    if age <=18:
        print("Registration Filed.")
        return
    print("Registration Successful.")
age = int(input("Enter age:"))
register(age)     

#LAMBDA FUNCTIONS

square_lambda = lambda X:X**2
print(square_lambda(19))

#LARGEST NUMBER

largest_number_lambda = 20 > 40
a = int(input("Enter a:"))
b = int(input("Enter b:"))
print("20"if 20>40 else "40")

# EVEN OR ODD

even_odd = lambda n:"Even" if n % 2 == 0 else"odd"
n = int(input("Enter n:"))
print(even_odd(n))

#GREAD CALCULATOR

gread = lambda n:"Pass"if n>=35 else"Fail"
n = int(input("Enter your marks:"))
print(gread(n))

#HIGHER ORDER FUNCTION##
#GREETING FUNCTION

def greet(): 
    print("HELLO ! SIRISHA")
def execute(func):
    func()
execute(greet)
    
#CALCULATOR  USING HIGHER ORDER FUNCTION

def add(a,b):
    print( a + b)
    return
def subtract(a,b):
    print( a - b)
    return
def multiply(a,b):
    print( a * b )
    return
def calculate(operation,a,b):
    return operation(a,b)
a = int(input("Enter the value:"))
b = int(input("Enter the value:"))

print("Addition:",calculate(add,a,b))
print("Subraction:",calculate(subtract,a,b))
print("Multiplication:",calculate(multiply,a,b))

 #WLCOME MESSAGE
def welcome():
    print("Welcome Alice")#

def display():
    print("function,student_name")
def execute(func):
    func()
execute(welcome)