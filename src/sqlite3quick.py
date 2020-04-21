#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Created on Sat Apr 18 11:11:10 2020
#@author: -

import logging
import sqlite3
import Database as db
import platform
import pandas as pd
from pandas import DataFrame

op_system = platform.system()

if op_system == 'Windows':
    db_file = "D:\\win_sqlite\\chinook.db"
elif op_system == 'Linux':
    db_file = "/mnt/d/win_sqlite/chinook.db"

# create formatter
#format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
format = '%(asctime)s - %(name)s - %(filename)s - %(message)s'
logging.basicConfig(filename='sqlite3quick.log',filemode='w',format = format, level=logging.DEBUG)



print("Database file is", db_file)
try:
    sqliteConnection = db.Database(db_file)
    logging.debug("Successfully Connected to SQLite")
    record = sqliteConnection.query("select sqlite_version();")
    logging.info("SQLite Database Version is %s:", record)
    record = sqliteConnection.query("select * from employees;")
    tab_df = pd.DataFrame(record)
    sqliteConnection.cursor.close()
    logging.info("The SQLite cursor is closed")
    print(tab_df)


except sqlite3.Error as error:
    logging.error("Error while connecting to sqlite - %s", error)

finally:
    sqliteConnection.close()
    logging.debug("The SQLite connection is closed")
    
logging.shutdown()  

