def dot(arg_value, arg):
    new = arg.split(".")
    if new[1] == "d":
        print(arg_value["description"])
    elif new[1] == "n":
        print(arg_value["nargs"])
    elif new[1] == "help":
        print(arg_value["help"])
    elif new[1] == "type":
        print(arg_value["type"])
    elif new[1] == "t":
        print(arg_value["target"])

    else:
        print("Invalid argument")


