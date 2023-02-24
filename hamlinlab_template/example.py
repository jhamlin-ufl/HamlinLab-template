'''
This is a sample module.  You can put functions here instead of in your
notebook in order to declutter the notebook.

In your notebook, you would need a line like:
    import hamlinlab_template.example

Then you'd be able to do:
    hamlinlab_template.example.hello('James')
'''

# You may need to import things here if you use them in this file.
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

def hello(name='there'):
    '''
    Say hello.
    A test function.

    arguments:
    name -- Who are we greeting (default 'there')
    '''
    return f"Hello {name}!"
