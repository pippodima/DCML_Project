import psutil
from injection import *


if __name__ == "__main__":
    inject_stress_cpu(duration=2, num_cpus=psutil.cpu_count())
