###################################
# !/usr/bin/python
# Python 3.10
# (C) 2023 admi.tech
###################################

# Import main packages


# Main Functions
def verify_card(data):
    """Simple function to validate credit card number based on Luhn algorithm.
    Returns Boolean ... True/False"""
    odd_sum = 0
    even = []
    even_sum = 0
    card_no_list = list(data)
    for (idx, val) in enumerate(card_no_list):
        if idx % 2 != 0:
            odd_sum += int(val)
        else:
            even.append(2 * int(val))
    even_string = ""
    for x in even:
        even_string += str(x)
    even_string_list = list(even_string)
    for (x, y) in enumerate(even_string_list):
        even_sum += int(y)

    total_sum = even_sum + odd_sum

    if total_sum % 10 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    sample_card_no = "5610591081018250"
    print(verify_card(sample_card_no))
