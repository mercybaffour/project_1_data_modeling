import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def get_files(filepath):
    """
    This procedure obtains all the files from a directory.
    """

    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    return all_files


def process_song_file(cur, filepath):
    """
    This procedure processes a song file whose filepath has been provided as an argument.
    It extracts the song information in order to store it into the songs table.
    Then it extracts the artist information in order to store it into the artists table.
    """

    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_data = df[["song_id", "artist_id", "title", 
                    "duration", "year"]].values[0].tolist()
    cur.execute(song_table_insert, song_data)

    # insert artist record
    artist_data = df[["artist_id", "artist_name", "artist_location",
                      "artist_latitude", "artist_longitude"]].values[0].tolist()
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    This procedure processes a log file whose filepath has been provided as an argument.
    It extracts the log time and user to store it into the time and songs table. 
    #Then it extracts songplay actions to insert into songplays table.
    """ 

    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    is_nextsong = df['page'] == 'NextSong'
    df = df[is_nextsong]

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'])

    # insert time data records
    hour = t.dt.hour
    day = t.dt.day
    week_of_year = t.dt.week
    month = t.dt.month
    year = t.dt.year
    weekday = t.dt.weekday

    time_data = []
    time_data.extend((t, hour.astype(int), day.astype(int), week_of_year.astype(
        int), month.astype(int), year.astype(int), weekday.astype(int)))
    column_labels = ["timestamp", "timestamp_hour", "timestamp_day",
                     "timestamp_weekofyear", "timestamp_month", "timestamp_year", "timestamp_weekday"]
    dict = {column_labels[i]: time_data[i]
            for i in range(len(column_labels))}
    time_df = pd.DataFrame.from_dict(dict)


    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[["userId", "firstName", "lastName", "gender", "level"]]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():

        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))

        results = cur.fetchone()

        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (pd.to_datetime(row.ts, unit='ms'), row.userId, row.level, songid,
                         artistid, row.sessionId, row.location, row.userAgent)
        
        print(songplay_data)
        cur.execute(songplay_table_insert, songplay_data)

def process_data(cur, conn, filepath, func):
    """
    This procedure processes the raw data to be used in our ETL pipeline.
    """

    #get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    """
    This procedure connects to a local instance of a database. 
    """

    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=sparkifydb user=postgres password=password")
    cur = conn.cursor()

    process_data(cur, conn, filepath='home\data\song_data', func=process_song_file)
    process_data(cur, conn, filepath='home\data\log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
