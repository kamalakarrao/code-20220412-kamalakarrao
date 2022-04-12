import os
import time
import logging
from app.database_manager.SqlHandler import SqlHandler
from app.utilities import Constants

#Initialize logging
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

def initializeLogging():
    '''
    Initialize logging for the application.
    :return:
    '''
    logging.basicConfig(filename=PROJECT_DIR+'/logs/'+str(time.ctime())+".log", level=logging.DEBUG)
    logging.info('Logging initialized')


#Intialize database connection
def initializeDatabase(dbName = Constants.DB_NAME):
    '''
    Initialize database connection
    :return:
    '''
    logging.info('Database initialized')
    sqlHandler = SqlHandler(PROJECT_DIR + dbName)
    logging.info('Database connection established')
    return sqlHandler




if __name__ == '__main__':
    initializeLogging()
