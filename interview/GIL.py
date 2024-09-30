"""
from threading import Thread
import time


def cpu_bound_task():
    # A CPU-bound task that keeps the CPU busy
    count = 0
    for _ in range(10 ** 7):
        count += 1


start_time = time.time()

# Create multiple threads
threads = [Thread(target=cpu_bound_task) for _ in range(4)]

# Start all threads
for thread in threads:
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

end_time = time.time()
print(f"Time taken with threads: {end_time - start_time:.2f} seconds")

"""

from multiprocessing import Process
import time


def cpu_bound_task():
    # A CPU-bound task that keeps the CPU busy
    count = 0
    for _ in range(10 ** 7):
        count += 1


start_time = time.time()

# Create multiple processes
processes = [Process(target=cpu_bound_task) for _ in range(4)]

# Start all processes
for process in processes:
    process.start()

# Wait for all processes to finish
for process in processes:
    process.join()

end_time = time.time()
print(f"Time taken with processes: {end_time - start_time:.2f} seconds")
