CREATE TABLE locations (
    location_id INTEGER PRIMARY KEY,
    country TEXT NOT NULL,
    location_name TEXT NOT NULL,
    latitude NUMERIC(8,2) NOT NULL,
    longitude NUMERIC(8,2) NOT NULL,
    timezone TEXT NOT NULL,
    UNIQUE (country, location_name, latitude, longitude, timezone)
);

CREATE TABLE weather_observations (
    observation_id INTEGER PRIMARY KEY,
    location_id BIGINT NOT NULL
        REFERENCES locations(location_id)
        ON DELETE CASCADE,

    last_updated_epoch BIGINT NOT NULL,
    --last_updated TIMESTAMP NOT NULL,

    --temperature_celsius NUMERIC(5,1),
    temperature_fahrenheit NUMERIC(5,1),
    condition_text TEXT,

    wind_mph NUMERIC(5,1),
    --wind_kph NUMERIC(5,1),
    wind_degree SMALLINT CHECK (wind_degree BETWEEN 0 AND 360),
    wind_direction VARCHAR(3),

    pressure_mb NUMERIC(6,1),
    --pressure_in NUMERIC(5,2),

    --precip_mm NUMERIC(6,1),
    precip_in NUMERIC(5,2),

    humidity SMALLINT CHECK (humidity BETWEEN 0 AND 100),
    cloud SMALLINT CHECK (cloud BETWEEN 0 AND 100),

    --feels_like_celsius NUMERIC(5,1),
    feels_like_fahrenheit NUMERIC(5,1),

    --visibility_km NUMERIC(5,1),
    visibility_miles NUMERIC(5,1),

    uv_index NUMERIC(4,1),

    gust_mph NUMERIC(5,1),
    --gust_kph NUMERIC(5,1),

    UNIQUE (location_id, last_updated_epoch)
);

CREATE TABLE air_quality_observations (
    observation_id BIGINT PRIMARY KEY
        REFERENCES weather_observations(observation_id)
        ON DELETE CASCADE,

    air_quality_carbon_monoxide NUMERIC(10,1),
    air_quality_ozone NUMERIC(10,1),
    air_quality_nitrogen_dioxide NUMERIC(10,1),
    air_quality_sulphur_dioxide NUMERIC(10,1),
    air_quality_pm2_5 NUMERIC(10,1),
    air_quality_pm10 NUMERIC(10,1),
    air_quality_us_epa_index SMALLINT,
    air_quality_gb_defra_index SMALLINT
);

CREATE TABLE astronomy_observations (
    observation_id BIGINT PRIMARY KEY
        REFERENCES weather_observations(observation_id)
        ON DELETE CASCADE,

    sunrise TIME,
    sunset TIME,
    moonrise TIME,
    moonset TIME,
    moon_phase TEXT,
    moon_illumination SMALLINT CHECK (moon_illumination BETWEEN 0 AND 100)
);

CREATE INDEX idx_weather_location_time
    ON weather_observations (location_id, last_updated_epoch);

--COMMENT ON COLUMN locations.country IS 'Country of the weather data';
--COMMENT ON COLUMN locations.location_name IS 'Name of the location (city)';
--COMMENT ON COLUMN locations.latitude IS 'Latitude coordinate of the location';
--COMMENT ON COLUMN locations.longitude IS 'Longitude coordinate of the location';
--COMMENT ON COLUMN locations.timezone IS 'Timezone of the location';

--COMMENT ON COLUMN weather_observations.last_updated_epoch IS 'Unix timestamp of the last data update';
--COMMENT ON COLUMN weather_observations.last_updated IS 'Local time of the last data update';
--COMMENT ON COLUMN weather_observations.temperature_celsius IS 'Temperature in degrees Celsius';
--COMMENT ON COLUMN weather_observations.temperature_fahrenheit IS 'Temperature in degrees Fahrenheit';
--COMMENT ON COLUMN weather_observations.condition_text IS 'Weather condition description';
--COMMENT ON COLUMN weather_observations.wind_mph IS 'Wind speed in miles per hour';
--COMMENT ON COLUMN weather_observations.wind_kph IS 'Wind speed in kilometers per hour';
--COMMENT ON COLUMN weather_observations.wind_degree IS 'Wind direction in degrees';
--COMMENT ON COLUMN weather_observations.wind_direction IS 'Wind direction as a 16-point compass';
--COMMENT ON COLUMN weather_observations.pressure_mb IS 'Pressure in millibars';
--COMMENT ON COLUMN weather_observations.pressure_in IS 'Pressure in inches';
--COMMENT ON COLUMN weather_observations.precip_mm IS 'Precipitation amount in millimeters';
--COMMENT ON COLUMN weather_observations.precip_in IS 'Precipitation amount in inches';
--COMMENT ON COLUMN weather_observations.humidity IS 'Humidity as a percentage';
--COMMENT ON COLUMN weather_observations.cloud IS 'Cloud cover as a percentage';
--COMMENT ON COLUMN weather_observations.feels_like_celsius IS 'Feels-like temperature in Celsius';
--COMMENT ON COLUMN weather_observations.feels_like_fahrenheit IS 'Feels-like temperature in Fahrenheit';
--COMMENT ON COLUMN weather_observations.visibility_km IS 'Visibility in kilometers';
--COMMENT ON COLUMN weather_observations.visibility_miles IS 'Visibility in miles';
--COMMENT ON COLUMN weather_observations.uv_index IS 'UV Index';
--COMMENT ON COLUMN weather_observations.gust_mph IS 'Wind gust in miles per hour';
--COMMENT ON COLUMN weather_observations.gust_kph IS 'Wind gust in kilometers per hour';

--COMMENT ON COLUMN air_quality_observations.air_quality_carbon_monoxide IS 'Air quality measurement: Carbon Monoxide';
--COMMENT ON COLUMN air_quality_observations.air_quality_ozone IS 'Air quality measurement: Ozone';
--COMMENT ON COLUMN air_quality_observations.air_quality_nitrogen_dioxide IS 'Air quality measurement: Nitrogen Dioxide';
--COMMENT ON COLUMN air_quality_observations.air_quality_sulphur_dioxide IS 'Air quality measurement: Sulphur Dioxide';
--COMMENT ON COLUMN air_quality_observations.air_quality_pm2_5 IS 'Air quality measurement: PM2.5';
--COMMENT ON COLUMN air_quality_observations.air_quality_pm10 IS 'Air quality measurement: PM10';
--COMMENT ON COLUMN air_quality_observations.air_quality_us_epa_index IS 'Air quality measurement: US EPA Index';
--COMMENT ON COLUMN air_quality_observations.air_quality_gb_defra_index IS 'Air quality measurement: GB DEFRA Index';

--COMMENT ON COLUMN astronomy_observations.sunrise IS 'Local time of sunrise';
--COMMENT ON COLUMN astronomy_observations.sunset IS 'Local time of sunset';
--COMMENT ON COLUMN astronomy_observations.moonrise IS 'Local time of moonrise';
--COMMENT ON COLUMN astronomy_observations.moonset IS 'Local time of moonset';
--COMMENT ON COLUMN astronomy_observations.moon_phase IS 'Current moon phase';
--COMMENT ON COLUMN astronomy_observations.moon_illumination IS 'Moon illumination percentage';