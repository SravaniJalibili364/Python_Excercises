'''Write a Python program to find the available built-in modules.'''

#sys module provides various functions and variables that are used to manipulate different parts of the Python runtime environment.
import sys
built_in_functions = sys.builtin_module_names
print(built_in_functions)