import datetime
import tables
from sapphire import esd
import pandas as pd

dir = 'coincidences\\'
DATAFILE = dir+'data.h5'
STATIONS = [501, 503, 506]
START = datetime.datetime(2016, 1, 1)
END = datetime.datetime(2016, 1, 2)


if __name__ == '__main__':
    if 'data' not in globals():
        data = tables.open_file(DATAFILE, 'a')

    if '/coincidences' not in data:
        esd.download_coincidences(data, stations=STATIONS, start=START, end=END)

print('-----------')
print(data)