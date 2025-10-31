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

# List of query stations
query_stations = ['Ealing Broadway', 'Acton Main Line', 'Paddington', 'Bond Street', 'Tottenham Court Road']

# Loop through each station in the query list and check if it's operational in the hash table
for query_station in query_stations:
    # Use if statement to check if the station is in the set (hash table)
    if query_station in operational_stations:
        print(f"{query_station} is operational.")
    else:
        print(f"{query_station} is not operational.")

