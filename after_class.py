def binarytodecimal(binary_str):
    result = 0

    length = len(binary_str)

    for i in range(length):

        result += int(binary_str[i]) * (2 ** (length - 1 - i))
    
    return result

binary_input = input("Enter a binary number: ")

print("The decimal value is:", binarytodecimal(binary_input))
