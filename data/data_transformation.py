import pandas as pd

# specify columns
pickup_columns = ['pickup_datetime', 'pickup_longitude', 'pickup_latitude']
dropoff_columns = ['dropoff_datetime', 'dropoff_longitude', 'dropoff_latitude']

df = pd.read_csv('train.csv',  usecols=pickup_columns)
df['cat'] = 'pickup'
df2 = pd.read_csv('train.csv',  usecols=dropoff_columns)
df2['cat'] = 'dropoff'

df.rename(columns={'pickup_datetime': 'datetime', 'pickup_longitude': 'longitude', 'pickup_latitude': 'latitude'}, inplace=True)
df2.rename(columns={'dropoff_datetime': 'datetime', 'dropoff_longitude': 'longitude', 'dropoff_latitude': 'latitude'}, inplace=True)
# merge two dataframes
combined = pd.concat([df, df2])
# write to a new csv file
combined.to_csv('new_york_taxi_trips.csv')
print(combined.count())