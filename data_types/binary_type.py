# Binary    Type: Python
# Binary types in Python are used to represent binary data, such as images, audio files,
# and other non-textual data. The main binary types in Python are `bytes`, `bytearray`, and `memoryview`.           
## Example of a bytes object
Bytes_Object = b"Hello, Navneet"
print(Bytes_Object)  # Output: b'Hello, Navneet'            
# Example of a bytearray object
Bytearray_Object = bytearray(b"Hello, Navneet")
print(Bytearray_Object)  # Output: bytearray(b'Hello, Navneet')
# Example of a memoryview object
Memoryview_Object = memoryview(b"Hello, Navneet")
print(Memoryview_Object)  # Output: <memory at 0x...>   
# Example of a bytes object with a mix of data types
Mixed_Bytes_Object = b"Navneet" + bytes([1, 2, 3]) + b"Python"
print(Mixed_Bytes_Object)  # Output: b'Navneet\x01\x02\x03Python'
# Example of a bytearray object with a mix of data types
Mixed_Bytearray_Object = bytearray(b"Navneet") + bytearray([1, 2, 3]) + bytearray(b"Python")
print(Mixed_Bytearray_Object)  # Output: bytearray(b'Navneet\x01\x02\x03Python')
# Example of a memoryview object with a mix of data types
Mixed_Memoryview_Object = memoryview(b"Navneet") + memoryview(bytes([1, 2, 3])) + memoryview(b"Python") # type: ignore
print(Mixed_Memoryview_Object)  # Output: <memory at 0x...>
# Example of a bytes object with a single byte
Single_Byte_Bytes_Object = b"A"
print(Single_Byte_Bytes_Object)  # Output: b'A'
# Example of a bytearray object with a single byte
Single_Byte_Bytearray_Object = bytearray(b"A")
print(Single_Byte_Bytearray_Object)  # Output: bytearray(b'A')      
# Example of a memoryview object with a single byte
Single_Byte_Memoryview_Object = memoryview(b"A")
print(Single_Byte_Memoryview_Object)  # Output: <memory at 0x...>
# Example of a bytes object with multiple bytes
Multiple_Bytes_Bytes_Object = b"Hello, World!"
print(Multiple_Bytes_Bytes_Object)  # Output: b'Hello, World!'
# Example of a bytearray object with multiple bytes
Multiple_Bytes_Bytearray_Object = bytearray(b"Hello, World!")
print(Multiple_Bytes_Bytearray_Object)  # Output: bytearray(b'Hello , World!')
# Example of a memoryview object with multiple bytes
Multiple_Bytes_Memoryview_Object = memoryview(b"Hello, World!")
print(Multiple_Bytes_Memoryview_Object)  # Output: <memory at 0x...>
# Example of a bytes object with a mix of data types and nested lists
Mixed_Nested_Bytes_Object = b"Navneet" + bytes([1, 2, 3]) + b"Python" + b"Nested List"
print(Mixed_Nested_Bytes_Object)  # Output: b'Navneet\x01\x02\x03PythonNested List'
# Example of a bytearray object with a mix of data types and nested lists
Mixed_Nested_Bytearray_Object = bytearray(b"Navneet") + bytearray([1, 2, 3]) + bytearray(b"Python") + bytearray(b"Nested List")
print(Mixed_Nested_Bytearray_Object)  # Output: bytearray(b'Navneet\x01\x02\x03PythonNested List')
# Example of a memoryview object with a mix of data types and nested lists
Mixed_Nested_Memoryview_Object = memoryview(b"Navneet") + memoryview(bytes([1, 2, 3])) + memoryview(b"Python") + memoryview(b"Nested List")  # type: ignore
print(Mixed_Nested_Memoryview_Object)  # Output: <memory at 0x...>
# Example of a bytes object with a mix of data types and nested dictionaries
Mixed_Nested_Dict_Bytes_Object = b"Navneet" + bytes([1, 2, 3]) + b"Python" + b"Nested Dict"
print(Mixed_Nested_Dict_Bytes_Object)  # Output: b'Navneet\x01\x02\x03PythonNested Dict'
# Example of a bytearray object with a mix of data types and nested dictionaries
Mixed_Nested_Dict_Bytearray_Object = bytearray(b"Navneet") + bytearray([1, 2, 3]) + bytearray(b"Python") + bytearray(b"Nested Dict")
print(Mixed_Nested_Dict_Bytearray_Object)  # Output: bytearray(b'Navneet\x01\x02\x03PythonNested Dict')
