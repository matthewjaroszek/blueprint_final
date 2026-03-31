from config import *
import sqlite3 as sql

nc('rc', 'location_name', 'city')
nc('rc', 'last_updated_epoch', 'last_update_unix')
nc('rc', 'last_update', 'last_update')
nc('rc', 'condition_text', 'weather_condition')
nc('rc', 'wind_degree', 'wind_dir_degree')
nc('rc', 'wind_direction', 'wind_dir_compass')
nc('rc', 'cloud', 'cloud_cover')
nc('rc', 'air_quality_Carbon_Monoxide', 'aq_co2')
nc('rc', 'air_quality_Ozone', 'aq_ozone')
nc('rc', 'air_quality_Nitrogen_dioxide', 'aq_no2')
nc('rc', 'air_quality_Sulphur_dioxide', 'aq_so2')
nc('rc', 'air_quality_us-epa-index', 'aq_us_epa')
nc('rc', 'air_quality_gb-defra-index', 'aq_gb_defra')

nc('dc', 'datetime', 'date')
nc('dc', 'tempmax', 'temp_max_celsius')
nc('dc', 'tempmin', 'temp_min_celsius')
nc('dc', 'feelslikemax', 'feels_max_celsius')
nc('dc', 'feelslikemin', 'feels_min_celsius')
nc('dc', 'feelslike', 'feels_like_celsius')
nc('dc', 'precipprob', 'precip_prob')
nc('dc', 'preciptype', 'precip_type')
nc('dc', 'snowdepth', 'snow_depth')
nc('dc', 'windgust', 'instant_wind_speed')
nc('dc', 'windspeed', 'max_wind_speed')
nc('dc', 'winddir', 'wind_dir')
nc('dc', 'sealevelpressure', 'sea_level_pressure_mb')
nc('dc', 'cloudcover', 'cloud_cover')
nc('dc', 'solarradiation', 'solar_radiation')
nc('dc', 'solarenergy', 'solar_energy')
nc('dc', 'uvindex', 'uv_index')
nc('dc', 'severerisk', 'storm_risk')
nc('dc', 'conditions', 'weather_condition')





"""
n = 50
df = getdf('rc').head(n)
df.to_csv("trc.gz", index = False)
df = getdf('dc').head(n)
df.to_csv("tdc.gz", index = False)

for csv in csvs:
    df = getdf(csv)
    conn = sql.connect(f'{csv}.db')
    df.to_sql(f'{csv}', conn, if_exists='replace')
    conn.close
    """