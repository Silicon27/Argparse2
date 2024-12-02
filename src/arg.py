# Remaking of the `argparse` module in Python 3.8.5

import sys
from helper import custom_syntax, usage_msg_gen

class Parser:
    def __init__(self):
        self.only_value = None
        self.target_kwarg = None
        self.target = None
        self.store_true = None
        self.nargs = None
        self.name = None
        self.short = None
        self.description = None
        self.help = None
        self.type = None
        self.allArguments = []
        self.arg_info = {}

    def add_argument(self, name, short, description: str = "", nargs: str = "", store_true: bool = False, argtype = None, nhelp: str = None, target=None, only_value=False, **kwargs):
        self.name = name
        self.allArguments.append(name)
        self.short = short
        self.allArguments.append(short)
        self.description = description
        self.nargs = nargs
        self.store_true = store_true
        self.type = argtype
        self.help = nhelp
        self.target = target
        self.target_kwarg = kwargs
        self.only_value = only_value

        self.arg_info[(self.name, self.short,)] = {
            "description": self.description,
            "nargs": self.nargs,
            "store_true": self.store_true,
            "type": self.type,
            "help": self.help,
            "target": self.target,
            "target_kwarg": self.target_kwarg,
            "only_value": self.only_value
        }

        # print(self.arg_info)

    def run(self):
        arguments = sys.argv[1:]
        for arg in arguments:
            if "." in arg:
                arg_value = self.print_argument_value_for_string(arg.split(".")[0])
                custom_syntax.dot(arg_value, arg)
                return
            arg_value = self.print_argument_value_for_string(arg)
            try:
                run = arg_value["target"]
            except KeyError:
                continue
            except TypeError:
                return
            if run:
                if arg_value["only_value"]:
                    run(*arg_value["target_kwarg"].values())
                else:
                    run(**arg_value["target_kwarg"])


    def print_argument_value_for_string(self, arg_string):
        for key in self.arg_info.keys():
            if arg_string in key:
                # print(f"Value associated with '{arg_string}': {self.arg_info[key]}")
                return self.arg_info[key]

        usage_msg = usage_msg_gen.usage_msg_gen(arg_string, self.arg_info, sys.argv[0])
        print(usage_msg)
        print(f"Error: Unrecognised Arguments: '{arg_string}'")


# def example(*args, **kwargs):
#     print(f"args: {args}, kwargs: {kwargs}")
#
# def example2(arg1, arg2):
#     print(f"arg1: {arg1}, arg2: {arg2}")
#
# myparser = Parser()
# myparser.add_argument('--example', '-e', description="Prints the help message",
#                       nhelp="Prints the help message", target=example, only_value=True,
#                       arg1="This is the help message", arg2="This is an extra message")
# myparser.add_argument('--example2', '-e2', description="Prints the help message",
#                       nhelp="Prints the help message", target=example2,
#                       arg1="This is the help message", arg2="This is an extra message")
#
# if __name__ == "__main__":
#     myparser.run()


