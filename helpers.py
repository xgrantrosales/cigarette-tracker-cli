from datetime import datetime

# Validates integer input and allowed range.
def get_number(question, minimum_value, maximum_value=None):

    while True:

        user_input = input(question)

        try:
            number = int(user_input)

            if number < minimum_value:
                print(f"Please enter a number greater than or equal to {minimum_value}.")
                continue

            # Only checks maximum_value if one is provided.
            if maximum_value is not None and number > maximum_value:
                print(f"Please enter a number less than or equal to {maximum_value}.")
                continue

            return number
        
        except ValueError:
            print("Invalid input. Please enter a number.")

# Validates YYYY-MM-DD date format.
def get_valid_date(prompt):

    while True:

        user_input = input(prompt)

        try:
            datetime.strptime(user_input, "%Y-%m-%d")
            return user_input

        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD format.")




