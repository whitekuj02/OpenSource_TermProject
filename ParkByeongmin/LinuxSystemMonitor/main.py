from monitor import get_cpu_usage

def main():
    print("=== Linux System Monitor ===")
    print("CPU Monitoring Started")
    print("Press Ctrl+C to stop.\n")

    try:
        while True:
            cpu = get_cpu_usage()
            print(f"CPU Usage: {cpu:.1f}%")

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    main()
