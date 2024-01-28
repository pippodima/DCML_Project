import psutil
import time
from injection import inject_stress_cpu
from injection import injection_stress_disk
from injection import injection_stress_memory


if __name__ == "__main__":
    print("injecting cpu")
    inject_stress_cpu(duration=3, num_cpus=psutil.cpu_count())
    time.sleep(4)
    print("injecting disk")
    injection_stress_disk(duration=3, num_cpus=psutil.cpu_count())

    print("injecting memory stress")
    injection_stress_memory(duration=3, verbose=True, memoryGB=1)
