from monitor import (
    get_cpu_usage,
    get_memory_usage,
    get_disk_usage
)

def main():
    print("=== Linux System Monitor ===")
    print("System Monitoring Started")
    print("Press Ctrl+C to stop.\n")

    try:
        while True:
            cpu = get_cpu_usage()
            memory = get_memory_usage()
            disk = get_disk_usage()

            print(
                f"CPU: {cpu:.1f}% | "
                f"RAM: {memory:.1f}% | "
                f"DISK: {disk:.1f}%"
            )

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    main()