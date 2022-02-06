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