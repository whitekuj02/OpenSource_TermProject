import os

from monitor import (
    get_cpu_usage,
    get_memory_usage,
    get_disk_usage,
    get_top_processes
)

def main():
    try:
        while True:
            cpu = get_cpu_usage()
            memory = get_memory_usage()
            disk = get_disk_usage()
            processes = get_top_processes(5)

            os.system('cls' if os.name == 'nt' else 'clear')

            print("=== Linux System Monitor ===")
            print("Press Ctrl+C to stop.\n")

            print(f"CPU:  {cpu:.1f}%")
            print(f"RAM:  {memory:.1f}%")
            print(f"DISK: {disk:.1f}%")

            print("\n=== TOP 5 CPU Processes ===")

            print(f"{'PID':<8}{'NAME':<25}{'CPU(%)':>10}{'RAM(%)':>10}")
            print("-" * 53)

            for proc in processes:
                print(
                    f"{proc['pid']:<8}"
                    f"{proc['name'][:24]:<25}"
                    f"{proc['cpu_percent']:>10.1f}"
                    f"{(proc['memory_percent'] or 0):>10.1f}"
                )

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    main()