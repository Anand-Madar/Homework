#!/usr/bin/env python
# coding: utf-8


import pandas as pd



zones_url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv"


df_zones = pd.read_csv(zones_url)



df_zones.head()



# Download the parquet file directly to your Codespace
# Read directly from the URL instead of a local file
parquet_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet"
df_green = pd.read_parquet(parquet_url)


df_green.head()


df_green.info()



from sqlalchemy import create_engine

# Creates a bridge between Pandas and your database running on the host network.
# Format: dialect://username:password@host:port/database_name
engine = create_engine('postgresql://postgres:postgres@db:5432/ny_taxi')


# In[8]:


# Pushes the zones DataFrame into a Postgres table named 'taxi_zones'
# if_exists='replace' ensures it overwrites any existing table with the same name.
df_zones.to_sql(name='taxi_zones', con=engine, if_exists='replace', index=False)

# Pushes the green trips DataFrame into a table named 'green_taxi_trips'
df_green.to_sql(name='green_taxi_trips', con=engine, if_exists='replace', index=False)

print("Data successfully ingested into PostgreSQL!")





