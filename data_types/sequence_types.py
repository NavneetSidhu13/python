# This script demonstrates various sequence types in Python.

# Sequence types in Python include strings, lists, and tuples.
# Strings Immutable ordered collection
# Strings are immutable, meaning once created, they cannot be changed.
# They are ordered, meaning the order of characters is preserved.
# Strings can contain letters, numbers, and special characters.
# You can access characters by their index, which starts at 0.
# Strings are defined using single quotes '' or double quotes "".
# Example of a string
print("Hello, Navneet")
# Example of a string with single quotes
print('Hello, Navneet')
# Example of a string with double quotes
print("Navneet's Python Course")
# Example of a string with special characters
print("Navneet\nPython\tCourse")  # \n is a newline, \t is a tab
# Example of a string with escape characters
print("Navneet said, \"Python is great!\"")  # \" is used to include double quotes in a string
# Example of a string with a variable
# Strings can be assigned to variables  
Name = "Navneet"
print(Name)     
# Example of a string with a number
# Strings can also contain numbers
Age = "25"
print(Age)  
# Example of a string with special characters
# Strings can contain special characters like @, #, $, etc.
Email = "navneet@example.com"
print(Email)    
# Example of a string with a multiline string
# Multiline strings can be created using triple quotes
Multiline_String = """This is a multiline string.
It can span multiple lines.
You can use it for longer text."""
print(Multiline_String)   




# Lists Mutable ordered collection
# Lists are mutable, meaning you can change their content
# after creation. They are ordered, meaning the order of elements is preserved.
# Lists can contain elements of different data types.
# You can access elements by their index, which starts at 0.
# Lists can be modified by adding, removing, or changing elements.
# Lists are defined using square brackets [].
# Example of a list containing different data types
Mixed_List = [1, "Navneet", 5.6, True]
print(Mixed_List)
# Example of a list containing only strings
# Lists can also contain only strings
String_List = ["Navneet", "Python", "Programming"]
print(String_List)  
# Example of a list containing only integers
Int_List = [1, 2, 3, 4, 5]
print(Int_List)
# Example of a list containing only floats
Float_List = [1.1, 2.2, 3.3, 4.4, 5.5]
print(Float_List)   
# Example of a list containing only booleans
Bool_List = [True, False, True]
print(Bool_List)




# Tuples Immutable ordered collection
# Tuples are immutable, meaning once created, they cannot be changed.
# They are ordered, meaning the order of elements is preserved.
# Tuples can contain elements of different data types.
# You can access elements by their index, which starts at 0.
# Tuples are defined using parentheses ().
# Example of a tuple containing different data types
Mixed_Tuple = (1, "Navneet", 5.6, True)
print(Mixed_Tuple)
# Example of a tuple containing only strings
# Tuples can also contain only strings
String_Tuple = ("Navneet", "Python", "Programming")
print(String_Tuple)
# Example of a tuple containing only integers
Int_Tuple = (1, 2, 3, 4, 5)
print(Int_Tuple)
# Example of a tuple containing only floats
Float_Tuple = (1.1, 2.2, 3.3, 4.4, 5.5)
print(Float_Tuple)
# Example of a tuple containing only booleans
Bool_Tuple = (True, False, True)
print(Bool_Tuple)       
# Example of a tuple with a single element
# Tuples with a single element must have a comma after the element
Single_Element_Tuple = (42,)
print(Single_Element_Tuple)     
# Example of a tuple with multiple elements
Multiple_Elements_Tuple = (1, 2, 3, 4,
5, 6, 7, 8, 9, 10)
print(Multiple_Elements_Tuple)
# Example of a tuple with nested tuples
Nested_Tuple = (1, (2, 3), (4, 5))
print(Nested_Tuple) 
# Example of a tuple with a mix of data types
Mixed_Nested_Tuple = (1, "Navneet", (2.2, 3.3), [4, 5])
print(Mixed_Nested_Tuple)   
# Example of a tuple with a mix of data types and nested lists
Mixed_Nested_List_Tuple = (1, "Navneet", [2.2, 3.3], (4, 5))
print(Mixed_Nested_List_Tuple)      
# Example of a tuple with a mix of data types and nested dictionaries
Mixed_Nested_Dict_Tuple = (1, "Navneet", {"key": "value"}, (4, 5))
print(Mixed_Nested_Dict_Tuple)
# Example of a tuple with a mix of data types and nested sets
Mixed_Nested_Set_Tuple = (1, "Navneet", {2.2,
3.3}, (4, 5))
print(Mixed_Nested_Set_Tuple)
# Example of a tuple with a mix of data types and nested frozensets
Mixed_Nested_Frozenset_Tuple = (1, "Navneet", frozenset([2.2, 3.3]), (4, 5))
print(Mixed_Nested_Frozenset_Tuple)  
# Example of a tuple with a mix of data types and nested bytearrays
Mixed_Nested_Bytearray_Tuple = (1, "Navneet", bytearray([2, 3, 4]), (4, 5))
print(Mixed_Nested_Bytearray_Tuple)  
# Example of a tuple with a mix of data types and nested memoryviews
Mixed_Nested_Memoryview_Tuple = (1, "Navneet", memoryview(b"Hello"), (4, 5))
print(Mixed_Nested_Memoryview_Tuple)
# Example of a tuple with a mix of data types and nested complex numbers
Mixed_Nested_Complex_Tuple = (1, "Navneet", complex(2, 3), (4, 5))
print(Mixed_Nested_Complex_Tuple)
# Example of a tuple with a mix of data types and nested decimal numbers
from decimal import Decimal
Mixed_Nested_Decimal_Tuple = (1, "Navneet", Decimal('2.2'), (4, 5))
print(Mixed_Nested_Decimal_Tuple)
# Example of a tuple with a mix of data types and nested fractions
from fractions import Fraction
Mixed_Nested_Fraction_Tuple = (1, "Navneet", Fraction(2, 3), (4, 5))
print(Mixed_Nested_Fraction_Tuple)
# Example of a tuple with a mix of data types and nested datetime objects
from datetime import datetime
Mixed_Nested_Datetime_Tuple = (1, "Navneet", datetime.now(), (4, 5))
print(Mixed_Nested_Datetime_Tuple)
# Example of a tuple with a mix of data types and nested timezone-aware datetime objects
from datetime import timezone
Mixed_Nested_TZ_Datetime_Tuple = (1, "Navneet", datetime.now(timezone.utc), (4, 5))
print(Mixed_Nested_TZ_Datetime_Tuple)
# Example of a tuple with a mix of data types and nested UUID objects
import uuid
Mixed_Nested_UUID_Tuple = (1, "Navneet", uuid.uuid4(), (4, 5))
print(Mixed_Nested_UUID_Tuple)
# Example of a tuple with a mix of data types and nested namedtuples
from collections import namedtuple
Person = namedtuple('Person', ['name', 'age'])
Mixed_Nested_NamedTuple_Tuple = (1, Person(name="Navneet", age=25), (4, 5))
print(Mixed_Nested_NamedTuple_Tuple)
# Example of a tuple with a mix of data types and nested dataclasses
from dataclasses import dataclass
@dataclass
class PersonData:
    name: str
    age: int
Mixed_Nested_DataClass_Tuple = (1, PersonData(name="Navneet", age=25), (4, 5))
print(Mixed_Nested_DataClass_Tuple)     
# Example of a tuple with a mix of data types and nested enums
from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
Mixed_Nested_Enum_Tuple = (1, Color.RED, (4, 5))
print(Mixed_Nested_Enum_Tuple)





# Ranges
# Ranges are immutable ordered collections of numbers.
# They are often used in loops and can be created using the range() function.
# Example of a range from 0 to 9
Range_Example = range(10)
print(list(Range_Example))  # Convert range to list for display
# Example of a range from 1 to 10
Range_Example_2 = range(1, 11)
print(list(Range_Example_2))  # Convert range to list for display
# Example of a range with a step of 2
Range_Example_3 = range(0, 10, 2)
print(list(Range_Example_3))  # Convert range to list for display
# Example of a range with a negative step
Range_Example_4 = range(10, 0, -1)
print(list(Range_Example_4))  # Convert range to list for display       
# Example of a range with a negative step and a start value
Range_Example_5 = range(10, -1, -1)
print(list(Range_Example_5))  # Convert range to list for display
# Example of a range with a negative step and a start value and a step of 2
Range_Example_6 = range(10, -1, -2)
print(list(Range_Example_6))  # Convert range to list for display
# Example of a range with a negative step and a start value and a step of 3
Range_Example_7 = range(10, -1, -3)
print(list(Range_Example_7))  # Convert range to list for display 


