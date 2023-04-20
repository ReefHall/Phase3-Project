import sqlite3

CONN = sqlite3.connect('lib/db/robots.db')
CURSOR = CONN.cursor()