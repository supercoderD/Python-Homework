def decimal_to_binary(n):
    # Handle the edge case for 0
    if n == 0:
        return "0"
    
    binary_str = ""
    while n > 0:
        remainder = n % 2           # Get the remainder (0 or 1)
        binary_str = str(remainder) + binary_str  # Add to the front of the string
        n = n // 2                  # Integer division to get the next quotient
        
    return binary_str

# Example usage
decimal_num = 10
print(f"The binary of {decimal_num} is {decimal_to_binary(decimal_num)}")
