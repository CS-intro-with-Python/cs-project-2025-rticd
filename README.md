[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/DESIFpxz)
# Task manager (2025 CS project)

## Description
Create, view, edit and delete certain entries called "the tasks". The tasks can be associated with some day/s (when they are supposed to be done) and the deadline (up until when they need to be done), but they don't necessarily need to have them. Each task also has a status and the note section. The possible values of the status are:
1. Not started
2. In progress
3. Completed
In the note section anything can be written. 
Tasks can be grouped. 
Tasks can be viewed on the calendar (as long as they have a day or a deadline).

## Setup

To build and run the backend server:

docker compose up -d --build 

This will launch it locally

The server can also be remotely accessed through web-production-8f19b.up.railway.app

## Requirements

- Python
   - flask
   - requests
   - psycopg2-binary
   - SQLAlchemy
   - Flask-SQLAlchemy
   - pytest (to run tests)
- Docker-Compose
- Git
- Railway

## Features

* Viewing tasks in different ways, including a calendar.
* Adding, editing and removing tasks

## Git
Latest stable version is stored on the main branch

## Success Criteria

* All features are implemented and work correctly
* The app is convenient to use

## Tests

* tests/test_launch.sh: launches the app (db and the server) and checks if the server responds. 
The db is also automatically checked, because the server doesn't launch if the db isn't ready.
To launch, ./test_launch.sh