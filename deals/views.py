from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Deal, Alert

def deal_list(request):
    deals = Deal.objects.all()
    return JsonResponse({"deals": list(deals.values())})

def deal_detail(request, id):
    deal = Deal.objects.get(id=id)
    return JsonResponse({"deal": deal})

def alert_list(request):
    alerts = Alert.objects.all()
    return JsonResponse({"alerts": list(alerts.values())})

def alert_detail(request, id):
    alert = Alert.objects.get(id=id)
    return JsonResponse({"alert": alert})