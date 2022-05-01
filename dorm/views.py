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

# def put(request):
#     if request.method == "PUT":
#         facilities_name = request.PUT["facilities_name"]
#         facilities_info = request.PUT["facilities_info"]
#         facilities.objects.filter(id=1).update(facilities_name=facilities_name, facilities_info=facilities_info)
#         return JsonResponse({"status":0})

# def get(request,id):
def get(request):

    context = facilities.objects.all()
    # name=[]
    # info=[]
    # voltage=[]
    # Date=[]
    # tmp=[]
    # for i in range(2,3): #3 is tricky
    #     # facilities_washing=facilities.objects.filter(facilities_name="washing machine")
    #     # tmp.append(facilities_washing[0])
    #     facilities_washing= facilities.objects.get(facilities_name="washing machine") # dry machine # toilet
    #     Date.append(facilities_washing.Date)
    #     name.append(facilities_washing.facilities_name)
    #     info.append(facilities_washing.facilities_info)
    #     voltage.append(facilities_washing.facilities_voltage)

    #     facilities_dry= facilities.objects.get(facilities_name="dry machine") # washing machine # toilet
    #     Date.append(facilities_dry.Date)
    #     name.append(facilities_dry.facilities_name)
    #     info.append(facilities_dry.facilities_info)
    #     voltage.append(facilities_dry.facilities_voltage)

    #     facilities_toilet= facilities.objects.get(facilities_name="toilet") # washing machine # toilet
    #     Date.append(facilities_toilet.Date)
    #     name.append(facilities_toilet.facilities_name)
    #     info.append(facilities_toilet.facilities_info)
    #     voltage.append(facilities_toilet.facilities_voltage)
    # context = {
    #     # 'tmp':tmp,
    #     'Date':Date,
    #     'facilities_list': name,
    #     'facilities_info': info,
    #     'facilities_voltage':voltage
    # }
    return render(request,"dorm.html",{"context":context})