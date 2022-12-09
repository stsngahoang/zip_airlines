# Zip Airline

This is project for ZipAirline Challenger

## List endpoints
#### Airplane

Method | Endpoint | Functionanlity
--- | --- | ---
GET | `/airplanes/` | Get list airplane
POST | `/airplanes/` | Create airplane
PUT | `/airplanes/<airplane_id>` | Update airplane detail
DELETE | `/airplanes/<airplane_id>` | Delete airplane
POST | `/airplanes/create_list_airplane/` | Create or update list of airplane

## Installation
### Pre-requisite
- Python 3.9+
- PIP

### Create your python virtual environment
Some virtualenv you can follow. Currently, I'm using miniconda.

- With conda/miniconda
```bash
$ conda create -n venv python=3.9
$ conda activate venv
```

- With virtualenv
```bash
# Install virtualenv from pip
$ pip install virtualenv

# create
$ python -m venv venv
$ source .venv/bin/active
```

- With pipenv
```bash
# Install pipenv from pip
$ pip install --user pipenv
```

After create your python virtual environment and activate it, the console
will look like:
```bash
(venv) $
```

### Install and running project

```bash
# Clone the project
(venv) $ git clone git@github.com:stsngahoang/zip_airlines.git
# Go to project
(venv) $ cd zip_airlines
# Install package
(venv) $ pip install requirements/dev.txt
# Copy .env file
(venv) $ cp src/.env.example src/.env
# Create migration
(venv) $ python src/manage.py makemigrations
# Apply migration file
(venv) $ python src/manage.py migrate
# Run server
(venv) $ python src/manage.py run server
```

**Note**: If you got issue is connection with database, please look at
```src/config/settings/common.py``` to edit DATABASES setting


### Play with bin - docker
You can easily run project via bin script and docker

**Note**: Make sure you install docker and docker-compose on your machine already

```bash
# Start development
bash bin/dc-run-dev.sh

# Stop development
bash bin/dc-run-dev.sh down

# Start test
bash bin/dc-run-test.sh

```

## Folder Structure
```bash
.
├── bin                          # folder of bash file as quick tool
│   └── gunicorn.sh
│   └── dc-*.sh                  # script for docker-compose
├── docker-compose.yaml          # docker-compose file for development
├── docker-compose.test.yaml     # docker-compose file for unit test
├── requirements                 # requirements folder
│   ├── common.txt
│   ├── dev.txt
│   ├── prod.txt
│   └── test.txt
└── src                          # django source app
    ├── airplanes                # airplanes app
    ├── config                   # core setting
    ├── core                     # custom django core setting
    ├── tests                    # unit test
    ├── manage.py                # django manage file
    └── ...
```
