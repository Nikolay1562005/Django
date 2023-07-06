from django.urls import path
from .views import test_1


urlpatterns = [
    path('', test_1)
]