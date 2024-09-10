#!/bin/bash

export FLASK_APP=softdes.py
export FLASK_RUN_HOST=0.0.0.0

python3 adduser.py

flask run
