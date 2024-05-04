from django.urls import path
from . import views

urlpatterns = [
    path('', views.alert_list, name='alert_list'),
    path('<int:id>/', views.alert_detail, name='alert_detail'),
]
