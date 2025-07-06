# Basic function 
def greet():
    print("Hello Navneet")
    
    
# Function with parameters
def add_numbers(a,b):
    return a + b
result = add_numbers(10,10)
print(f"The sum is: {result}")

# Function with Variable Arguments
def print_names(*names):
    for name in names:
        print(name)
print_names("Navneet", "Python", "Programming")

#