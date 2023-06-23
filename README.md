# Proactive Web

## Description

This repository contains a Web App implemented with [Django](https://www.djangoproject.com/) and Python for the "Planspiel CEO" which employs a Proactivity Agent for helping the Player based on his personality.

## Usage

### Prequesities

Images have to be put in ProactiveWeb/webapp/static/imgs. Files are too big for GitHub.

### Build Image

```
# properties may have to be adjusted with chmod
./build_image.sh
```

### Run Container

```
# properties may have to be adjusted with chmod
./run_container.sh
```

### Run App inside Container

```
# properties may have to be adjusted with chmod
./run_app.sh
```

### Run App in Browser

Afterwards open a browser, the server will be available at http://127.0.0.1:8000. The console will show that the app is available at http://0.0.0.0:8000, that's because of Dockers networking.

## Project Structure

### ProactiveTraining

Includes readme, files for Docker, gitignore and ProactiveWeb.

### ProactiveWeb

Includes run_app for running the app and the manage.py which acts as an interface to interact with the Django project. Also it includes the directories ProactiveWebApp, proactivityAgent and webapp.

### ProactiveWebApp

This directory contains the asgi.py, settings.py, urls.py and wsgi.py. It is the Django projects root directory which houses project-level configuration files and acts as the entry point for the Django application.

### webapp

This directory contains the Django application. It contains the several other directories and files, the most important are:

 - static 
    - static files just as CSS files, JavaScript files, JSON files and images in the imgs directory. In the JSON directory the user data is saved
 - templates
    - contains the html templates
 - urls.py
    - defines the URL patterns specific to this application
 - views.py
    - This file contains the view functions or classes that handle the logic for generating responses to HTTP requests within the application

### proactivityAgent

Includes the DQN Agent, the trust model, data like the difficulties and the config, as well as various files for using the agent.