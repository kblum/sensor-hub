# Arduino Sensor Hub

Hub for Arduino temperature sensors built using the [Django](https://www.djangoproject.com) Python web framework.


## Setup

Install Python 3 using [Homebrew](http://brew.sh):

    brew install python3

Create virtual environment:

    virtualenv --python=python3 venv

Activating the virtual environment:

    source venv/bin/activate

Install dependencies:

    pip install -r requirements.txt

Deactivation the virtual environment:

    deactivate


## Running the Project

Activate the virtual environment.

Create schema migrations if any changes were made to models:

    python manage.py makemigrations

Run database migrations:

    python manage.py migrate

Start the development server:

    python manage.py runserver
