from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AI/', include("AI.api.urls"), name="AI-root")
]
