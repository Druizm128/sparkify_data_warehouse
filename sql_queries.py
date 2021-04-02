import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE staging_events;"
staging_songs_table_drop = "DROP TABLE staging_songs;"
songplay_table_drop = "DROP TABLE songplay;"
user_table_drop = "DROP TABLE users;"
song_table_drop = "DROP TABLE songs;"
artist_table_drop = "DROP TABLE artists;"
time_table_drop = "DROP TABLE time;"

# CREATE TABLES

staging_events_table_create= ("""
CREATE TABLE staging_events (
    artist CHARACTER NOT NULL,
    auth CHARACTER NOT NULL,
    firstName CHARACTER NOT NULL,
    gender CHARACTER NOT NULL,
    itemInSession INT NOT NULL,
    lastName CHARACTER NOT NULL,
    length FLOAT,
    level CHARACTER NOT NULL,
    location CHARACTER NOT NULL,
    method CHARACTER NOT NULL,
    page CHARACTER NOT NULL,
    registration INT NOT NULL,
    sessionId INT NOT NULL,
    song CHARACTER NOT NULL,
    status INT NOT NULL,
    ts INT NOT NULL,
    userAgent CHARACTER NOT NULL,
    userId INT NOT NULL,
);
""")

staging_songs_table_create = ("""
CREATE TABLE staging_songs (
    num_songs INT NOT NULL,
    artist_id CHARACTER NOT NULL,
    artist_latitude FLOAT,
    artist_longitude FLOAT,
    artist_location CHARACTER NOT NULL,
    artist_name CHARACTER NOT NULL,
    song_id CHARACTER NOT NULL,
    title CHARACTER NOT NULL,
    duration FLOAT NOT NULL,
    year INT NOT NULL
);
""")

songplay_table_create = ("""
CREATE TABLE songplay (
    "songplay_id" INT IDENTITY(0,1),
    "start_time" TIMESTAMP,
    "user_id" INT NOT NULL,
    "level" CHARACTER NOT NULL,
    "song_id" CHARACTER NOT NULL,
    "artist_id" CHARACTER NOT NULL,
    "session_id",
    "location" CHARACTER NOT NULL,
    "user_agent" CHARACTER NOT NULL
);
""")

user_table_create = ("""
CREATE TABLE users (
    "user_id" INT IDENTITY(0,1),
    "first_name" CHARACTER NOT NULL,
    "last_name"  CHARACTER NOT NULL,
    "gender"  CHARACTER NOT NULL,
    "level" CHARACTER NOT NULL
);
""")

song_table_create = ("""
CREATE TABLE songs (
    "song_id" CHARACTER NOT NULL,
    "title" CHARACTER NOT NULL,
    "artist_id" CHARACTER NOT NULL,
    "year" INT NOT NULL,
    "duration" FLOAT NOT NULL
);
""")

artist_table_create = ("""
CREATE TABLE artists (
    "artist_id" CHARACTER NOT NULL,
    "name" CHARACTER NOT NULL,
    "location" CHARACTER NOT NULL,
    "latitude" FLOAT,
    "longitude" FLOAT
);
""")

time_table_create = ("""
CREATE TABLE time (
    "start_time" TIMESTAMP NOT NULL,
    "hour" INT NOT NULL,
    "day" INT NOT NULL,
    "week" INT NOT NULL,
    "month" INT NOT NULL,
    "year" INT NOT NULL,
    "weekday" INT NOT NULL 
);
""")

# STAGING TABLES

staging_events_copy = ("""
""").format()

staging_songs_copy = ("""
""").format()

# FINAL TABLES

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")

time_table_insert = ("""
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
