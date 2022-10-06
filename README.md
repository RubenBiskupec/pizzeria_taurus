# Pizzeria Taurus

![alt text](https://github.com/RubenBiskupec/pizzeria_taurus/blob/develop/menu.png)

Check the report for a detailed description of the project and its architecture (in italian).

## Project setup - backend

> source venv/bin/activate 

The dependencies will already be installed, but the output of "pip freeze" can be seen in the requirements.txt 

> cd taurus_backend

>  python manage.py runserver

This should output
> Watching for file changes with StatReloader
Performing system checks...

> System check identified no issues (0 silenced).
April 15, 2022 - 21:56:34
Django version 4.0.3, using settings 'taurus_backend.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

## Project setup - frontend
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

This should output 
```
  App running at:
  - Local:   http://localhost:8080/ 
  - Network: http://192.168.1.85:8080/

  Note that the development build is not optimized.
  To create a production build, run npm run build.
```

### Compiles and minifies for production
```
npm run build
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
