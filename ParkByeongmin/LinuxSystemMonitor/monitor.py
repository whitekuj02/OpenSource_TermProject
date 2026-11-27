import psutil

CPU_THRESHOLD = 80
RAM_THRESHOLD = 85
DISK_THRESHOLD = 90


def get_cpu_usage():
    return psutil.cpu_percent(interval=1)


def get_memory_usage():
    return psutil.virtual_memory().percent


def get_disk_usage():
    return psutil.disk_usage('/').percent


def get_top_processes(limit=5):
    processes = []

    for proc in psutil.process_iter(
        ['pid', 'name', 'cpu_percent', 'memory_percent']
    ):
        try:
            if proc.info['cpu_percent'] is not None:
                processes.append(proc.info)

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    processes = sorted(
        processes,
        key=lambda p: p['cpu_percent'],
        reverse=True
    )

    return processes[:limit]


def check_alerts(cpu, memory, disk):
    alerts = []

    if cpu >= CPU_THRESHOLD:
        alerts.append(f"WARNING: CPU usage {cpu:.1f}%")

    if memory >= RAM_THRESHOLD:
        alerts.append(f"WARNING: RAM usage {memory:.1f}%")

    if disk >= DISK_THRESHOLD:
        alerts.append(f"WARNING: DISK usage {disk:.1f}%")

    return alerts