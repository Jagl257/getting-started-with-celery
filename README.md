# Getting Started With Celery

## Overview

This demo, contains the code that was used in the [Celery Getting Started Quito Lambda](https://www.youtube.com/watch?v=f35EoGYL7A4&t=850s)

It is divided into 4 sub-demos, each one related to a different Celery's characteristics. These sub-demos are:

- simple_celery_app
- celery_app_with_routing
- celery_app_with_beat
- web_app_with_celery

---

## Before getting started

### Dependencies

This demo was created with the following tool versions:

redis = 5.0.7
python = 3.9.2
celery = 5.2.7

### Installation

For this demo we use pipenv as our package/environment manager, to install it you can run:

`pip install --user pipenv`

After having pipenv installed, you can install the rest of python dependencies running:

`pipenv install`

## Getting Started

**Note: Remember that for the demos to work you need to have redis running

**Note: Remeber that all the comands must be executed inside the virtual environment. To enter the `pipenv venv`, use the following command:

```bash
$ pipenv shell
```

### Simple Celery Application

Demo File: simple_celery_app

This module will just run a simple celery app and run two tasks which can be found under `tasks.py`

To run the worker run:

```bash
$ celery -A single_celery_app.celery_app worker --loglevel INFO`
```

To start queing tasks, open a python REPL and execute the tasks, example:

```python
>>> from simple_celery_app.tasks import add
>>> s = add.delay(2,3)
```

You should be able to see this tasks beign queued and executed in the worker logs


### Celery App With Routing

Demo File: celery_app_with_routing

This demo will run two celery workers (a default one and a priority one) and will queue two tasks (which can be found under `tasks.py`) to the two different workers.

To run the default worker run:

```bash
$ celery -A celery_app_with_routing.celery_app worker --loglevel INFO
```

To run the priority worker run:

```bash
$ celery -A celery_app_with_routing.celery_app worker -Q priority -n priority@worker --loglevel INFO
```

To start queing tasks, open a python REPL and execute the tasks, example:

```python
>>> from celery_app_with_routing.tasks import notify_hello_world, say_hello_world   
>>> hello = say_hello_world.delay() # This will be routed to the default worker
>>> notify = notify_hello_world.delay() # This will be routed to the priority worker
```

### Celery App with Beat

Demo Directory: celery_app_with_beat

This demo will run two celery workers (default and priority) and a celery scheduler to queue tasks automatically based on a schedule. This schedule can be found in the `beat_conf.py` file.

To run the scheduler, run:

```bash
celery -A celery_app_with_beat.celery_app beat --loglevel INFO
```

This will start queing tasks to Redis based on the configuration.

In order to see the tasks beign executed it is necessary to run the workers.

To run the default worker run:

```bash
$ celery -A celery_app_with_routing.celery_app worker --loglevel INFO
```

To run the priority worker run:

```bash
$ celery -A celery_app_with_routing.celery_app worker -Q priority -n priority@worker --loglevel INFO
```

### Web Application with Celery

Demo Directory: web_app_with_celery

This demo will serve a flask web page, that will be able to generate a FizzBuzz sequence and store it in a external file. It will be to options to generate it, one that blocks the web app until the sequence is finished and one in which we send this task to a celery worker and it will be in charge of generating it and storing it.

To run the flask application, export the `FLASK_APP` and `FLASK_ENV` environment variables.

```bash
$ export FLASK_APP=web_app_with_celery
$ export FLASK_ENV=development

$ flask run
```

To see the web application go to: `http://localhost:8000`

To run the worker run:

```bash
$ celery -A web_app_with_celery.celery worker --loglevel INFO
```



