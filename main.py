import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request, render_template, redirect, url_for

@app.route('/create', methods=['POST'])
def add_book():
    try:
        _title = request.form['title']
        _author = request.form['author']
        _genre = request.form['genre']

        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("INSERT INTO books(title, author, genre) VALUES(%s, %s, %s)", (_title, _author, _genre))
        conn.commit()

        # flash('Book added successfully!', 'success')  # Optional: Flash a success message

        return redirect(url_for('book'))
    except Exception as e:
        # Handle exceptions here (e.g., database errors)
        # flash('An error occurred while adding the book.', 'error')
        return redirect(url_for('book'))  # Redirect to the book page even if there's an error
    finally:
        cursor.close()
        conn.close()
        
#insert book page
@app.route('/new_book')
def new_book():
    return render_template('add-book.html')

#update book page and display data from coreesponding id
@app.route('/edit/<string:id>', methods=['GET', 'POST'])
def edit(id):
    conn = mysql.connect()
    cursor = conn.cursor()

    if request.method == 'POST':
        # Retrieve the form data
        _title = request.form['title']
        _author = request.form['author']
        _genre = request.form['genre']

        # Update the record in the database
        cursor.execute(
            "UPDATE books SET title=%s, author=%s, genre=%s WHERE id=%s",
            (_title, _author, _genre, id)
        )
        conn.commit()

        # flash('Book updated successfully!', 'success')
        conn.close()
        return redirect(url_for('book'))

    # If the request method is GET, retrieve the data of the book to be edited
    cursor.execute("SELECT * FROM books WHERE id = %s", (id,))
    book = cursor.fetchone()
    conn.close()

    if book:
        return render_template('edit-book.html', book=book)
    else:
        # flash('Book not found!', 'danger')
        return redirect(url_for('book'))
   
# #update function
# @app.route('/update', methods=['POST'])
# def update():
#     conn = mysql.connect()
#     cursor = conn.cursor()

#     if request.method == 'POST':
#         # Retrieve the form data
#         _title = request.form['title']
#         _author = request.form['author']
#         _genre = request.form['genre']

#         # Update the record in the database
#         cursor.execute(
#             "UPDATE books SET title=%s, author=%s, genre=%s WHERE id=%s",
#             (_title, _author, _genre, id)
#         )
#         conn.commit()

#         flash('Book updated successfully!', 'success')
#         conn.close()
#         return redirect(url_for('book'))
    
@app.route('/book')
def book():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM books")
        bookRows = cursor.fetchall()
        return render_template('books.html', title='Books', books=bookRows)
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()


@app.route('/book/<int:id>')
def book_details(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, title, author, genre FROM books WHERE id =%s", (id,))
        bookRow = cursor.fetchone()
        respone = jsonify(bookRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 

# @app.route('/update', methods=['PUT'])
# def update_book():
#     try:
#         _id = request.form['id']
#         _title = request.form['title']
#         _author = request.form['author']
#         _genre = request.form['genre']

#         conn = mysql.connect()
#         cursor = conn.cursor(pymysql.cursors.DictCursor)
#         cursor.execute("UPDATE books SET title=%s, author=%s, genre=%s WHERE id=%s", (_title, _author, _genre, id))
#         conn.commit()
#         return redirect(url_for('book'))
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close() 
#         conn.close() 

@app.route('/delete/<int:id>', methods=['GET'])
def delete_book(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM books WHERE id =%s", (id,))
		conn.commit()
		return redirect(url_for('book'))
	except Exception as e:
		return redirect(url_for('book'))
	finally:
		cursor.close() 
		conn.close()
        
       
@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
        
if __name__ == "__main__":
    app.run(debug=True)
