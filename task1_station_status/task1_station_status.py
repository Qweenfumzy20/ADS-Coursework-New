stations = {"Victoria", "Oxford Circus", "King's Cross"}

def is_station_open(station):
    return station in stations

print(is_station_open("Victoria"))   # True
print(is_station_open("Paddinton"))  # False (misspelled)

Created Task 1 initial version – checks if station is open
