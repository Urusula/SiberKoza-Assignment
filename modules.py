""" A module is basically a file containing a set of functions to include in your application. There are core python modules,
modules you can install using the pip package manager (including Django) as well as custom modules"""

import datetime
from datetime import date
import time
from time import time


today=date.today()
print(today)

timestamp=time()
print(timestamp)