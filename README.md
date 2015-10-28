# Web Vidyeo

Simple yet web application to send mobile camera to website canvas

# Installation

Run the following commands

    make venv

Create database

    touch storage/default.sqlite
    source venv/bin/activate && alembic upgrade head

Run developer server

    make server

Run assets watcher

    make watch
