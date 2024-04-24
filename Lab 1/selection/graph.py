import matplotlib.pyplot as plt
import numpy as np
import time
from selection  import selection

def time_vs_elements_selection(arrays):
    sizes = []
    times = []

    for arr in arrays:
        start_time = time.time()
        selection(arr)
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        
        sizes.append(len(arr))
        times.append(elapsed_time)
    
    return sizes, times

def generate_random_array(size):
    return np.random.rand(size)

def generate_best_case_array(size):
    return np.arange(1, size + 1)

def generate_worst_case_array(size):
    return np.arange(size, 0, -1)


max_size = 1000 
step = 50  
num_samples = 10  

best_case_arrays = [generate_best_case_array(size) for size in range(1, max_size + 1, step)]
worst_case_arrays = [generate_worst_case_array(size) for size in range(1, max_size + 1, step)]
average_case_arrays = [generate_random_array(size) for size in range(1, max_size + 1, step)]


best_case_sizes, best_case_times = time_vs_elements_selection(best_case_arrays)
worst_case_sizes, worst_case_times = time_vs_elements_selection(worst_case_arrays)
average_case_sizes, average_case_times = time_vs_elements_selection(average_case_arrays)


plt.plot(best_case_sizes, best_case_times, label='Best Case', marker='o', linestyle='-')
plt.plot(worst_case_sizes, worst_case_times, label='Worst Case', marker='o', linestyle='-')
plt.plot(average_case_sizes, average_case_times, label='Average Case', marker='o', linestyle='-')

plt.xlabel('Number of Elements')
plt.ylabel('Time (s)')
plt.title('Time vs Number of Elements (Selection Sort)')
plt.legend()
plt.grid(True)
plt.show()

