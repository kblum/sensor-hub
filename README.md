# Arduino Sensor Hub

Hub for Arduino temperature sensors built using the [Django](https://www.djangoproject.com) Python web framework.


## Setup

The project uses [direnv](https://direnv.net) to manage the environment. This ensures that the correct Python 3 virtual environment is used. The package installation instructions are based on [Homebrew](http://brew.sh).

Install [PostgreSQL](https://www.postgresql.org) and Python 3 using Homebrew:

```sh
brew install postgresql
brew install python3
```

Install `direnv` using Homebrew and add the hook to your shell as per the documentation:

```sh
brew install direnv
```

For example, is using zsh, add the following to the end of your `~/.zshrc` file:

```sh
eval "$(direnv hook zsh)"
```

Allow `direnv` to load the `.envrc` file:

```sh
direnv allow
```

Install dependencies:

```sh
pip install -r requirements.txt
```


## Configuration

Create a `hub/local_settings.py` file and populate with the following settings (substituting in appropriate values):

```python
import os

# enable/disable debug mode (defaults to false)
os.environ['DEBUG'] = 'true'

# cryptographic signing key - must be unique and kept secret
os.environ['SECRET_KEY'] = 'SECRET'

# database
os.environ['DATABASE_URL'] = 'sqlite:///hub//db.sqlite3'

# comma-separated list of host/domain names that are valid for the site (required if DEBUG=False)
# a value beginning with a period can be used as a sub-domain wildcard (e.g. .example.com will match www.example.com)
os.environ['ALLOWED_HOSTS'] = 'example.com, sub.example.com'

# list of timezones: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
os.environ['TIME_ZONE'] = 'UTC'

# noinspection PyUnresolvedReferences
from .settings import *
```

The configuration file is not under version control.

Run initial database migrations:

```sh
python manage.py migrate
```

Create a new admin user:

```sh
python manage.py createsuperuser
```


## Running the Project

Create schema migrations if any changes were made to models:

```sh
python manage.py makemigrations
```

Run database migrations:

```sh
python manage.py migrate
```

Start the development server:

```sh
python manage.py runserver
```
