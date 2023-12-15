import psutil
import time
import csv


def monitor(path='', duration=None, **kwargs):  # interval and duration in seconds
    """
    Args:
        path: path in witch will be created file.csv
        duration: running time in seconds
        **kwargs: insert what parameter you want to monitor.
                  choose from:
                  CPU, MEMORY, DISK, NETWORK, PROCESSES, BATTERY (if on a laptop)
                  Example:
                      monitor(path = pathname, duration = 10, CPU=None, DISK=None)

    Returns: None

    """
    start_time = time.time()
    with open(path + 'monitoring_values.csv', "w+") as csvFile:
        fieldnames = ['TIMESTAMP'] + ",".join(kwargs.keys()).split(',')
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
        writer.writeheader()
        try:
            while True:
                time.sleep(1)
                # TODO scegliere il tipo di timestamp e capire come colorare l'output
                info = {'TIMESTAMP': time.time()}

                # CPU
                if "CPU" in kwargs.keys():
                    cpu_percent = psutil.cpu_percent()
                    print(f"CPU Usage: {cpu_percent}%")
                    print("--------------------------------")
                    info['CPU'] = cpu_percent


                # MEMORY
                if "MEMORY" in kwargs.keys():
                    memory_info = psutil.virtual_memory()
                    print(f"Total Memory: {memory_info.total} bytes")
                    print(f"Available Memory: {memory_info.available} bytes")
                    print(f"Used Memory: {memory_info.used} bytes")
                    print(f"Memory Usage Percentage: {memory_info.percent}%")
                    print("--------------------------------")

                # DISK
                if "DISK" in kwargs.keys():
                    disk_info = psutil.disk_usage('/')  # disk statistics about a path
                    print(f"Total Disk Space: {disk_info.total} bytes")
                    print(f"Used Disk Space: {disk_info.used} bytes")
                    print(f"Free Disk Space: {disk_info.free} bytes")
                    print(f"Disk Usage Percentage: {disk_info.percent}%")
                    print("--------------------------------")
                    # info['DISK'] = disk_info.percent
                    info['DISK'] = (psutil.disk_io_counters().read_bytes, psutil.disk_io_counters().write_bytes)


                # NETWORK
                if "NETWORK" in kwargs.keys():
                    network_info = psutil.net_io_counters()
                    print(f"Bytes Sent: {network_info.bytes_sent}")
                    print(f"Bytes Received: {network_info.bytes_recv}")
                    print("--------------------------------")

                # PROCESSES
                if "PROCESSES" in kwargs.keys():
                    for process in psutil.process_iter(['pid', 'name', 'username']):
                        print(process.info)
                    print("--------------------------------")

                # BATTERY
                if "BATTERY" in kwargs.keys():
                    battery_info = psutil.sensors_battery()
                    print(f"Battery Percent: {battery_info.percent}%")
                    print(f"Battery Power Plugged In: {battery_info.power_plugged}")
                    print("--------------------------------")
                    info['BATTERY'] = battery_info.percent

                writer.writerow(info)

                if duration and (time.time() - start_time) >= duration:
                    break

        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    # Monitor CPU usage for 10 seconds
    monitor(duration=10, CPU=None, BATTERY=None, DISK=None)
