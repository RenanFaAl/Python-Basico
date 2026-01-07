def validate_isbn(isbn, length):
    # Check length correctness
    if len(isbn) != length:
        print(f"ISBN-{length} code should be {length} digits long.")
        return

    # Validate characters
    if length == 10:
        if not (isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1] == 'X')):
            print("Invalid character was found.")
            return
    else:
        if not isbn.isdigit():
            print("Invalid character was found.")
            return

    main_digits = isbn[:-1]
    given_check_digit = isbn[-1]

    main_digits_list = [int(digit) for digit in main_digits]

    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    if given_check_digit == expected_check_digit:
        print("Valid ISBN Code.")
    else:
        print("Invalid ISBN Code.")


def calculate_check_digit_10(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)

    result = 11 - digits_sum % 11

    if result == 11:
        return '0'
    elif result == 10:
        return 'X'
    else:
        return str(result)


def calculate_check_digit_13(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit
        else:
            digits_sum += digit * 3

    result = 10 - digits_sum % 10

    if result == 10:
        return '0'
    else:
        return str(result)


def main():
    user_input = input("Enter ISBN and length: ")

    # Must be comma-separated
    if ',' not in user_input:
        print("Enter comma-separated values.")
        return

    values = user_input.split(',')

    if len(values) != 2:
        print("Enter comma-separated values.")
        return

    isbn = values[0]
    length_str = values[1]

    # Length must be numeric
    if not length_str.isdigit():
        print("Length must be a number.")
        return

    length = int(length_str)

    if length != 10 and length != 13:
        print("Length should be 10 or 13.")
        return

    validate_isbn(isbn, length)


# main()  ← COMENTADO para os testes funcionarem
