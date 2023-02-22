'''
Various convenience modules for data analysis in the Hamlin Laboratory.
'''

import pathlib
import os
from hamlinlab_template.config import *
import hamlinlab_template.mplstyle

cwd = pathlib.Path.cwd() # The current working directory
project_root = cwd.parent
