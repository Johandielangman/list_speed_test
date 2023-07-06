import time
import pandas as pd
import numpy as np

def timeit(f):

    def timed(*args, **kwargs):
        start = time.time()
        for _ in range(100):
            f(*args, **kwargs)
        end = time.time()
        return end - start
    return timed

@timeit
def append_loop(n):
    """Simple loop with append"""
    my_list = []
    for i in range(n):
        my_list.append(0)

@timeit
def add_loop(n):
    """Simple loop with +="""
    my_list = []
    for i in range(n):
        my_list += [0]

@timeit   
def list_comprehension(n):        
    """List comprehension"""
    my_list = [0 for i in range(n)]

@timeit
def integer_multiplication(n):
    """List and integer multiplication"""
    my_list = [0] * n


@timeit
def numpy_array(n):
    my_list = np.zeros(n)
    

df = pd.DataFrame([(integer_multiplication(n), numpy_array(n)) for n in range(1000)], 
                  columns=['Integer multiplication', 'Numpy array'])
df.plot()