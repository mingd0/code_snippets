import pandas as pd
import dateutil

INPUT_FILENAME = input("Enter input filename (.txt/.csv): ")
OUTPUT_FILENAME = input("Enter output filename (.csv): ")

df = pd.read_csv(INPUT_FILENAME,
                 parse_dates=[[0, 1]],
                 header=None,
                 names=['Date', 'Time', 'Pressure'],
                 usecols=[0, 1, 2],
                 index_col=['Date_Time'])

df = df.tz_localize(dateutil.tz.tzlocal())
df['Pressure'] = df['Pressure'].str.replace("\'", '')

df_out = df[['Pressure']]
df_out.to_csv(OUTPUT_FILENAME)

""" Unused code - did not end up being necessary.

df['_DateTime'] = df.index.strftime('%Y-%m-%dT%H:%M:%S.')

df['Milliseconds'] = df.index.strftime('%f')
df['Milliseconds'] = df['Milliseconds'].str[0:3]

df['Timezone'] = df.index.strftime('%z')
df['Timezone'] = df['Timezone'].str[0:3] + ':' + df['Timezone'].str[3:]
df['Date_Time_Final_Str'] = (df['_DateTime']
                             + df['Milliseconds']
                             + df['Timezone'])

"""
