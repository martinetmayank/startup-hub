from django.urls.conf import path
from . import views

urlpatterns = [
    path('add/', views.add_startup, name='add'),
    path('<id>/update/', views.update_startup, name='update'),
    path('<id>/details/', views.view_startup, name='details'),
    path('view/', views.display_startup, name='view'),
]
