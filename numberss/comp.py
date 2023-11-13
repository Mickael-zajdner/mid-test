def sum_of_digits(number):
    # Convert the number to a string to iterate through its digits
    num_str = str(number)

    # Initialize a variable to store the sum of digits
    digit_sum = 0

    # Iterate through each digit and add it to the sum
    for digit in num_str:
        digit_sum += int(digit)

    # Return the final sum of digits
    return digit_sum

def ispal(number):
    # Convert the number to a string
    num_str = str(number)

    # Check if the reversed string is the same as the original
    return num_str == num_str[::-1]

