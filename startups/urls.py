from django.urls.conf import path
from . import views

urlpatterns = [
    path('add/', views.add_startup, name='add'),
]
