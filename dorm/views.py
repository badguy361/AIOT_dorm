from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from dorm import models
from dorm.models import facilities
from django.views.decorators.csrf import csrf_exempt
from dorm.serializers import FacilitiesSerializer

# Create your views here.
@csrf_exempt
def post(request):
    if request.method == "POST":
        try:
            Date = request.POST["Date"]
            facilities_name = request.POST["facilities_name"]
            facilities_info = request.POST["facilities_info"]
            facilities_voltage = request.POST["facilities_voltage"]
            facilities.objects.create(Date=Date, facilities_name=facilities_name, facilities_info=facilities_info, facilities_voltage=facilities_voltage)
            return JsonResponse({"status":0})
            
        except:
            return JsonResponse({"status":1})

def put(request):
    if request.method == "PUT":
        facilities_name = request.PUT["facilities_name"]
        facilities_info = request.PUT["facilities_info"]
        facilities.objects.filter(id=1).update(facilities_name=facilities_name, facilities_info=facilities_info)
        return JsonResponse({"status":0})

# def get(request,id):
def get(request):
    name=[]
    info=[]
    for i in range(1,3): #3 is tricky
        facilities_list= facilities.objects.get(id=1)
        name.append(facilities_list.facilities_name)
        info.append(facilities_list.facilities_info)
    context = {
        'facilities_list': name,
        'facilities_info': info
    }
    return render(request,"hello.html",context)