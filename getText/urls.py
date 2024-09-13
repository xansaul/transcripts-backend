from django.urls import path
from .views import GetTextApi,Seed


urlpatterns = [
    path('generate/get-text/', GetTextApi.as_view()),
    path('generate/seed/', Seed.as_view()),
]
            