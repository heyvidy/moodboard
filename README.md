# Mood Board Demo Full Stack Project

The project is constructed into two Django Apps 
- webserver
- api

**webserver** emulates a file server. Usually this would be a separate project in itself.
**api** is a REST-API that handles application logic and serves JSON at all endpoints.

---

## Getting Started with the Project

To get started with the project:
```
$ 
```

To install all dependencies, **create a new virutalenv** with your preferred plugin and do
```
$ pip install -r requirements.txt
```

To run the project, Go to the root folder and run
```
$ python manage.py runserver
```

To run the project on a local network
```
$ python manage.py runserver 0.0.0.0:80
```