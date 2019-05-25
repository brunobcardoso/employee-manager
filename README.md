# Employee Manager

[![CircleCI](https://circleci.com/gh/brunobcardoso/employee-manager/tree/master.svg?style=svg)](https://circleci.com/gh/brunobcardoso/employee-manager/tree/master)
[![Coverage Status](https://coveralls.io/repos/github/brunobcardoso/employee-manager/badge.svg?branch=master)](https://coveralls.io/github/brunobcardoso/employee-manager?branch=master)
[![CodeFactor](https://www.codefactor.io/repository/github/brunobcardoso/employee-manager/badge)](https://www.codefactor.io/repository/github/brunobcardoso/employee-manager)

A web application to manage employees' information, built with Django and Django REST framework.

## Dependencies
For local installation, this project requires Python3.7 and [Pipenv](https://pipenv.readthedocs.io/en/latest/) to be installed.
Otherwise, if you have `Docker` and `Docker Compose` installed, you can jump directly to installation.

## Installation

Clone the project and change directory
```
$ git clone https://github.com/brunobcardoso/employee-manager
$ cd employee-manager
```

#### With Docker:
```
$ make run
```

#### Locally:
```
$ pip install pipenv
$ cp .env.example .env
$ pipenv install --dev --skip-lock
$ pipenv run python manage.py migrate
$ pipenv run manage.py runserver
```

The development server should be running at: http://localhost:8000/

## Running the tests

#### Tests:
```console
make test
```
or
```console
pipenv run pytest
```

#### Coverage:
```console
make coverage
```

## Employee Manager Admin Panel
Create a superuser to manage the system:
```console
make superuser
```

Access Admin panel at: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## API Documentation

Swagger UI: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

ReDoc: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)


## Deployment

The deployment process is automated by CircleCI whenever `master` or `develop` changes.

**Staging:** https://staging-employee-manager.herokuapp.com/

**Production:** https://production-employee-manager.herokuapp.com/

### Pipeline

![ci_cd_pipeline](ci_cd_pipeline.png)

---

Example CircleCI Workflow for a non-deploy-branch

![non_deploy_branch_pipeline](non_deploy_branch_pipeline.png)

Example CircleCI Workflow for branch `develop`

![develop_pipeline](develop_pipeline.png)