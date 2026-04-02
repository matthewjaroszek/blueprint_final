create table locations (
    id integer primary key,
    country text not null,
    city text not null,
    latitute real not null,
    longitute real not null,
    time_zone real not null
)

create table air_quality (
    id integer primary key,
    location_id integer not null,
    aq
)