-- Various Queries that will be utlized in the whatabook book store application

-- To display user wishlist, two inner joins are utilized to combine the user and book tables
SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author
FROM wishlist   
    INNER JOIN user ON wishlist.user_id = user.user_id
    INNER JOIN book ON wishlist.book_id = book.book_id
WHERE user.user_id = 1;

-- To display the store information, SELECT store_id and locale row(s) from the store table
SELECT store_id, locale FROM store;

-- Display all of the books offered by whatabook, SELECT all rows in the book table
SELECT book_id, book_name, author, details FROM book;

-- Display all of the books not in a specified users wishlist. 
-- Select all rows in book table, conditionally display books NOT in users wishlist
SELECT book_id, book_name, author, details
FROM book
WHERE book_id NOT IN (SElECT book_id FROM wishlist WHERE user_id=1);

-- INSERT book into users wishlist. Values here are examples and will need to be specific in actual practice.
INSERT INTO wishlist(user_id, book_id)
    VALUES(1, 9)

-- Removal of items in the user's wishlist. user_id and book_id will need to be specific values.
DELETE FROM wishlist WHERE user_id = 1 AND book_id = 9;
