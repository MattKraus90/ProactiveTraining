# ProactiveWeb

## Prequesities

Images have to be put in ProactiveWeb/webapp/static/imgs. Files are too big for GitHub.

## Build Image

```
./build_image.sh
```

If it doesn't work change properties of the file and try again.

```
chmod 777 build_image.sh
```

## Run Container

```
./run_container.sh
```

If it doesn't work change properties of the file and try again.

```
chmod 777 run_container.sh
```

## Run App inside Container

```
./run_app.sh
```

If it doesn't work change properties of the file and try again.

```
chmod 777 run_app.sh
```

## Run App in Browser

Afterwards open a browser, the server will be available at http://127.0.0.1:8000. The console will show that the app is available at http://0.0.0.0:8000, that's because of Dockers networking.

## TODOs

### ProactiveWeb/proactivityAgent/proactivity_agent.py Lines 108 - 112

user number unclear

### ProactiveWeb/webapp/views.py Line 84 + ProactiveWeb/webapp/templates/mainTask.html

build in that there is a 20 sec wait before continuing + removing the '+20' in the views