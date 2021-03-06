# DROP TABLES

songplay_table_drop = "DROP Table if exists songplays"
user_table_drop = "DROP table if exists users"
song_table_drop = "DROP table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES

songplay_table_create = """
CREATE TABLE IF NOT EXISTS songplays(
    songplay_id serial PRIMARY KEY,
    start_time bigint not null,
    user_id text not null,
    level text,
    song_id text,
    artist_id text,
    session_id int,
    location text,
    user_agent text
    )
"""

user_table_create = """
CREATE TABLE IF NOT EXISTS users(
    user_id text PRIMARY KEY,
    first_name text not null,
    last_name text not null,
    gender text,
    level text
    )
"""

song_table_create = """
CREATE TABLE IF NOT EXISTS songs(
    song_id text PRIMARY KEY,
    title text,
    artist_id varchar NOT NULL,
    year int,
    duration decimal
    )
"""

artist_table_create = """
CREATE TABLE IF NOT EXISTS artists(
    artist_id text PRIMARY KEY,
    name text,
    location text,
    latitude decimal,
    logitude decimal
    )
"""

time_table_create = """
CREATE TABLE IF NOT EXISTS time(
    start_time time,
    hour int,
    day int,
    week int,
    month int,
    year int,
    weekday int
    )
"""

# INSERT RECORDS

songplay_table_insert = """
INSERT INTO songplays (
    start_time,
    user_id,
    level,
    song_id,
    artist_id,
    session_id,
    location,
    user_agent
    )
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

user_table_insert = """
INSERT INTO users(user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id)
DO UPDATE
    SET level = EXCLUDED.level;
"""

song_table_insert = """
INSERT INTO songs (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id)
DO NOTHING;
"""

artist_table_insert = """
INSERT INTO artists (artist_id, name, location, latitude, logitude)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id)
DO NOTHING;
"""


time_table_insert = """
insert into time (start_time, hour, day, week, month, year, weekday)
values (%s, %s, %s, %s, %s, %s, %s)
"""

# FIND SONGS

song_select = """
select song_id, artists.artist_id from songs
join artists on songs.artist_id = artists.artist_id
where songs.title = %s
and artists.name = %s and songs.duration = %s
"""

# QUERY LISTS

create_table_queries = [
    songplay_table_create,
    user_table_create,
    song_table_create,
    artist_table_create,
    time_table_create,
]
drop_table_queries = [
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop,
]
