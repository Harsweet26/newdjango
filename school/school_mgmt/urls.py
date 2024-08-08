from django.urls import path
from .views import*

urlpatterns = [
    # path('home/',hello),
    # path('room/',structure),
    path('store/', store),
    path('mac/', mac),
    path('ipad/', ipad),
]
