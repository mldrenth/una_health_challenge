# una_health_challenge
Project for Una Health
## Why Django?:
- Quick setup of APIs
- Easy implementation of Test Driven Development
- Admin Area
- Extandable with other django packages

## How to Install
- git clone the repository
- ``` cd una_health_challenge```
- Create env file  ```python3 -m venv .env ```
- ```source .env/bin/activate```
- Install requirements ``` pip3 install -r requirements.txt ```
- ``` python3 manage.py migrate  ```
- Load csv data``` python3 manage.py load_csv [filepath]```
- ``` python3 manage.py createsuperuser ```
- ``` python3 manage.py runserver```

## API
- For Detail Value Overview for User go to: http://127.0.0.1:8000/api/v1/levels
- For Value by Id go to: http://127.0.0.1:8000/api/v1/levels/{id}

