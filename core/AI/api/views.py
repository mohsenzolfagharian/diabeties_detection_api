# views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
import numpy as np
import tensorflow as tf
from joblib import load
from AI.models import ModelPrediction
from AI.api.serializer import DiabetiesSerializer

class DiabetesPredictionView(generics.CreateAPIView):
    queryset = ModelPrediction.objects.all()
    serializer_class = DiabetiesSerializer
    model = tf.keras.models.load_model('diabetes_model.h5')
    scaler = load('scaler.joblib')

    def perform_create(self, serializer):
        data = serializer.validated_data
        
        # Prepare input array
        input_features = np.array([[
            data['pregnancies'],
            data['glucose'],
            data['bp'],
            data['skin_thickness'],
            data['insulin'],
            data['bmi'],
            data['dpf'],
            data['age']
        ]])
        
        # Scale features
        scaled_data = self.scaler.transform(input_features)
        
        # Make prediction
        prediction = self.model.predict(scaled_data)
        probability = float(prediction[0][0])
        prediction_class = int(probability > 0.5)
        
        # Save prediction with instance
        serializer.save(predict=prediction_class)
    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )