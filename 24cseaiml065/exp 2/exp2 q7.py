# Input for Integer
int_input_str = input("Enter an integer: ")
my_int = int(int_input_str)

# Input for String
my_string = input("Enter a string: ")

# Input for Float
float_input_str = input("Enter a float: ")
my_float = float(float_input_str)

# Input for Boolean
# Boolean input is handled by checking for "True" or "False" strings
bool_input_str = input("Enter a boolean (True/False): ")
my_boolean = bool_input_str.lower() == "true" 

# Input for Complex Number
complex_input_str = input("Enter a complex number (e.g., 3+5j): ")
my_complex = complex(complex_input_str)

print(f"\nData types:")
print(f"Integer: {type(my_int)}")
print(f"String: {type(my_string)}")
print(f"Float: {type(my_float)}")
print(f"Boolean: {type(my_boolean)}")
print(f"Complex: {type(my_complex)}")