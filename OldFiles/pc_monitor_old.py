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
                  CPU, MEMORY, DISK, NETWORK, BATTERY (if on a laptop), MOUSE, KEYBOARD
                  Example:
                      monitor(path = pathname, duration = 10, CPU=None, DISK=None)

    Returns: None

    """
    fieldnames = ['TIMESTAMP']
    for arg in kwargs.keys():
        if arg == 'CPU':
            fieldnames.extend(['CPU_PERCENT'])
        if arg == 'MEMORY':
            fieldnames.extend(['MEMORY_USED', 'MEMORY_FREE', 'MEMORY_PERCENT'])
        if arg == 'DISK':
            fieldnames.extend(['DISK_USED', 'DISK_FREE', 'DISK_BYTE_READ', 'DISK_BYTE_WROTE'])
        if arg == 'NETWORK':
            fieldnames.extend(['NETWORK_BYTES_SENT', 'NETWORK_BYTES_RECV', 'NETWORK_ERRIN', 'NETWORK_ERROUT'])
        if arg == 'BATTERY':
            fieldnames.extend(['BATTERY_PERCENT', 'BATTERY_PLUGGED'])

    start_time = time.time()
    with open(path + 'monitored_values_old.csv', "w+") as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
        writer.writeheader()
        try:
            while True:
                time.sleep(1)
                info = {'TIMESTAMP': time.time_ns()}

                # CPU
                if "CPU" in kwargs.keys():
                    info['CPU_PERCENT'] = psutil.cpu_percent()

                # MEMORY
                if "MEMORY" in kwargs.keys():
                    info['MEMORY_USED'] = psutil.virtual_memory().used
                    info['MEMORY_FREE'] = psutil.virtual_memory().free
                    info['MEMORY_PERCENT'] = psutil.virtual_memory().percent

                # DISK
                if "DISK" in kwargs.keys():
                    info['DISK_USED'] = psutil.disk_usage('/').used
                    info['DISK_FREE'] = psutil.disk_usage('/').free
                    info['DISK_BYTE_READ'] = psutil.disk_io_counters().read_bytes
                    info['DISK_BYTE_WROTE'] = psutil.disk_io_counters().write_bytes

                # NETWORK
                if "NETWORK" in kwargs.keys():
                    info['NETWORK_BYTES_SENT'] = psutil.net_io_counters().bytes_sent
                    info['NETWORK_BYTES_RECV'] = psutil.net_io_counters().bytes_recv
                    info['NETWORK_ERRIN'] = psutil.net_io_counters().errin
                    info['NETWORK_ERROUT'] = psutil.net_io_counters().errout

                try:
                    # BATTERY
                    if "BATTERY" in kwargs.keys():
                        info['BATTERY_PERCENT'] = psutil.sensors_battery().percent
                        info['BATTERY_PLUGGED'] = psutil.sensors_battery().power_plugged
                except AttributeError:
                    print('il pc non supporta la batteria')
                    info['BATTERY_PERCENT'] = None
                    info['BATTERY_PLUGGED'] = None

                writer.writerow(info)

                if duration and (time.time() - start_time) >= duration:
                    break

        except KeyboardInterrupt:
            pass


