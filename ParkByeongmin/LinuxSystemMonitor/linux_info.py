import platform


previous_cpu = None


def is_linux():
    return platform.system() == "Linux"


def get_proc_cpu_usage():
    global previous_cpu

    with open("/proc/stat", "r") as file:
        values = file.readline().split()[1:]

    times = list(map(int, values[:8]))

    total = sum(times)
    idle = times[3] + times[4]

    if previous_cpu is None:
        previous_cpu = (total, idle)
        return None

    total_diff = total - previous_cpu[0]
    idle_diff = idle - previous_cpu[1]

    previous_cpu = (total, idle)

    if total_diff <= 0:
        return None

    return (1 - idle_diff / total_diff) * 100


def get_proc_memory_usage():

    memory = {}

    with open("/proc/meminfo", "r") as file:

        for line in file:
            key, value = line.split(":", 1)
            memory[key] = int(value.split()[0])

    total = memory["MemTotal"]
    available = memory["MemAvailable"]

    return (total - available) / total * 100


def get_proc_uptime():

    with open("/proc/uptime", "r") as file:
        uptime = int(float(file.read().split()[0]))

    hours = uptime // 3600
    minutes = (uptime % 3600) // 60
    seconds = uptime % 60

    return f"{hours}h {minutes}m {seconds}s"


def get_proc_load_average():

    with open("/proc/loadavg", "r") as file:
        return file.read().split()[:3]


def get_linux_info():

    if not is_linux():
        return None

    try:
        return {
            "cpu": get_proc_cpu_usage(),
            "memory": get_proc_memory_usage(),
            "uptime": get_proc_uptime(),
            "load": get_proc_load_average()
        }

    except (OSError, KeyError, ValueError):
        return None