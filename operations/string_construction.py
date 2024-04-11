# Simple string assignments
simple_string = "Hello, World!"  # A basic string
multi_line_string = """This is a
multi-line
string"""  # A multi-line string using triple quotes

# Concatenation of strings
concatenated = "Hello, " + "World!"  # Concatenating two strings with '+'

# String formatting using .format()
formatted_string = "{} {}".format("Hello", "World")  # Using .format() method for formatting

# Advanced string formatting (Python 3.6+)
name = "John"
age = 30
formatted_fstring = f"My name is {name} and I am {age} years old"  # Using f-string for formatting

# String formatting with dictionaries
data = {"name": "Jane", "age": 25}
formatted_dict_string = "Name: {name}, Age: {age}".format(**data)  # Unpacking a dictionary for formatting

# Formatting with numbers and precision
formatted_numbers = "Pi is approximately {:.2f}".format(3.14159)  # Formatting numbers with precision

# Raw strings (ignores escape characters like \n, \t, etc.)
raw_string = r"C:\Users\Name"  # Using 'r' before the string to make it raw

# Using join to concatenate a list of strings
string_list = ["Hello", "World"]
joined_string = " ".join(string_list)  # Joining a list of strings with a space

# Advanced: String interpolation (old style, less used)
interpolated_string = "Name: %s, Age: %d" % ("Alice", 28)  # Old style of string formatting

# String encoding and decoding
unicode_string = "こんにちは"  # A unicode string
encoded_string = unicode_string.encode('utf-8')  # Encoding to UTF-8
decoded_string = encoded_string.decode('utf-8')  # Decoding back to unicode

# Advanced: String manipulation using str.translate() and str.maketrans()
intab = "aeiou"
outtab = "12345"
transtab = str.maketrans(intab, outtab)
translated_string = "this is an example".translate(transtab)  # Translate vowels to numbers

# Display all the constructed strings
print(simple_string)
print(multi_line_string)
print(concatenated)
print(formatted_string)
print(formatted_fstring)
print(formatted_dict_string)
print(formatted_numbers)
print(raw_string)
print(joined_string)
print(interpolated_string)
print(unicode_string, "->", encoded_string, "->", decoded_string)
print(translated_string)
