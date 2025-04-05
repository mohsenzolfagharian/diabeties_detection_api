from django.urls import path
from AI.api.views import DiabetesPredictionView

urlpatterns = [
    path('predict/', DiabetesPredictionView.as_view(), name="PREDICT")
]
