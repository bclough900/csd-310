#Import the Required Modules for the Application 
import sys
import mysql.connector
from mysql.connector import errorcode

#Database Connection Config Object
config = {
    "user" : "whatabook_user",
    "password" : "MySQLIsGreat!",
    "host" : "127.0.0.1",
    "database" : "whatabook",
    "raise_on_warnings" : True
}

#Initial Interface for User
def show_menu():
    print("\n -- Welcome to the WhatABook Main Menu --")
    print("1. View Books\n2. View Store Locations\n3. My Account\n4. Exit Application")

    try:
        choice = int(input('    <Example enter 1 for book listings>: '))
        return choice
    except ValueError:
        print("\n   Invalid choice, exiting program....\n")
        sys.exit(0)

#Display List of Books Function WITH Query of book Table
def show_books(_cursor):
    _cursor.execute("SELECT book_id, book_name, author, details FROM book")
    books = _cursor.fetchall()
    i = 0
    for book in books:
        if i == 0:
            print(" Book ID: {}\n Book Name: {}\n Author: {}\n Details: {}\n".format(book[0], book[1], book[2], book[3]))  
            i + 1
        elif i == 1:
            print("End of list...")

#Display Store Locations WITH Query of store Table
def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")
    locations = _cursor.fetchall()
    print("\n  -- Displaying Locations --")
    
    for location in locations:
        print("  Locale: {}\n".format(location[1]))
        
                
   

#User Validation Function
def validate_user():
    try:
        user_id = int(input('\n      Enter your customer id <I.e 1, 2, or 3>: '))

        if user_id < 0 or user_id > 3:
            print("\n ID invalid, exiting program...\n")
            sys.exit(0)
        return user_id
    except ValueError:
        print("\n Invalid number, exiting program...\n")
        sys.exit(0)

#Display User Account
def show_account_menu():
    try:
        print("\n   -- Customer Account Menu --")
        print("\n   1. Wishlist\n   2. Add Book\n   3. Main Menu ")
        account_option = int(input('    <I.e. Enter 1 for wishlist 2 to add book and 3 for the main menu>: '))

        return account_option
    except ValueError:
        print("\n You have entered an invalid option, exiting program...")
        sys.exit(0)

#Display the User's Wishlist Items, Query to Show Items
def show_wishlist(_cursor, _user_id):
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
        "FROM wishlist " + 
        "INNER JOIN user ON wishlist.user_id = user.user_id " +
        "INNER JOIN book ON wishlist.book_id = book.book_id " +
        "WHERE user.user_id = {}".format(_user_id))

    wishlist = _cursor.fetchall()
    print("\n   -- Displaying Items in Wishlist --")

    for book in wishlist:
        print(" Book Name: {} \n    Author: {}\n".format(book[4], book[5]))

 #Display Books Available to Add to the Wishlist
def show_books_to_add(_cursor, _user_id):
    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
    print(query)
    _cursor.execute(query)
    books_to_add = _cursor.fetchall()
    print("\n   -- Displaying Books Available --")
    for book in books_to_add:
        print("\n   Book ID: {}\n   Book Name: {}\n".format(book[0], book[1]))

#Add Book to Wishlist Function
def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))
#Error Handling for Potential Database Errors
try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    print("\n Welcome to the WhatABook Application!")
    user_selection = show_menu()

    while user_selection != 4:
        if user_selection == 1:
            show_books(cursor)
            user_selection = show_menu()            
        elif user_selection == 2:
            show_locations(cursor)
            user_selection = show_menu()
        elif user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()
            while account_option != 3:
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)
                if account_option == 2:
                    show_books_to_add(cursor, my_user_id)
                    book_id = int(input("\n Enter the ID of the book you wish to add: "))
                    add_book_to_wishlist(cursor, my_user_id, book_id)
                    db.commit()
                    print("\n   Book ID: {} has been added to your wishlist.".format(book_id))
                if account_option == 3:
                    show_menu
                if account_option < 0 or account_option > 3:
                    print("\n   Invalid input, please try again...")
                account_option = show_account_menu()
        if user_selection < 0 or user_selection > 4:
            print("\n      Invalid option, please retry...")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Unable to connect to database, invalid username or pasword...")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database not found, please check configuration or submit a ticket to IT")
    else:
        print(err)
finally:
    db.close()






