# API Template

- This is a basic template to develop APIs in an easy way

### Pre-requirements

- This app use `pipenv` to configurate dependencies easily

```zsh
pip install pipenv
pipenv install
pipenv run pre-commit install # install pre-commits
```

### Main libs list

- [fastapi](https://github.com/tiangolo/fastapi) - web framework
- [uvicorn](https://www.uvicorn.org/) - ASGI web server
- [orjson](https://github.com/ijl/orjson) - for faster JSON "parsing" and more
- [httpx](https://github.com/encode/httpx) - for better requests
- [pytest](https://github.com/pytest-dev/pytest) - for unit testing

### Structure

```
api-project
├── alembic/
│   └── __init__.py
├── src
│   ├── __init__.py
│   ├── auth
│   │   ├── __init__.py
│   │   ├── router.py
│   │   ├── schemas.py  # pydantic models
│   │   ├── models.py  # db models
│   │   ├── dependencies.py
│   │   ├── config.py  # local configs
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   ├── service.py
│   │   └── utils.py
│   ├── aws
│   │   ├── __init__.py
│   │   ├── client.py  # client model for external service communication
│   │   ├── schemas.py
│   │   ├── config.py
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   └── utils.py
│   ├── config.py  # global configs
│   ├── models.py  # global models
│   ├── exceptions.py  # global exceptions
│   ├── pagination.py  # global module e.g. pagination
│   ├── utils.py
│   ├── database.py  # db connection related stuff
│   └── main.py
├── tests/
│   ├── __init__.py
│   ├── auth
│   └── aws
├── templates/  # In case you need it
│   ├── __init__.py
│   └── index.html
├── Pipfile
├── Pipfile.lock
├── .env
├── .gitignore
├── logging.ini
└── alembic.ini
```

- Many practices are taken from [Fastapi best practices](https://github.com/zhanymkanov/fastapi-best-practices)
