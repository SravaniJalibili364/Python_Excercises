'''Print the name of the computer on which you are working.'''

#import os module ,this module provides modules for interacting with operating system
import os

#using uname will get the information about the currently running operating system
pc_name = os.uname()
#It will print username of the system
print(pc_name)