def print_hello(name, ex_name, greeting):
    """
    :param name:
    :param ex_name:
    :param greeting:
    :return:
    """
    if name != ex_name:
        print("%s %s" % greeting, name)


def multiply(x, y):
    result = x * y
    return result

bls = multiply(10, 4)

user_name = input("enter yuor names")
print(print_hello(user_name, "d", "hii"))
