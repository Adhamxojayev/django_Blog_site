from .views import video 
from django.urls import path,include
from . import views
urlpatterns = [

    path('',views.index1),
    path('qalesan/',views.qalesan),
    path('video/',views.video),
]
