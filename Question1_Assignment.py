import time
import matplotlib.pyplot as plt

# Naive iterative method
def power_iterative(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

# Divide-and-conquer method
def power_divide_conquer(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        time.sleep(0.1)
        temp = power_divide_conquer(base, exponent // 2)
        return temp * temp
    else:
        time.sleep(0.1)
        temp = power_divide_conquer(base, (exponent - 1) // 2)
        return base * temp * temp

# Experiment setup
#powers = list(range(1, 1**6 + 1))
powers= [1,2,100,1000,5000,10000,50000,100000,400000,800000,1000000]
iterative_times = []
divide_conquer_times = []

# Measure execution time for each power size
for power in range(len(powers)):
    start_time = time.time()
    power_iterative(2, powers[power])  # Replace 2 with the desired base number
    iterative_times.append(time.time() - start_time)
    
    print(powers[power])
    
    start_time = time.time()
    power_divide_conquer(2, powers[power])  # Replace 2 with the desired base number
    divide_conquer_times.append(time.time() - start_time)

# Plotting the results
plt.plot(powers, iterative_times, label='Iterative Method')
plt.plot(powers, divide_conquer_times, label='Divide and Conquer Method')
plt.xlabel('Power Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.legend()
plt.show()