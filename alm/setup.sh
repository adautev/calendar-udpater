#!/usr/bin/env bash
git clone https://github.com/adautev/calendar-updater.git
cd calendar-updater/
virtualenv venv
source venv/bin/activate
pip install -r virtualenv.txt