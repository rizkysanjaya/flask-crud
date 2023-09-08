# flask-crud
Basic CRUD operation with python flask

UI Template using [Material Dashboard 2](https://themewagon.github.io/material-dashboard-2/)

<p align="center"><img src ="doc/doc.png?raw=true" height="565" /></p>

# Run the Flask application
```
python app.py
```
# Example API Requests
---
Create a Book (POST):
---
- POST /create HTTP/1.1
- Host: localhost:5000
- Content-Type: application/json

```
{
  "title": "Sample Book",
  "author": "John Doe",
  "genre": "Fiction"
}
```
# Get List of Books (GET):

- GET /book HTTP/1.1
- Host: localhost:5000

# Endpoints

Here's an example:

# POST /create
- Create a new book record.

Request:

- Method: POST

- URL: /create

# Request body format: JSON
- Example request body:
```
{
  "title": "Sample Book",
  "author": "John Doe",
  "genre": "Fiction"
}
```
Response:
- Status code: 302 (Redirect)
- Redirects to /book on success.



