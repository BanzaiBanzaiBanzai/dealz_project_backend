from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def alert_list(request):
    # Dummy response
    return JsonResponse({"alerts": []})

def alert_detail(request, id):
    # Dummy response
    return JsonResponse({"alert": {"id": id}})
