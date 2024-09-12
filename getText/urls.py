from django.urls import path
from .views import GetTextApi


urlpatterns = [
    path('get-text/', GetTextApi.as_view())
]
            