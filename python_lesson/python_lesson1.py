def days_to_units(number_of_days, to_units=24, name_of_units="hours"):
    return f"{number_of_days} days are {number_of_days * to_units} {name_of_units}"

user_input = input("Enter number of days:\n")

def validate_and_execute(user_input, to_units=24, name_of_units="hours"):
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, to_units, name_of_units)
            print(calculated_value)
        elif user_input_number == 0 :
            return f"Number is 0"
    else:
        print(f"User input is not a digit")

validate_and_execute(user_input, 24*60*60, "seconds")
