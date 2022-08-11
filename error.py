error_name = "the age is negative"


def get_user_age():
    age_to_check = int(input("enter your aga: "))
    if age_to_check < 0:
        raise ValueError(error_name)
    return age_to_check


try:
    print(get_user_age())
except ValueError as e:
    print(e.args)
    get_user_age()