import os
import time
import logging

#Initialize logging
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

def initializeLogging():
    '''
    Initialize logging for the application.
    :return:
    '''
    logging.basicConfig(filename=PROJECT_DIR+'/logs/'+str(time.ctime())+".log", level=logging.DEBUG)
    logging.info('Logging initialized')






if __name__ == '__main__':
    initializeLogging()
