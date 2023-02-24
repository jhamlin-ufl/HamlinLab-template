'''
Some convenient configuration options.
Here we define some directories that we may use
for loading or saving data.

In a notebook you could do e.g.:
from config import (
    pub_ready_dir,
    external_data_dir,
    processed_data_dir,
    raw_data_dir
    )
'''

import pathlib
import os

# __all__ specifies which things to import when using from config import *
__all__ = [
    'project_root',
    'pub_ready_dir',
    'external_data_dir',
    'processed_data_dir',
    'raw_data_dir',
    'cwd'
    ]

cwd = pathlib.Path.cwd() # The current working directory
project_root = cwd.parent

# Various useful directories
pub_ready_dir = project_root / 'publication_ready'
external_data_dir = project_root / 'data' / 'external'
processed_data_dir = project_root / 'data' / 'processed'
raw_data_dir = project_root / 'data' / 'raw'

