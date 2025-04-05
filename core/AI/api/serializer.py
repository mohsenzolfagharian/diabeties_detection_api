from rest_framework import serializers
from AI.models import ModelPrediction


class DiabetiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelPrediction
        fields = ['pregnancies', 'glucose', "bp", "skin_thickness", "insulin", "bmi", "dpf", "age", "predict"]
        read_only_fields = ['predict']
    