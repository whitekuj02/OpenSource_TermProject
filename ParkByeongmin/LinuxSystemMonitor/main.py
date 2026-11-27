import os
from datetime import datetime

from monitor import (
    get_cpu_usage,
    get_memory_usage,
    get_disk_usage,
    get_top_processes,
    check_alerts
)

from logger import save_log
from linux_info import get_linux_info


def main():

    try:
        while True:

            # LAB 01, 02: System Monitoring
            cpu = get_cpu_usage()
            memory = get_memory_usage()
            disk = get_disk_usage()

            # LAB 03: Process Monitoring
            processes = get_top_processes(5)

            # LAB 04: Threshold Alerts
            alerts = check_alerts(cpu, memory, disk)

            # LAB 05: CSV Logging
            save_log(cpu, memory, disk, alerts)

            # LAB 06: Linux /proc Parsing
            linux = get_linux_info()

            # Clear Terminal
            os.system('cls' if os.name == 'nt' else 'clear')

            print("=" * 55)
            print("              Linux System Monitor")
            print("=" * 55)

            print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            print("Press Ctrl+C to stop.\n")

            # System Resources
            print("=== SYSTEM RESOURCES ===")
            print(f"CPU:  {cpu:.1f}%")
            print(f"RAM:  {memory:.1f}%")
            print(f"DISK: {disk:.1f}%")

            # Process Information
            print("\n=== TOP 5 CPU PROCESSES ===")

            print(
                f"{'PID':<8}"
                f"{'NAME':<25}"
                f"{'CPU(%)':>10}"
                f"{'RAM(%)':>10}"
            )

            print("-" * 53)

            for proc in processes:

                name = proc['name'] or "Unknown"

                print(
                    f"{proc['pid']:<8}"
                    f"{name[:24]:<25}"
                    f"{proc['cpu_percent']:>10.1f}"
                    f"{(proc['memory_percent'] or 0):>10.1f}"
                )

            # Warning Messages
            print("\n=== SYSTEM ALERTS ===")

            if alerts:
                for alert in alerts:
                    print(alert)

            else:
                print("All resources are normal.")

            # Linux Kernel Information
            print("\n=== LINUX KERNEL INFORMATION ===")

            if linux:

                if linux['cpu'] is None:
                    print("/proc CPU: Calculating...")
                else:
                    print(f"/proc CPU: {linux['cpu']:.1f}%")

                print(f"/proc RAM: {linux['memory']:.1f}%")
                print(f"Uptime: {linux['uptime']}")
                print(f"Load Average: {' / '.join(linux['load'])}")

            else:
                print("Linux /proc information unavailable.")

            # Log Status
            print("\n[LOG] Saved to system_log.csv")

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")


if __name__ == "__main__":
    main()