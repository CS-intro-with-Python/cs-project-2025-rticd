[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/DESIFpxz)
# Task manager (2025 CS project)

(Everything is work in progress, so this README is incomplete and can change)

## Description
Create, view, edit and delete certain entries called "the tasks". The tasks can be associated with some day/s (when they are supposed to be done) and the deadline (up until when they need to be done), but they don't necessarily need to have them. Each task also has a status and the note section. The possible values of the status are:
1. Not started
2. In progress
3. Completed
In the note section anything can be written. 
Tasks can be grouped and viewed on the calendar (as long as they have a day or a deadline).

## Setup

To build and run the backend server:
docker build -t taskmanager <project_repo>
docker run -p 5000:5000 taskmanager

This will launch it locally

The server can also be remotely accessed through https://cs-project-2025-rticd-production.up.railway.app

## Requirements

- Python
   - Flask
   - Requests
- Docker
- Git
- Railway

## Features

* View tasks in different way, including a calendar.
* Add, edit and remove tasks

## Git
Latest stable version is stored in the main branch

## Success Criteria

* All features are implemented and work correctly
* The app is convenient to use

