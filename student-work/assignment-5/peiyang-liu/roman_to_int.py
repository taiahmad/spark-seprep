def roman_to_int(s: str) -> int:
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prev_value = 0
    
    for char in reversed(s):  # Iterate from right to left
        curr_value = roman_values[char]
        if curr_value < prev_value:
            total -= curr_value  # Subtract if smaller than previous value
        else:
            total += curr_value  # Otherwise, add to total
        prev_value = curr_value
    
    return total