#!/usr/bin/env bash
git clone https://github.com/adautev/calendar-updater.git
cd calendar-updater/
mkdir credentials
virtualenv venv
source venv/bin/activate
pip install -r virtualenv.txt