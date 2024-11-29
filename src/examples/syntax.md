## Syntax

AdvancedArgs has some extra syntax separate from the traditional argparse syntax.

Given the following flag definition:
```python
from advanced_args import Parser

myparser = Parser()
myparser.add_argument('--help', '-h', description="Prints the help message", nhelp="Prints the help message")
myparser.run()
```

The user can in the terminal get the description explicitly with the following command:
```shell
python3 arg.py --help.d
```

The added `.d` at the end of the flag will print the description of the flag.

You can also use the `target` argument to specify a target function for the flag to run when it is called.
```python
from advanced_args import Parser
myparser = Parser()
myparser.add_argument('--callingtarget', '-c', description="Prints the help message", nhelp="Prints the help message", target=lambda: print("Hello World!"))
```

The user can then call the target function with the following command:
```shell
python3 arg.py --callingtarget
```
Only keyword arguments are allowed in the calling of the target function with custom arguments.

If you don't wish to have target arguments, or your target function does not take keyword arguments, you can use the `only_value` argument to specify that the target function should only take the value specified in the keyword arguments in the `.add_argument()` function.
```python
from advanced_args import Parser

def myfunc(value):
    print(value)

myparser = Parser()
myparser.add_argument('--callingtarget', '-c', description="Prints the help message", nhelp="Prints the help message", target=myfunc, only_value=True, myarg="Hello World!")
```
