# flask-crud

Basic CRUD operation with python flask

UI Template using [Material Dashboard 2](https://themewagon.github.io/material-dashboard-2/)

<p align="center"><img src ="doc/doc.png?raw=true" height="565" /></p>

# Setup Database

```
-- Create the Database if it doesn't exist
CREATE DATABASE IF NOT EXISTS `bookapi`;

-- Use the created database
USE `bookapi`;

-- Create the `books` table if it doesn't exist
CREATE TABLE IF NOT EXISTS `books` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(25) NOT NULL,
  `author` varchar(20) NOT NULL,
  `genre` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Insert data into the `books` table, ignoring duplicates
INSERT IGNORE INTO `books` (`id`, `title`, `author`, `genre`) VALUES
(2, 'Ini Judul', 'Ini Penulis', 'Ini Genre'),
(5, 'Book 1', 'Author 1', 'Genre 1'),
(6, 'Book 6', 'Author 6', 'Genre 6'),
(7, 'The Hobbit', 'J.R.R. Tolkien', 'Fantasy'),
(9, 'The Two Towers', 'J.R.R. Tolkien', 'Fantasy'),
(11, 'Book 7', 'Author 7', 'Genre 7');
```

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
