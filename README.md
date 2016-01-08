# Seedstars Django/Python Challenge

Both challenges were implemented with Python 2.7.10 on a Mac OS X 10.11.2 El Capitan.

## jenkins-script

Contains a simple Python script that fetches data about jobs via the REST API of a Jenkins instance and stores it in a SQLite database. By default, it fecthes data from the public Jenkins of the Ubuntu project ([https://jenkins.qa.ubuntu.com](https://jenkins.qa.ubuntu.com)). You can change the JENKINS_BASE_URL variable to any other Jenkins instance.

```
python jenkins-job-status.py
```

## django_app

Simple Django web app that stores names and emails on a SQLite database. For a quick and simple test you can use the built in server.

```
python manage.py runserver
```

> Daniel Filipe Silva
