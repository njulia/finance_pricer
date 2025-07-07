from django.urls import path
from . import views

urlpatterns = [
    path('bond_future', views.bond_future_view, name='bond_future'),
]
