#!/bin/bash

# Navigate to the site folder
cd /home/site/wwwroot

# Install dependencies
pip install -r requirements.txt

# Start the app with gunicorn (recommended for production)
# 'app:app' assumes you have app.py with a Flask() instance named `app`
gunicorn --bind=0.0.0.0 --timeout 600 app:app
