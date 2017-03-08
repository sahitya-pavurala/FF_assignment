import re


def convert(input_string):
    """
    Method to convert string to int/float
    if it can be converted
    :param input_string: string input
    :return: float/int value of input_string
    """
    if re.match("^\d+?\.\d+?$", input_string) is not None:
        return float(input_string)
    elif re.match(r"[-+]?\d+$", input_string):
        return int(input_string)
    return input_string

