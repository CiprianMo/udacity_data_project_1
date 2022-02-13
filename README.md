# Sparkify Data Modeling

## Introduction

The aim of this repository is to model and structure the `Song` and `Log` data so that the analytics team can understand better what songs users are listening to.

Currently the data is devided into two repositories in JSON format, one repository contains the meta data about songs, the other contains logs on user activity.

Using pandas and python, the project will build a pipeline with extract the data from the JSON format and build a Postgres database. The database will use a star schema which will be optimized for analitical queries.

## Install

The dependencies are installed using `poetry` tool, to install poetry: https://python-poetry.org/docs/#installation

Once poetry is installed run this to install the dependecies:
```
poetry install
```

The above will install the dependencies in a virtual environment.

To run the scripts you can activate the environment using:
```
poetry shell
```

Once the environemnt is activated the scripts can be run with:
```
python create_tables.py
```


## Database design

The database is made up of 3 `Dimention Tables`:
- *users*: which cotains the data about the users of the app
- *songs*: contains that data about the songs
- *artists*: data about the artis of the app
- *time*: timestamps of the records

In addition to the dimention tables there's one `Fact Table` caled `songsplays`, which logs the activity in our application. The fact table will reference the dimention tables and will help us analyse the usage of our application.

As the dimention tables should contain unique entities about our application, like `users`, `songs` and `artists` we have to add `ON CONFLICT` statements on the primary keys of these tables so that we don't add multiple enteries of the same `user`, `song` or `artist`. The `users` table is slightly different than the others that if an `user` already exists, it's level might change from `free` to `paid`, so we need to ferify the level of the existing user and in some cases update it.


## Pipeline explaination

The pipeline starts with the `create_tables.py` script. This script is the backbone of the database, it creates the database itself, sets up the connection to it, creates the requires tables and resets the tables if needed. The `etl.py` script describes the data pipeline, for **extracting** data from the files, **transform** the data acording to our analitical needs, and **load** the data into our database. For ease of data extraction and transforming we make use of `Pandas` tool for python. Pandas allows us to read the data from the files, visualize it, apply transformations and conversions and finally insert it into database. Finally all the queries for creations and insertions are described in the `sql_queries.py` file.
