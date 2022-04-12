import os
import time
import logging

from app.bmi_machine.BodyMassIndex import BodyMassIndex
from app.database_manager.SqlHandler import SqlHandler
from app.utilities import Constants, helpers

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
    try:
        logging.info('Database initialized')
        sqlHandler = SqlHandler(PROJECT_DIR + dbName)
        logging.info('Database connection established')
        return sqlHandler
    except Exception as e:
        logging.error('Error while initializing database connection')
        logging.error(e)
        return None

# Generate a list of patients from json file
def generateBodyMassIndexData():
    '''
    Generate body mass index data for each patient
    :param patientData:
    :return:
    '''
    patientData = helpers.getJsonFromFile(PROJECT_DIR+Constants.PATIENT_DATA_FILE)
    if patientData is None:
        logging.error("Error while reading patient data file")
        return None
    logging.info('Generating body mass index data')
    bmiPatients = []
    try:
        for patient in patientData:
            gender = helpers.get_value_by_key("Gender", patient)
            weight = helpers.get_value_by_key("WeightKg", patient)
            height = helpers.get_value_by_key("HeightCm", patient)
            if height != None and weight != None and gender != None:
                height = height / 100
                patientObj = BodyMassIndex(weight, height, gender)
                bmiPatients.append(patientObj)
    except Exception as e:
        logging.info("Error while fetching and intializing BMI Objects")
        logging.error(e)

    return bmiPatients





def loadPatientDataIntoDb(sqlHandler, bmiPatientData):
    '''

    :param sqlHandler:
    :param bmiPatientData:
    :return:
    '''
    if sqlHandler is None:
        logging.error("Error while initializing database connection")
        return False
    if len(bmiPatientData) == 0:
        logging.error("Error while loading patient data into database")
        return False

    logging.info('Loading patient data into database')
    sqlHandler.createTable(replace=True)
    try:
        for patient in bmiPatientData:
            sqlHandler.insertData(patient.gender,patient.get_category(),patient.weight,patient.height,patient.bmi,patient.getHealthRisk())
        sqlHandler.commit()
        return True
    except Exception as e:
        logging.info("Error while loading patients to database")
        logging.error(e)
        return False


def updatePatientDataIntoDb(sqlHandler, bmiPatientData):
    '''

    :param sqlHandler:
    :param bmiPatientData:
    :return:
    '''
    logging.info('Loading patient data into database')
    sqlHandler.createTable(replace=False)
    try:
        for patient in bmiPatientData:
            sqlHandler.insertData(patient.gender,patient.get_category(),patient.weight,patient.height,patient.bmi,patient.getHealthRisk())
            sqlHandler.commit()
        return True
    except Exception as e:
        logging.info("Error while loading patients to database")
        logging.error(e)
        return False

def displayAllPatientsData(sqlHandler):
    print("Displaying all patients data")
    data = sqlHandler.getAllData()
    for row in data:
        print(row)

def getOverweightPatientsCount(sqlHandler):
    print("Displaying overweight patients count")
    data = sqlHandler.getOverweightCount()
    print(data)


if __name__ == '__main__':
    initializeLogging()
    # Initialize database connection
    sqlHandler = initializeDatabase()
    # Generate body mass index data
    bmiPatients = generateBodyMassIndexData()

    if bmiPatients is not None:
        if sqlHandler is not None:
            #Uncomment to replace existing data if any
            loadPatientDataIntoDb(sqlHandler, bmiPatients)

            #Uncomment to update data into database
            #updatePatientDataIntoDb(sqlHandler, bmiPatients)

            #Display all patients data
            displayAllPatientsData(sqlHandler)

    #Display overweight patients count
            getOverweightPatientsCount(sqlHandler)





