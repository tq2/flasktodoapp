# Todo Application

A simple to-do list application built with Flask and SQLAlchemy.

## Requirements

- Flask
- Flask-SQLAlchemy
- SQLite

## Usage

1. Clone the repository to your local machine:

```python
$ git clone https://github.com/1saNe/flasktodoapp.git
```

2. Install the required packages:

```python
$ pip install -r requirements.txt
```

3. Set the environment variable for the database URI:

```python
$ export TODO_DATABASE_URI="sqlite:///<database_location>.db"
```

4. Create the database and tables:

```python
from app import db
db.create_all()
exit()
```

5. Run the application:

```python
$ python app.py
```

6. Open your web browser and navigate to `http://localhost:5000/` to access the to-do list.

## Features

- Add new to-dos
- Mark to-dos as complete
- Delete to-dos

## Contributing

1. Fork the repository
2. Create a new branch for your changes
3. Commit your changes
4. Open a pull request
