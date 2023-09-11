# flask-crud

Basic CRUD operation with python flask

UI Template using [Material Dashboard 2](https://themewagon.github.io/material-dashboard-2/)

<p align="center"><img src ="doc/doc.png?raw=true" height="565" /></p>

# Install required libraries

```
pip install -r requirements.txt
```

# Run the Flask application

```
python main.py
```

# Example API Requests

---

## Create a Book (POST):

(Add new book page)

- Host: localhost:5000/new_book

## Get List of Books (GET):

(View All data)

- Host: localhost:5000/book

## Endpoints

Here's an example:

## POST

- localhost:5000/create (insert data)

## GET

- localhost:5000/book (view all data)

- localhost:5000/book/<id> (view data by id)

- localhost:5000/edit/<id> (edit data by id)

## DELETE

- localhost:5000/delete/<id> (delete data by id)
