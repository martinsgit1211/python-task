import sqlite3

def connectDB():
    return sqlite3.connect('ebookstore.db')

def create_table():
    db = connectDB()
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS book (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            qty INTEGER NOT NULL
        )
    ''')
    # Hello again Martins

    cursor.executemany(''' 
        INSERT OR REPLACE INTO book (id, title, author, qty) VALUES (?, ?, ?, ?)
    ''', [
        (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
        (3002, 'Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', 40),
        (3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25),
        (3004, 'The Lord of the Rings', 'J.R.R. Tolkien', 37),
        (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
    ])
    db.commit()
    db.close()

def add_new_books(id, title, author, qty):
    db = connectDB()
    cursor = db.cursor()
    cursor.execute('''
        INSERT INTO book (id, title, author, qty) VALUES (?, ?, ?, ?)
    ''', (id, title, author, qty))
    db.commit()
    db.close()

def update_books(id, title, author, qty):
    db = connectDB()
    cursor = db.cursor()
    cursor.execute('''
        UPDATE book
        SET title = ?, author = ?, qty = ?
        WHERE id = ?
    ''', (title, author, qty, id))
    db.commit()
    db.close()

def delete_books(id):
    db = connectDB()
    cursor = db.cursor()
    cursor.execute('''
        DELETE FROM book WHERE id = ?
    ''', (id,))
    db.commit()
    db.close()

def search_books(title):
    db = connectDB()
    cursor = db.cursor()
    cursor.execute('''
        SELECT * FROM book WHERE title LIKE ?
    ''', ('%' + title + '%',))
    books = cursor.fetchall()
    db.close()
    return books


def menu():
    while True:
        print('\n1. Enter book')
        print('2. Update book')
        print('3. Delete book')
        print('4. Search books')
        print('0. Exit')

        select_menu = input('What would you like to do?: ')

        if select_menu == '1':  
            id = int(input('Enter book ID: '))
            title = input('Enter title of book: ')
            author = input('Enter name of author: ')
            qty = int(input('Enter the quantity of books: '))
            add_new_books(id, title, author, qty)
        elif select_menu == '2':  
            id = int(input('Enter book ID: '))
            title = input('Enter title of book: ')
            author = input('Enter name of author: ')
            qty = int(input('Enter the quantity of books: '))
            update_books(id, title, author, qty)
        elif select_menu == '3':  
            id = int(input('Enter book ID: '))
            delete_books(id)
        elif select_menu == '4':  
            title = input('Enter title of book: ')
            books = search_books(title)
            for book in books:  
                print(book)
        elif select_menu == '0':  
            break
        else:  
            print('INVALID SELECTION. Please try again.')

# Create the table and insert initial data
create_table()

# Display the menu
menu()
