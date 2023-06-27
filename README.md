### Hexlet tests and linter status:
[![Actions Status](https://github.com/dmitriy-ga/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/dmitriy-ga/python-project-52/actions)
[![CI](https://github.com/dmitriy-ga/python-project-52/actions/workflows/CI.yml/badge.svg)](https://github.com/dmitriy-ga/python-project-52/actions/workflows/CI.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/28d73cb13a60e2595aba/maintainability)](https://codeclimate.com/github/dmitriy-ga/python-project-52/maintainability)

### Description
Task Manager - redmine-like project management web application. Users can operate with statuses, labels and tasks.

### Deployed demo: [web-production-b7c3.up.railway.app]()

### Minimum requirements
- Python (3.10 or newer)
- Django (4.1 or newer)
- python-dotenv (1.0 or newer)
- django-filter (23.1 or newer)
- django-bootstrap4 (23.1 or newer)
- rollbar (0.16 or newer)
- gunicorn (20.1 or newer)
- dj-database-url (0.5.0)
- psycopg2-binary (2.9 or newer)

### Additional dev-dependencies
- flake8 (6.0 or newer)

### Environment variables
Can be also collected from .env file in root project folder

| Key                   | Description                             | Value      |
|-----------------------|-----------------------------------------|------------|
| SECRET_KEY            | Django secret key for database signing  | Key string |
| DJANGO_DEBUG          | Debug mode for development purposes     | True/False |
| ROLLBAR_ACCESS_TOKEN  | Access key for Rollbar reporting        | Key string |
| DISABLE_COLLECTSTATIC | Disabling static files processing       | 0/1        |
| USE_POSTGRESQL        | Switch to PostgreSQL, SQLite otherwise  | True/False |
| DATABASE_URL          | Full URL to connect PostgreSQL database | URL string |

### Installing (from source)
1. [Install Poetry](https://python-poetry.org/docs/#installation)
2. In terminal navigate to desired folder to extract
3. Clone the repo `git clone git@github.com:dmitriy-ga/python-project-52.git`
4. Open downloaded folder `cd python-project-52`
5. Run `make install`
6. Run `make migrate`

### Usage locally
`make startserver` to start up server