# laptime-analyzer

`python -m venv venv`
`.\venv\Scripts\activate`

`pip install django psycopg2-binary`
`pip install gunicorn django-heroku`

`django-admin startproject PKB`

`echo "venv/" > .gitignore`
`echo "*.pyc" >> .gitignore`
`echo "__pycache__/" >> .gitignore`
`echo "*.sqlite3" >> .gitignore`

````
# Access PostgreSQL
psql

# In the PostgreSQL shell, run these commands:
CREATE DATABASE pkb_db;
CREATE USER pkb_user WITH PASSWORD 'your_password';
ALTER ROLE pkb_user SET client_encoding TO 'utf8';
ALTER ROLE pkb_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE pkb_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE pkb_db TO pkb_user;
\q
```

`echo "web: gunicorn PKB.wsgi" > Procfile`
echo "python-3.12.6" > runtime.txt
pip freeze > requirements.txt