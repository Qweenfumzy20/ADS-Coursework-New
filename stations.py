import pandas as pd

stations = pd.read_excel('London_stations.xlsx', header=None)

unique_stations = stations[1].unique().tolist()

print('Our unique stations are: ', unique_stations)



# List of station names from the dataset
stations = unique_stations

# Initializing the hash table (set in this case)
operational_stations = set()

# Populating the hash table with station names
for station in stations:
    operational_stations.add(station)

# Example of querying the hash table to check if a station is operational
query_station = 'Acton Main Line'
is_operational = query_station in operational_stations

print(f'Is {query_station} operational? {is_operational}')
