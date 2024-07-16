def reverse_string(input_str):
    # Convert the string to a list of characters for easy manipulation
    char_list = list(input_str)

    # Initialize pointers for reversing
    start, end = 0, len(char_list) - 1

    # Swap characters while maintaining the position of punctuations and spaces
    while start < end:
        if not char_list[start].isalnum():
            start += 1
        elif not char_list[end].isalnum():
            end -= 1
        else:
            # Swap alphanumeric characters
            char_list[start], char_list[end] = char_list[end], char_list[start]
            start += 1
            end -= 1

    # Convert the list back to a string
    reversed_str = ''.join(char_list)
    
    return reversed_str

# Example usage
input_string = "Hello, World!"
result = reverse_string(input_string)
print("Original string:", input_string)
print("Reversed string:", result)
