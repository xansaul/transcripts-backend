from django.urls import path
from .views import GetTextApi


urlpatterns = [
    path('generate/get-text/', GetTextApi.as_view())
]
            