def find_min(num1, num2, num3):
    """
    Method to find minimum of three numbers
    :param num1:
    :param num2:
    :param num3:
    :return:
    """
    minimum = num1 if num1 < num2 and num1 < num3 else (num2 if num2 < num3 else num3)
    return minimum

