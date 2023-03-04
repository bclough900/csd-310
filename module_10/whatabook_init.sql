/* Creation of Database Objects for the WhatABook Application */
-- Drop User if User Already Exists
DROP USER IF EXISTS 'whatabook_user'@'localhost'

-- Creation of User
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- Granting of Permissions for Users
GRANT ALL PRIVELAGES ON whatabook.* TO 'whatabook_user'@'localhost';

-- Drop Constraints if Already Exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- Drop Tables if Already Exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS wishlist;


-- Creation of Required Tables
 CREATE TABLE store (
    store_id INT NOT NULL AUTO_INCREMENT,
    locale VARCHAR(500) NOT NULL,
    PRIMARY KEY(store_id)
 );

 CREATE TABLE book (
    book_id INT NOT NULL AUTO_INCREMENT,
    book_name VARCHAR(200) NOT Null,
    author VARCHAR(200) NOT NULL,
    details VARCHAR(500),
    PRIMARY KEY(book_id)
 );

 CREATE TABLE user (
    user_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(75) NOT NULL,
    last_name VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id)
 );

CREATE TABLE wishlist (
    wishlist_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    PRIMARY KEY(wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY(book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY(user_id)
        REFERENCES user(user_id)
);

-- Insert Intitial Store
INSERT INTO store(locale)
    VALUES('1516 Rock Ridge Dr, Cleveland, OK')

-- Insert Initial Book(s)
INSERT INTO book(book_name, author, details)
    VALUES('The Appeal', 'John Grisham', 'Politics have always been a dirty game. Now justice is, too.');
INSERT INTO book(book_name, author, details)
    VALUES('One Flew Over the Cuckoos Nest', 'Ken Kesey', 'In this classic novel of the 1960s, Ken Keseys hero is Randle Patrick McMurphy, a boisterous, brawling, fun-loving rebel who swaggers into the world of a mental hospital and takes over.');
INSERT INTO book(book_name, author, details)
    VALUES('The Glass Castle', 'Jeannette Walls', 'The Glass Castle is a remarkable memoir of resilience and redemption, and a revelatory look into a family at once deeply dysfunctional and uniquely vibrant.');
INSERT INTO book(book_name, author, details)
    VALUES('A Walk to Remember', 'Nicholas Sparks', 'Every April, when the wind blows in from the sea and mingles with the scent of lilacs, Landon Carter remembers his last year at Beaufort High.');
INSERT INTO book(book_name, author, details)
    VALUES('The Spectacular Now', 'Tim Tharp', 'So, my girlfriend, Cassidy, is threatning to kick me to the curb again, my best friend suddenly wants to put the brakes on our lives of fabulous fun, my mom and big sister are plotting a future in hwihc I turn into an atomic vampire, and my dad, well, my dad is a big fat question mark that Im not sure I want the answer to.');
INSERT INTO book(book_name, author, details)
    VALUES('Its Kind of a Funny Story', 'Ned Vizzini', 'Ambitious New york City teenager Craig Gilner is determined to succeed at life - which means getting into the right high school to get into the right college to get the right job.');
INSERT INTO book(book_name, author, details)
    VALUES('Walk Two Moons', 'Sharon Creech', 'Thirteen-year old Salamanca Tree hill, known as Sal, is traveling from Ohio to Idaho with her grandparents, in search of her mother. Along the way, she tells the the story of Phoebe Winterbottom, who received mysterious messages, met a "potential lunatic," and whose mother disappeared.');
INSERT INTO book(book_name, author, details)
    VALUES('Holes', 'Louis Sachar', 'Stanley Yelnats is under a curse. A curse that began with his no-good-dirty-rotten-pig-stealing great-great-grandfather and has since followed generations of Yelnats.');

-- Insert Initial User(s)
INSERT INTO user(first_name, last_name)
    VALUES('TheLone', 'Gunmen');
INSERT INTO user(first_name, last_name)
    VALUES('Fox', 'Mulder');
INSERT INTO user(first_name, last_name)
    VALUES('Dana', 'Scully');

-- Insert Initial Wishlist Values
INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'TheLone'),
        (SELECT book_id FROM book WHERE book_name = 'The Glass Castle')
    );
INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Fox'),
        (SELECT book_id FROM book WHERE book_name = 'Walk Two Moons')
    );
INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Dana'),
        (SELECT book_id FROM book WHERE book_name = 'The Spectacular Now')
    );

