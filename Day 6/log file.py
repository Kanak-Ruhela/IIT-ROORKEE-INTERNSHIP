error_counts = {}
try:
    with open("server.log", "r") as file:
        for line in file:
            if "ERROR" in line:
                parts = line.split("ERROR:")
                if len(parts) > 1:
                    error_type = parts[1].strip().split()[0]
                    if error_type in error_counts:
                        error_counts[error_type] += 1
                    else:
                        error_counts[error_type] = 1
    print("\n--- Log Analysis Report ---")
    if not error_counts:
        print("No errors found in the log file!")
    else:
        for error, count in error_counts.items():
            print(f"{error}: {count} times")
except FileNotFoundError:
    print("Error: The log file 'server.log' was not found.")

