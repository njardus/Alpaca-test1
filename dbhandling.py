from loguru import logger
import settings
import sqlite3 as sql
from sqlite3 import Error

logger.info("Running dbhandler.py")
db_filename = ""

def setDBFile():
    logger.info("Start setDBFile function.")
    db_filename = settings.dbfilename
    logger.info(f"db_file set to {db_filename}")

def createConn(db_file):
    """ Create the SQL Lite connection """
    logger.info("Attempt the db connection.")
    conn = ""

    try:
        conn = sql.connect(db_file)
        logger.info(sql.version)
        return conn
    except Error as e:
        logger.error(f"Error connecting to the DB: {e}")
        return ""

    # TODO: On failure, evaluate if we want to create a db, and write the function for that.
    logger.info("Finish the CreateConn function")

def putdataintodb(data, meta_data):
    logger.info("Starting the putdataindb function")
    if db_filename == "":
        setDBFile()
    conn = createConn(db_filename)

    # We know this is going to fail for now, so nothing further
    # TODO: Add putting into db queries

    logger.info("Close connection to db in the putdataindb function")
    conn.close()

if db_filename == "":
    setDBFile()