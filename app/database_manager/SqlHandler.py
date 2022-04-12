
from app.utilities import Constants
import sqlite3

class SqlHandler:
    '''
    This class is used to handle all database operations.
    '''
    def __init__(self, name):
        '''
        This method is used to initialize the database connection.
        :param name:
        '''
        self._conn = sqlite3.connect(name)
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        '''
        This method is used to get the connection object.
        :return:
        '''
        return self._conn

    @property
    def cursor(self):
        '''
        This method is used to get the cursor object.
        :return:
        '''
        return self._cursor

    def commit(self):
        '''
        This method is used to commit the changes to the database.
        :return:
        '''
        self.connection.commit()

    def close(self, commit=True):
        '''
        This method is used to close the database connection.
        :param commit:
        :return:
        '''
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql, params=None):
        '''
        This method is used to execute the sql query.
        :param sql:
        :param params:
        :return:
        '''
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        '''
        This method is used to fetch all the data from the database.
        :return:
        '''
        return self.cursor.fetchall()

    def fetchone(self):
        '''
        This method is used to fetch one row from the database.
        :return:
        '''
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        '''
        This method is used to execute the sql query.
        :param sql:
        :param params:
        :return:
        '''
        self.cursor.execute(sql, params or ())
        return self.fetchall()

    def dropTable(self):
        '''
        This method is used to drop the table.
        :return:
        '''
        self.connection.execute("DROP TABLE IF EXISTS BMI_DATA ")

    # Create a table in the database for gender, weight, height and healthrisk
    def createTable(self,replace=False):
        '''
        This method is used to create table
        :param replace:
        :return:
        '''
        if replace:
            self.dropTable()
        self.connection.execute('''CREATE TABLE IF NOT EXISTS BMI_DATA 
                 (ID INTEGER PRIMARY KEY NOT NULL,
                 GENDER           VARCHAR    NOT NULL,
                 CATEGORY         VARCHAR(30)    NOT NULL,
                 WEIGHT            FLOAT     NOT NULL,
                 HEIGHT            FLOAT     NOT NULL,
                 BMI        FLOAT           NOT NULL,
                 HEALTHRISK     VARCHAR(30)        NOT NULL);''')


    def insertData(self, gender, category, weight, height, bmi, healthrisk):
        '''

        :param gender:
        :param category:
        :param weight:
        :param height:
        :param bmi:
        :param healthrisk:
        :return:
        '''
        params = (gender,category,str(weight),str(height),str(bmi),healthrisk)
        query = "INSERT INTO BMI_DATA (GENDER,CATEGORY,WEIGHT,HEIGHT,BMI,HEALTHRISK) VALUES (?,?,?,?,?,?)"
        self.connection.execute(query,params)

    def getAllData(self):
        '''
        Fetch all the patient data
        :return:
        '''

        query = "SELECT * FROM BMI_DATA"
        cursor = self.connection.execute(query)
        return cursor.fetchall()


    def getOverweightCount(self):
        '''
        This method returns the overweight count
        :return:
        '''
        cursor  = self.connection.execute("Select * from BMI_DATA where CATEGORY = ?",(Constants.OVERWEIGHT,))
        return len(cursor.fetchall())

