from flask import Flask
import sqlite3 as sql

app = Flask(__name__)

conn = sql.connect('dbTest.db')
conn.close()