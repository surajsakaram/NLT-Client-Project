#!/bin/bash


# Initiates flask server
cd ~/GA_DSI/projects/project-4/code

export FLASK_ENV=development
export FLASK_APP=webpage.py
# flask run
flask run --host=0.0.0.0 --port=5000
