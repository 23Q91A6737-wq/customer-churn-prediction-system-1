import sqlite3
import os


###########################################################
# STEP 20 : Database Path
###########################################################

DB_PATH = "database/churn_history.db"


###########################################################
# STEP 20.1 : Create Database Folder
###########################################################

os.makedirs(

    os.path.dirname(DB_PATH),

    exist_ok=True

)


###########################################################
# STEP 20.2 : Connect Database
###########################################################

conn = sqlite3.connect(

    DB_PATH,

    check_same_thread=False

)

cursor = conn.cursor()


###########################################################
# STEP 20.3 : Create Table
###########################################################

cursor.execute(

'''

CREATE TABLE IF NOT EXISTS prediction_history(

id INTEGER PRIMARY KEY AUTOINCREMENT,

prediction TEXT,

churn_probability REAL,

retention_probability REAL,

risk_level TEXT,

timestamp TEXT

)

'''

)


conn.commit()