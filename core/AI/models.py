from django.db import models


class ModelPrediction(models.Model):
    pregnancies = models.FloatField()
    glucose = models.FloatField()
    bp = models.FloatField()
    skin_thickness = models.FloatField()
    insulin = models.FloatField()
    bmi = models.FloatField()
    dpf = models.FloatField()
    age = models.IntegerField()
    predict = models.IntegerField()
    
    def __str__(self):
        return str(self.predict)