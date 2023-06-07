def password_strength(password):
    # Define the criteria for a strong password
    length_check = len(password) >= 8
    uppercase_check = any(char.isupper() for char in password)
    lowercase_check = any(char.islower() for char in password)
    digit_check = any(char.isdigit() for char in password)
    special_check = any(char.isalnum() == False for char in password)

    # Check the password strength based on the criteria
    if length_check and uppercase_check and lowercase_check and digit_check and special_check:
        return "Strong password"
    elif length_check and (uppercase_check or lowercase_check or digit_check):
        return "Medium password"
    else:
        return "Weak password"

# Prompt the user to enter a password
password = input("Enter your password: ")

# Check the strength of the password and display the result
strength = password_strength(password)
print("Password strength:", strength)
