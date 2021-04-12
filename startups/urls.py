from django.urls.conf import path
from . import views

urlpatterns = [
    path('add/', views.add_startup, name='add'),
    path('update/<str>', views.update_startup, name='update'),
    path('details/<str>/', views.view_startup, name='details'),
    path('view/', views.display_startup, name='view'),
]
