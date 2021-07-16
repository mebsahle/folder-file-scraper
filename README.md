# folder-file-scraper

## Getting Started
This project helps to selected files save to the database. \
Simply file scraping from folder using Python3.

## Installation
* git clone [Repository](https://github.com/mebsahle/folder-file-scraper.git)
* sudo apt-get install sqlite3 libsqlite3-dev
* delete and create SQLite_Python.db
* on terminal `sqlite3 SQLite_Python.db` 
* create table \
 `create table if not exists ark_file (id integer PRIMARY KEY, name text not NULL);` \
 .quit
* python3 b.py

#### Author
> Mebatsion Sahle
