import psutil
from injection import *


if __name__ == "__main__":
    inject_stress_cpu(duration=3, num_cpus=psutil.cpu_count())
    print("injected cpu")
    time.sleep(4)
    injection_stress_disk(duration=3, num_cpus=psutil.cpu_count())
    print("injected disk")
    # TODO vedere se il file in injection_stress_disk viene rimosso
