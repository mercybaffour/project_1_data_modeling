# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = "CREATE TABLE songplays (songplay_id serial PRIMARY KEY, start_time BIGINT NOT NULL, userId varchar, level varchar, songid varchar, artistid varchar, sessionId int, location varchar, userAgent varchar);"

user_table_create = "CREATE TABLE users (userId varchar, firstName varchar, lastName varchar, gender varchar, level varchar);"

song_table_create = "CREATE TABLE songs (song_id varchar, title varchar, artist_id varchar, year int, duration int);"

artist_table_create = "CREATE TABLE artists (artist_id varchar, name varchar, location varchar, latitude decimal, longitude decimal);"

time_table_create = "CREATE TABLE time (start_time timestamp, hour int, day int, week int, month int, year int, weekday int);"

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s);""")

user_table_insert =  ("""INSERT INTO users (userId, firstName, lastName, gender, level) VALUES (%s, %s, %s, %s, %s);""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s);""")

artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s);""")

time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s);""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]