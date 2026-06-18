import sqlite3
import os


###########################################################
# STEP 20 : Database Path
###########################################################

BASE_DIR = os.getcwd()


DB_DIR = os.path.join(

    BASE_DIR,

    "database"

)


os.makedirs(

    DB_DIR,

    exist_ok=True

)


DB_PATH = os.path.join(

    DB_DIR,

    "churn_history.db"

)


###########################################################
# STEP 20.1 : Connect Database
###########################################################

conn = sqlite3.connect(

    DB_PATH,

    check_same_thread=False

)


cursor = conn.cursor()


###########################################################
# STEP 20.2 : Create Table
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
