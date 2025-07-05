# Dictionary mapping type in Python
# Dictionaries are mutable, unordered collections of key-value pairs. 
# Each key in a dictionary must be unique and immutable, while values can be of any type.
# Dictionaries are defined using curly braces {} or the dict() constructor.
# Example of a dictionary with string keys and values


String_Dict = {"name": "Navneet", "language": "Python"}
print(String_Dict)  # Output: {'name': 'Navneet', 'language':
# 'Python'}
# Example of a dictionary with integer keys and values
Int_Dict = {1: "one", 2: "two", 3: "three"}
print(Int_Dict)  # Output: {1: 'one', 2: 'two', 3: 'three'}
# Example of a dictionary with mixed keys and values
Mixed_Dict = {"name": "Navneet", 1: 42, "is_student": True}
print(Mixed_Dict)  # Output: {'name': 'Navneet, 1: 42, 'is_student': True}
# Example of a dictionary with nested dictionaries
Nested_Dict = {    "person": {
        "name": "Navneet",
        "age": 30,
        "languages": ["Python", "JavaScript"]
    },
    "location": {
        "city": "New York",
        "country": "USA"
    }
}
print(Nested_Dict)  # Output: {'person': {'name': 'Navneet', 'age': 30, 'languages': ['Python', 'JavaScript']}, 'location': {'city': 'New York', 'country': 'USA'}}
# Example of a dictionary with mixed data types
Mixed_Data_Dict = {
    "name": "Navneet",
    "age": 30,
    "is_student": False,
    "grades": [85, 90, 95],
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "country": "USA"
    }
}
print(Mixed_Data_Dict)  # Output: {'name': 'Navneet', 'age': 30, 'is_student': False, 'grades': [85, 90, 95], 'address': {'street': '123 Main St', 'city': 'New York', 'country': 'USA'}}
# Example of a dictionary with a single key-value pair
Single_Pair_Dict = {"key": "value"}
print(Single_Pair_Dict)  # Output: {'key': 'value'}
# Example of a dictionary with multiple key-value pairs
Multiple_Pairs_Dict = {
    "name": "Navneet",
    "age": 30,
    "is_student": False,
    "languages": ["Python", "JavaScript"],
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "country": "USA"
    }
}
print(Multiple_Pairs_Dict)  # Output: {'name': 'Navneet', 'age': 30, 'is_student': False, 'languages': ['Python', 'JavaScript'], 'address': {'street': '123 Main St', 'city': 'New York', 'country': 'USA'}}
# Example of a dictionary with a mix of data types and nested lists
Mixed_Nested_List_Dict = {
    "name": "Navneet",
    "age": 30,
    "is_student": False,
    "grades": [85, 90, 95],
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "country": "USA"
    },
    "hobbies": ["reading", "coding", "traveling"]
}
print(Mixed_Nested_List_Dict)  # Output: {'name': 'Navneet', 'age': 30, 'is_student': False, 'grades': [85, 90, 95], 'address': {'street': '123 Main St', 'city': 'New York', 'country': 'USA'}, 'hobbies': ['reading', 'coding', 'traveling']}
# Example of a dictionary with a mix of data types and nested dictionaries
Mixed_Nested_Dict = {
    "person": {
        "name": "Navneet",
        "age": 30,
        "languages": ["Python", "JavaScript"]
    },
    "location": {
        "city": "New York",
        "country": "USA" 
    },
    "hobbies": ["reading", "coding", "traveling"]
}
print(Mixed_Nested_Dict)  # Output: {'person': {'name': 'Navneet', 'age': 30, 'languages': ['Python', 'JavaScript']}, 'location': {'city': 'New York', 'country': 'USA'}, 'hobbies': ['reading', 'coding', 'traveling']}
