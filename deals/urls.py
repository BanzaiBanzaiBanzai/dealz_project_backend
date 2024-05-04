from django.urls import path
from . import views

urlpatterns = [
    path('deals/', views.deal_list, name='deal_list'),
    path('deals/<int:id>/', views.deal_detail, name='deal_detail'),
    path('alerts/', views.alert_list, name='alert_list'),
    path('alerts/<int:id>/', views.alert_detail, name='alert_detail'),
]
