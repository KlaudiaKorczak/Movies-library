# Movies Library

Django Rest Api:
- Django Rest Framework
- SQLite db


## How to run this project locally:

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

4) Go to (http://localhost:8000)

### Movies endpoint (http://localhost:8000/movies/)
- GET
- POST
required request body : `{"title": "Movie title"}`
### Comments endpoint (http://localhost:8000/comments/)
- GET: 
possible filtering from Rest Tool` -> Filters -> Movie_id` or `http://localhost:8000/comments/?movie_id={id}`
- POST: 
required request body:
`{
    "movie_id": id,
    "body": "Comment body"
    }`
### Top comments endpoint (http://localhost:8000/top/)
- GET: 
Dates params in url are optional for date range filtering: `http://localhost:8000/top/date/date`. Date format: `yyyy-mm-dd e.q. 2019-08-20`
