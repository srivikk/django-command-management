# django-command-management

This repository contains project on a Django application with User and ActivityPeriod models which uses custom management command to populate the database with dummy data and API to serve that data in the json format.

### API endpoint 

http://ec2-3-22-172-18.us-east-2.compute.amazonaws.com:8000/activities/

### Data

Dummy data to populate the database

* test_data.json

### How to populate database with dummy data

Using custom management command, models: User and ActivityPeriod is populated with dummy data in the json file.

```
python manage.py populate_data --path test_data.json
```

### Project Organization

```
├── api
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── management
│   │   └── commands
│   │       └── populate_data.py
│   ├── migrations
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── django_assignment
│   ├── asgi.py
│   ├── nohup.out
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── nohup.out
└── test_data.json
```
