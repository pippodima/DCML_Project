import psutil
import time
from injection import inject_stress_cpu
from injection import injection_stress_disk


if __name__ == "__main__":
    print("injecting cpu")
    inject_stress_cpu(duration=3, num_cpus=psutil.cpu_count())
    time.sleep(3)
    print("injecting disk")
    injection_stress_disk(duration=3, num_cpus=psutil.cpu_count())
