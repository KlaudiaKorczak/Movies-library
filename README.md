# Movies Library

Django Rest Api:
- Django Rest Framework
- SQLite db


## How to run tis project locally:

1) Clone this repository and go to the project directory

2) Create local environment
- make venv
    ```
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    ```
    To exit venv: `deactivate`

or
- run docker
    ```docker-compose up```

3) Migrate db and run Django project
    ```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```

4) Go to:
- Movies endpoint (http://localhost:8000/movies/)
- Comments endpoint (http://localhost:8000/comments/)
- Top comments endpoint (http://localhost:8000/top/)
