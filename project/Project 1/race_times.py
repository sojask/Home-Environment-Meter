import sys

def get_race_data(file_name):
    try:
        file = open(file_name, 'r')
        location = file.readline().strip()
        driver_times = {}

        for line in file:
            driver_id = line[:3]
            lap_time = line[3:]

            try:
                lap_time = float(lap_time)
            except ValueError:
                print(f"Invalid lap time format for driver {driver_id}")
                continue

            if driver_id not in driver_times:
                driver_times[driver_id] = []

            driver_times[driver_id].append(lap_time)
        file.close()

        print(f"The race today is in {location}")

        fastest_driver = None
        fastest_time = float('inf')
        slowest_driver = None
        slowest_time = float('-inf')

        for driver in driver_times:
            times = driver_times[driver]
            driver_fastest = min(times)
            driver_slowest = max(times)

            if driver_fastest < fastest_time:
                fastest_time = driver_fastest
                fastest_driver = driver

            if driver_slowest > slowest_time:
                slowest_time = driver_slowest
                slowest_driver = driver

        print(f"The fastest driver is {fastest_driver}, with a time of {fastest_time:.3f} seconds")
        print(f"The slowest driver is {slowest_driver}, with a time of {slowest_time:.3f} seconds")

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python racetimes.py <filename>")
    else:
        file_name = sys.argv[1]
        get_race_data(file_name)
