def is_armstrong_number(num):
    """
    Checks if a given number is an Armstrong number.
    
    An Armstrong number is a number that is equal to the sum of the cubes of its digits.
    
    Parameters:
    num (int): The number to check.
    
    Returns:
    bool: True if the number is an Armstrong number, False otherwise.
    """
    original_num = num
    sum_of_cubes = 0
    
    while num > 0:
        digit = num % 10
        sum_of_cubes += digit ** len(str(original_num))
        num //= 10
    
    return original_num == sum_of_cubes

# Example usage
user_input = int(input("Enter a number: "))
if is_armstrong_number(user_input):
    print(f"{user_input} is an Armstrong number.")
else:
    print(f"{user_input} is not an Armstrong number.")