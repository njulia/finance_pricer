from django.urls import path
from . import views

urlpatterns = [
    path('ir_swap', views.interest_rate_swap_view, name='interest_rate_swap'),
]
