"""
Used to generate the usage of the command line interface.

Example could be if you have declared a flag, then the generated usage would be:
Usage: mycli [--flag]/[-f]
"""

def usage_msg_gen(unrecognised_arg: str, arg_dict: dict, cli_name: str):
    result = f"Usage: {cli_name}: ["
    short = []
    long = []
    for key in arg_dict.keys():
        long.append(key[0])
        short.append(key[1])

    if short:
        for arg in long:
            result += f"{arg}/"
        result = result[:-1]
        result += "]"

    if long:
        result += "["
        for arg in short:
            result += f"{arg}/"
        result = result[:-1]
        result += "]"

    return result