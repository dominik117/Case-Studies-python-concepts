# Conversions
decimal_number = 42

# Decimal to other systems
binary = bin(decimal_number)
octal = oct(decimal_number)
hexadecimal = hex(decimal_number)

# Back to decimal
back_to_decimal_from_binary = int(binary, 2)
back_to_decimal_from_octal = int(octal, 8)
back_to_decimal_from_hex = int(hexadecimal, 16)

# Bitwise operations
bitwise_and = decimal_number & 15  # AND operation with 15 (0b1111)
bitwise_or = decimal_number | 15  # OR operation with 15 (0b1111)
bitwise_xor = decimal_number ^ 15 # XOR operation with 15 (0b1111)

# Output
print("Decimal:", decimal_number)
print("Binary:", binary)
print("Octal:", octal)
print("Hexadecimal:", hexadecimal)
print("Back to Decimal from Binary:", back_to_decimal_from_binary)
print("Back to Decimal from Octal:", back_to_decimal_from_octal)
print("Back to Decimal from Hex:", back_to_decimal_from_hex)
print("Bitwise AND:", bitwise_and)
print("Bitwise OR:", bitwise_or)
print("Bitwise XOR:", bitwise_xor)


a = 12  # In binary: 1100
b = 5   # In binary: 0101

# XOR operation
result = a ^ b  # This will be 1100 XOR 0101 = 1001 (which is 9 in decimal)

print("Result of XOR between", a, "and", b, "is:", result)
