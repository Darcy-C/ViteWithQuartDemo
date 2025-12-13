##  Vite+Quart Demo

This repository demonstrates how to integrate `Vite` with a classic, template-engine–based backend framework similar to `Flask`. The demo uses `Quart` (an async-first framework) so implementing a real WebSocket handler later is straightforward.

In this demo, we would like to use `Quart`, an async first framework, so we can easily implement real websocket handler in the future.

**QUICK NOTE**: `Quart` is just an async version of `Flask`, they almost share the same apis.

### WHY VITE

Historically, we managed JS imports manually, now with `vite`, we can use it as a html page auto reload tool, a scss compiler hot-reload tool, a js bundler, and many features which vite would like to provide, e.g. JS syntax trans-compiler, many things we can specify in `vite.config.js` in the future if we would like to do.

### REPO OVERVIEW

- app/static/bundle/

    vite compiled js and css will finally go there, to compile, please issue `npm run build`.

- app/templates/

    just like any other flask/quart projects, old classic html templates go in there, these are jinja based templates.

- app/utils/context_processor.py

    defines helpers like `asset`, so that we can use `asset('/ababababa')` in our template file.

- web/

    scripts and styles are in here, vite will take care of theses.


### HOW TO USE

#### Install Python server side deps
```
pythonXXX -m pip install -r requirements.txt
```
where pythonXXX is your python executable installed on your system,
if you are sure that you will call the correct pip, you can do
```
pip install -r requirements.txt
```
Also, since current project only have one package, which is quart, you
can directly install it by issuing `pip install quart`.

#### Install Vite related site deps

```
npm i
```

#### RUN DEV

This will watch JS side changes
```
npm run dev
```

The main entry point is here
```
QUART_DEBUG=1 pythonXXX main.py
```

Note, these two lines should be run in two different shell sessions since they block.

**ABOUT QUART_DEBUG ENV VAR**

quart debug flag can be changed by environment variable or in code e.g. `app.run(debug=True)`

In our app design, we have a logic which reuses quart debug flag to check if the current environment is in production or development, we will use different asset path depending on current mode.

In an another word, if current mode is dev, we will use asset file, e.g. js script, compiled from vite, otherwise, the already compiled assets from `static/bundle` folder will be used. 

**(OPTIONAL) BUT GOOD PRACTICE**

Please note that if ever possible, try the project in virtual environment is a
good practice, Please do:

(bash example)
```bash
pythonXXX -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
python main.py
```

### BEFORE DEPLOY

After you have done the coding part and are ready to deploy the app somewhere, make sure that you have your vite-project built, please run:

```
npm run build
```

The build output will be placed in `./app/static/bundle/`. Make sure this folder is available in your deployment environment.

### RELATED PROJECT

This demo project is highly inspired by 
`tylerlwsmith/vite-with-flask-backend` with slight improvements, thank you.
