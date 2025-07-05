# Boolean       # Boolean is a data type that can hold one of two values: True or False.
# # It is often used to represent truth values in logical expressions.
# # Booleans are commonly used in conditional statements and loops.         
# # Example of a boolean value
True_Value = True
print(True_Value)  # Output: True
# # Example of a boolean value
False_Value = False
print(False_Value)  # Output: False
# # Example of a boolean expression
Boolean_Expression = (5 > 3)  # This expression evaluates to True
print(Boolean_Expression)  # Output: True
# # Example of a boolean expression
Boolean_Expression_2 = (5 < 3)  # This expression evaluates to False
print(Boolean_Expression_2)  # Output: False
# # Example of a boolean value in a conditional statement
if True_Value:
    print("This is True")  # Output: This is True
else:
    print("This is False")
# # Example of a boolean value in a conditional statement
if False_Value:
    print("This is True")
else:
    print("This is False")
# # Example of a boolean value in a loop
for i in range(3):
    if i % 2 == 0:
        print(f"{i} is even")  # Output: 0 is even, 2 is even
    else:
        print(f"{i} is odd")  # Output: 1 is odd
# # Example of a boolean value in a loop
while True_Value:
    print("This loop will run until False_Value is set to False")
    break  # Break to avoid infinite loop
# # Example of a boolean value in a loop
while False_Value:
    print("This loop will not run because False_Value is False")
    break  # Break to avoid infinite loop
# # Example of a boolean value in a function
def check_boolean(value):
    if value:
        return "Value is True"
    else:
        return "Value is False"

print(check_boolean(True_Value))  # Output: Value is True
print(check_boolean(False_Value))  # Output: Value is False
