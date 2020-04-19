# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sqlite3
conn = sqlite3.connect('chinook.db')

c = conn.cursor()

t = ('3',)
c.execute('SELECT * FROM tracks WHERE albumid=?', t)

record = c.fetchone()

print(record)
print(record[2])
