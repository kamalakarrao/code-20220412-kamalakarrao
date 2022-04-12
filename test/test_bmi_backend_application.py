from app.utilities import Constants


class TestCase:
    """
    Test class for the BMI Backend Application.
    """
    def test_bmi_app(self):
        """
        Test the BMI Backend Application.
        """
        pass

    def test_bmi_app_logging(self):
        """
        Test the BMI Backend Application logging.
        """
        try:
            from app import bmi_backend_application as bmi_app
            bmi_app.initializeLogging()
            assert True
        except:
            assert False


    def test_bmi_app_database_initiation(self):
        """
        Test the BMI Backend Application database initiation.
        """
        try:
            from app import bmi_backend_application as bmi_app
            bmi_app.initializeDatabase(Constants.DB_TEST_NAME)
            assert True
        except:
            assert False


    def test_bmi_app_database_with_empty_name(self):
        """
        Test the BMI Backend Application database initiation with empty name.
        """
        try:
            from app import bmi_backend_application as bmi_app
            bmi_app.initializeDatabase("")
            assert False
        except:
            assert True


    def test_bmi_app_body_mass_index_calculation(self):
        """
        Test the BMI Backend Application body mass index calculation.
        """
        try:
            from app import bmi_backend_application as bmi_app
            bmi_app.generateBodyMassIndexData()
            assert True
        except:
            assert False


    def test_bmi_app_loadPatientDataIntoDb(self):
        """
        Test the BMI Backend Application load patient data into database.
        """
        try:
            from app import bmi_backend_application as bmi_app
            sqlHandler = bmi_app.initializeDatabase(Constants.DB_TEST_NAME)
            bmiPatientData = bmi_app.generateBodyMassIndexData()
            bmi_app.loadPatientDataIntoDb(sqlHandler, bmiPatientData)
            assert True
        except:
            assert False

    def test_bmi_app_updatePatientDataIntoDb(self):
        """
        Test the BMI Backend Application update patient data into database.
        """
        try:
            from app import bmi_backend_application as bmi_app
            sqlHandler = bmi_app.initializeDatabase(Constants.DB_TEST_NAME)
            bmiPatientData = bmi_app.generateBodyMassIndexData()
            bmi_app.updatePatientDataIntoDb(sqlHandler, bmiPatientData)
            assert True
        except:
            assert False


    def test_bmi_app_displayAllPatientsData(self):
        """
        Test the BMI Backend Application display all the patients.
        """
        try:
            from app import bmi_backend_application as bmi_app
            sqlHandler = bmi_app.initializeDatabase(Constants.DB_TEST_NAME)
            bmiPatientData = bmi_app.generateBodyMassIndexData()
            bmi_app.loadPatientDataIntoDb(sqlHandler, bmiPatientData)
            bmi_app.displayAllPatientsData(sqlHandler)
            assert True
        except:
            assert False

    def test_bmi_app_getOverweightPatientsCount(self):
        """
        Test the BMI Backend Application get the count of overweight patients.
        """
        try:
            from app import bmi_backend_application as bmi_app
            sqlHandler = bmi_app.initializeDatabase(Constants.DB_TEST_NAME)
            bmiPatientData = bmi_app.generateBodyMassIndexData()
            bmi_app.loadPatientDataIntoDb(sqlHandler, bmiPatientData)
            bmi_app.getOverweightPatientsCount(sqlHandler)
            assert True
        except:
            assert False
