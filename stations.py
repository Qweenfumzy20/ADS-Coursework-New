import pandas as pd

stations = pd.read_excel('London_stations.xlsx', header=None)

unique_stations = stations[1].unique().tolist()

print(unique_stations)

