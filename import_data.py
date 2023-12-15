import cdsapi
import xarray as xr
#import pygrib
import pandas as pd
import netCDF4 as nc

c = cdsapi.Client(url="https://cds.climate.copernicus.eu/api/v2", key="264462:059a1953-be2a-4bc1-abcc-e3002aaa1766")

c.retrieve(
    'sis-temperature-statistics',
    {
        'format': 'zip',
        'variable': 'maximum_temperature',
        'period': 'year',
        'statistic': [
            '95th_percentile', 'time_average',
        ],
        'experiment': 'rcp8_5',
        'ensemble_statistic': 'ensemble_members_average',
    },
    'download.zip')



# # Open the downloaded GRIB file using pygrib
# grbs = pygrib.open('download.grib')

# # Access the specific message you want
# grb = grbs[1]  # Replace 1 with the appropriate message number

# # Access the data as a NumPy array
# data = grb.values

# # Close the GRIB file
# grbs.close()
# print(data)
# df = pd.DataFrame(data)

# # Define the CSV file name
# csv_filename = 'data_sample.csv'

# # Save the DataFrame to a CSV file
# df.to_csv(csv_filename, index=False)

# print(f'Data exported to {csv_filename}')