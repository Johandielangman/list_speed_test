import numpy as np
import time
from functools import wraps
import tracemalloc


def performance_check(func, rep=3):
    """Measure performance of a function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        memory_usage_results = []
        peak_memory_usage_results = []
        duration_results = []

        for _ in range(rep):
            tracemalloc.start()
            start_time = time.perf_counter()
            res = func(*args, **kwargs)
            duration = time.perf_counter() - start_time
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            memory_usage_results.append(current / 10**6)
            peak_memory_usage_results.append(peak / 10**6)
            duration_results.append(duration)

        print(f'\nRepeating function:         {rep} times'
              f"\nFunction:                   {func.__name__}"
              f"\nMemory usage (Ave):         {np.average(memory_usage_results):.6f} ± {np.std(memory_usage_results):.6f} MB"
              f"\nPeak memory usage (Ave):    {np.average(peak_memory_usage_results):.6f} ± {np.std(peak_memory_usage_results):.6f} MB"
              f"\nDuration(Ave):              {np.average(duration_results):.6f} ± {np.std(duration_results):.6f} sec"
              f"\n{'-'*40}"
              )
        return res
    return wrapper


@performance_check
def python_list(length=3000):
    python_list = []

    for i in range(length):
        python_list.append(i)

    return python_list


@performance_check
def numpy_list(length=3000):
    numpy_list = np.zeros(length)

    for i in range(length):
        numpy_list[i] = i

    return numpy_list


@performance_check
def comprehension_list(length=3000):
    comprehension_list = [i for i in range(length)]

    return list(comprehension_list)


if __name__ == "__main__":

    comprehension_list_result = comprehension_list(10**6)
    time.sleep(5)
    python_list_result = python_list(10**6)
    time.sleep(5)
    numpy_list_result = numpy_list(10**6)
    
    

    print("done.")
