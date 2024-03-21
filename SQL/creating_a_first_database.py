import sqlite3

conn = sqlite3.connect("hello.db")

# It is used to create database in a certain location.
# conn = sqlite3.connect('C:\sqlite\hello.db') 

# It is used to create database in RAM.
# conn = sqlite3.connect(':memory:')