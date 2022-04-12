from app.utilities import Constants
class BodyMassIndex:
    def __init__(self, weight, height,gender):
        '''

        :param weight:
        :param height:
        :param gender:
        '''
        self.weight = float(weight)
        self.height = float(height)
        self.gender = gender
        self.bmi = self.weight / (self.height * self.height)

    def get_category(self):
        '''
        Returns the category of the BMI
        :return:
        '''
        if self.bmi <= 18.4:
            return Constants.UNDERWEIGHT
        elif self.bmi <= 24.9:
            return Constants.NORMAL_WEIGHT
        elif self.bmi <= 29.9:
            return Constants.OVERWEIGHT
        elif self.bmi <= 34.9:
            return Constants.MODERATELY_OBESE
        elif self.bmi <= 39.9:
            return Constants.SEVERELY_OBESE
        elif self.bmi > 40:
            return Constants.VERY_SEVERELY_OBESE

    def getHealthRisk(self):
        '''
        Returns the health risk of the BMI
        :return:
        '''
        if self.bmi <= 18.4:
            return Constants.MALNUTRITION_RISK
        elif self.bmi <= 24.9:
            return Constants.LOW_RISK
        elif self.bmi <= 29.9:
            return Constants.ENHANCED_RISK
        elif self.bmi <= 34.9:
            return Constants.MEDIUM_RISK
        elif self.bmi <= 39.9:
            return Constants.HIGH_RISK
        elif self.bmi > 40:
            return Constants.VERY_HIGH_RISK