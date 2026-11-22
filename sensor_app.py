import csv

#--------- Start of Functions to be implemented -----------------------

def get_hottest_reading(readings):
     hottest=None
     for data in readings:
         if  hottest is None or hottest['temperature'] < data['temperature']:
             hottest=data
     return hottest

def filter_by_location(readings, location):
    # REQ-02: Return a list of reading dictionaries matching the given location.
    # If none match or readings is empty, return an empty list [].
    filter = []
    for data in readings:
        if data['location'] == location:
            filter.append(data)
    return filter

def calc_average_temp(readings):
    # REQ-03: Return the average temperature (float) across all readings.
    # If readings is empty, return 0.
    total = 0
    if len(readings) == 0:
        return 0
    for data in readings:
        total +=data['temperature']
    return total/len(readings)

#--------- End of Functions to be implemented -------------------------

def load_readings():
    readings = []
    with open('readings.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            readings.append({
                'sensor_id': row['sensor_id'],
                'location': row['location'],
                'temperature': float(row['temperature'])
            })
    return readings

def main():
    readings = load_readings()
    while True:
        print("\n--- IoT Sensor Logger ---")
        print("1 - Display all readings")
        print("2 - Display hottest reading")
        print("3 - Filter by location")
        print("4 - Display average temperature")
        print("Q - Quit")
        choice = input("Enter selection => ").strip().upper()

        if choice == '1':
            for r in readings:
                print(r)
        elif choice == '2':
            print("Hottest:", get_hottest_reading(readings))
        elif choice == '3':
            loc = input("Enter location: ").strip()
            print("Matches:", filter_by_location(readings, loc))
        elif choice == '4':
            print(f"Average Temp: {calc_average_temp(readings):.2f} C")
        elif choice == 'Q':
            break

if __name__ == "__main__":
    main()