from django.urls import path
from . import views

urlpatterns = [
    path('', views.query_dbpedia, name='query_dbpedia'),
]
