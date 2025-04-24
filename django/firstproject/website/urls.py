from django.urls import path
from .views import index, about

urlpatterns = [
    path('', index, name='home'),
    path('about-my-compnay', about, name='about'),
]