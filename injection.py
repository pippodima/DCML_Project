import multiprocessing
import os
import random
import string
import tempfile
import time


def stress_cpu(x=123456):
    while True:
        x * x


def inject_stress_cpu(duration=5, verbose=False, num_cpus=1):
    processes = []
    for i in range(num_cpus):
        process = multiprocessing.Process(target=stress_cpu, args=(i,))
        processes.append(process)
        process.start()
    time.sleep(duration)
    for process in processes:
        process.terminate()
    if verbose: print("terminated cpu stress")


def stress_disk(writing_times=10):
    while True:
        writing_string = ''.join(random.choices(string.ascii_letters + string.digits, k=1024))
        with tempfile.NamedTemporaryFile() as temp_file:
            for _ in range(writing_times):
                temp_file.write(writing_string.encode('utf-8'))
            temp_file.seek(0)
            temp_file.read()


def injection_stress_disk(duration=5, verbose=False, num_cpus=1, writing_times=10):
    processes = []
    for i in range(num_cpus):
        process = multiprocessing.Process(target=stress_disk, args=(writing_times,))
        processes.append(process)
        process.start()
    time.sleep(duration)
    for process in processes:
        process.terminate()
    if verbose: print("terminated disk stress")


def stress_memory(memoryGB=4, duration=5):
    num_elements = 1024 ** 3 * memoryGB // 4
    start_time = time.time()
    while True:
        temp = [[0] * 100 for _ in range(num_elements // 100)]
        if duration and (time.time() - start_time) >= duration:
            break


def injection_stress_memory(duration=5, verbose=False, memoryGB=4):
    stress_memory(memoryGB=memoryGB, duration=duration)
    if verbose: print("memory stress done")
