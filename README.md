# Data Modeling with Postgres

## **Project Overview:**

In this project, I'll apply what I've learned on data modeling with Postgres and build an ETL pipeline using Python.
To complete the project, I will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

### **Purpose: What songs users are listening to?**

      Example: A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to.

### **Issue: Data to be queried resides in JSON logs**

      Currently, we don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

### **What is the schema?:**

    *Schema for Song Play Analysis*
    Using the song and log datasets, I'll create a star schema optimized for queries on song play analysis. This includes the fact and dimension tables.

    ER Diagram

##    <img src="images/Song_ERD.png" alt="ER diagram" style="height: 300px; width:800px;"/>

### **What is the fact table?:**

    Fact Table
    Songplays - records in log data associated with song plays
        songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

### What are the dimension tables?:

      Dimension Tables
      users - users in the app -
        user_id, first_name, last_name, gender, level
      songs - songs in music database
        song_id, title, artist_id, year, duration
      artists - artists in music database
        artist_id, name, location, latitude, longitude
      time - timestamps of records in songplays broken down into specific units
        start_time, hour, day, week, month, year, weekday

### Files and what they do:

      In "home" folder:

      create_table.py
        Creates our fact and dimension tables.
      etl.py
        Processes the entire datasets to extract, transform dataset data, and insert records in our tables.
      sql_queries.py
        SQL queries for creating tables and inserting.
      test.ipynb
        Confirms that records were successfully inserted into each table.
      README.md
        Provides project overview and instructions.


