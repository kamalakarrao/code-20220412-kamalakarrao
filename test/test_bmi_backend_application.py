from app.utilities import Constants


class TestCase:
    """
    Test class for the BMI Backend Application.
    """
    def test_bmi_backend_application(self):
        """
        Test the BMI Backend Application.
        """
        pass

    def test_bmi_backend_application_logging(self):
        """
        Test the BMI Backend Application logging.
        """
        try:
            from app import bmi_backend_application as bmi_app
            bmi_app.initializeLogging()
            assert True
        except:
            assert False


    def test_bmi_backend_application_database_initiation(self):
        """
        Test the BMI Backend Application database initiation.
        """
        try:
            from app import bmi_backend_application as bmi_app
            bmi_app.initializeDatabase(Constants.DB_TEST_NAME)
            assert True
        except:
            assert False