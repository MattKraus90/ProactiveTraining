# ProactiveWeb

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

Afterwards open a browser, the server will be available at http://127.0.0.1:8000. The console will show that the app is available at http://0.0.0.0:8000, that's wrong though. The reason is Dockers networking.