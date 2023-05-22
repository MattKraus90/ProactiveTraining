# ProactiveWeb

## Prequesities

Images have to be put in ProactiveWeb/webapp/static/imgs. Files are too big for GitHub.

## Build Image

```
# properties may have to be adjusted with chmod
./build_image.sh
```

## Run Container

```
# properties may have to be adjusted with chmod
./run_container.sh
```

## Run App inside Container

```
# properties may have to be adjusted with chmod
./run_app.sh
```

## Run App in Browser

Afterwards open a browser, the server will be available at http://127.0.0.1:8000. The console will show that the app is available at http://0.0.0.0:8000, that's because of Dockers networking.

## TODOs

### ProactiveWeb/webapp/views.py Line 84 + ProactiveWeb/webapp/templates/mainTask.html

build in that there is a 20 sec wait before continuing + removing the '+20' in the views