import multiprocessing
import time


def stress_cpu(x):
    while True:
        x * x


def inject_stress_cpu(duration=2, num_cpus=8):
    processes = []
    for i in range(num_cpus):
        process = multiprocessing.Process(target=stress_cpu, args=(i,))
        processes.append(process)
        process.start()
    time.sleep(duration)
    for process in processes:
        process.terminate()


def stress_disk():
    pass
