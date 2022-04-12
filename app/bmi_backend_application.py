import os
import time
import logging

#Initialize logging
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(filename=PROJECT_DIR+'/logs/'+str(time.ctime())+".log", level=logging.DEBUG)

