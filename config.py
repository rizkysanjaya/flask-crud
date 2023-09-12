from app import app
from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy


# # Configure the PostgreSQL database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/bookapi'

# # Optional: Disable SQLAlchemy track modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # Create an SQLAlchemy database object
# db = SQLAlchemy(app)
# db.init_app(app)

# mysql = MySQL()
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = ''
# app.config['MYSQL_DATABASE_DB'] = 'bookapi'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql.init_app(app)
