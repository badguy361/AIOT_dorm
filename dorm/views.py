from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from requests import Response
from dorm import models
from dorm.models import facilities_firstfloor,facilities_secondfloor,\
        facilities_thirdfloor,facilities_fourthfloor,facilities_fifthfloor
from dorm.serializers import FacilitiesSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponseRedirect
import json
from django.core import serializers
    
# @api_view(['GET'])
# def getData(request):
#     data = facilities.objects.all()
#     serializer = FacilitiesSerializer(data,many=True)
#     return Response(serializer.data[0])

class FacilitiesViewSet1(viewsets.ModelViewSet):
    queryset = facilities_firstfloor.objects.all() #要加這行不然put沒法過
    serializer_class = FacilitiesSerializer
    
    def get(request):
        template_name = 'dorm.html'
        queryset = facilities_firstfloor.objects.all()
        return render(request, template_name, {"context":queryset})

    def getJsondata(request):
        queryset = serializers.serialize("json",facilities_firstfloor.objects.all())
        return HttpResponse(queryset)

    # def Home(request):
    #     template_name = 'dormitory.html'
    #     return render(request, template_name)

    # def connect(request):
    #     template_name = 'info.html'
    #     return render(request, template_name)


class FacilitiesViewSet2(viewsets.ModelViewSet):
    queryset = facilities_secondfloor.objects.all() #要加這行不然put沒法過
    serializer_class = FacilitiesSerializer
    
    def get(request):
        template_name = 'dorm.html'
        queryset = facilities_secondfloor.objects.all()
        return render(request, template_name, {"context":queryset})

    def getJsondata(request):
        queryset = serializers.serialize("json",facilities_secondfloor.objects.all())
        return HttpResponse(queryset)

    # def Home(request):
    #     template_name = 'dormitory.html'
    #     return render(request, template_name)

    # def connect(request):
    #     template_name = 'info.html'
    #     return render(request, template_name)


class FacilitiesViewSet3(viewsets.ModelViewSet):
    queryset = facilities_thirdfloor.objects.all() #要加這行不然put沒法過
    serializer_class = FacilitiesSerializer
    
    def get(request):
        template_name = 'dorm.html'
        queryset = facilities_thirdfloor.objects.all()
        return render(request, template_name, {"context":queryset})

    def getJsondata(request):
        queryset = serializers.serialize("json",facilities_thirdfloor.objects.all())
        return HttpResponse(queryset)

    # def Home(request):
    #     template_name = 'dormitory.html'
    #     return render(request, template_name)

    # def connect(request):
    #     template_name = 'info.html'
    #     return render(request, template_name)


class FacilitiesViewSet4(viewsets.ModelViewSet):
    queryset = facilities_fourthfloor.objects.all() #要加這行不然put沒法過
    serializer_class = FacilitiesSerializer
    
    def get(request):
        template_name = 'dorm.html'
        queryset = facilities_fourthfloor.objects.all()
        return render(request, template_name, {"context":queryset})

    def getJsondata(request):
        queryset = serializers.serialize("json",facilities_fourthfloor.objects.all())
        return HttpResponse(queryset)

    def Home(request):
        template_name = 'dormitory.html'
        return render(request, template_name)

    def feedbacks(request):
        template_name = 'form.html'
        return render(request, template_name)

    def connect(request):
        template_name = 'info.html'
        return render(request, template_name)

class FacilitiesViewSet5(viewsets.ModelViewSet):
    # model = facilities
    queryset = facilities_fifthfloor.objects.all() #要加這行不然put沒法過
    serializer_class = FacilitiesSerializer #要加這行不然put沒法過，應該是serializer去吃queryset且是由queryset決定是哪層樓

    def get(request):
        template_name = 'dorm.html'
        queryset = facilities_fifthfloor.objects.all()
        return render(request, template_name, {"context":queryset})

    def getJsondata(request):
        queryset = serializers.serialize("json",facilities_fifthfloor.objects.all())
        return HttpResponse(queryset)
        # return JsonResponse({f"Date":queryset[0].Date})

    # def Home(request):
    #     template_name = 'dormitory.html'
    #     return render(request, template_name)

    # def connect(request):
    #     template_name = 'info.html'
    #     return render(request, template_name)

    # @csrf_exempt #預設傳x-www-form-urlencoded格式 #form的傳法
    # def post(request):
    #     if request.method == "POST":
    #         try:
    #             Date = request.POST["Date"]
    #             facilities_name = request.POST["facilities_name"]
    #             facilities_info = request.POST["facilities_info"]
    #             facilities_voltage = request.POST["facilities_voltage"]
    #             facilities.objects.create(Date=Date, facilities_name=facilities_name, facilities_info=facilities_info, facilities_voltage=facilities_voltage)
    #             print("Date:",Date,"facilities_name:",facilities_name,"facilities_info:",facilities_info,"facilities_voltage:",facilities_voltage)
    #             return JsonResponse({"post":"success"})
    #             # return render(request, 'dorm.html', {"context":facilities.objects.all()})
    #         except:
    #             print("post fail",request.POST)
    #             print(request.body)
    #             return JsonResponse({"post":"fail"})

# @csrf_exempt
# def post(request):
#     if request.method == "POST":
#         try:
#             Date = request.POST["Date"]
#             facilities_name = request.POST["facilities_name"]
#             facilities_info = request.POST["facilities_info"]
#             facilities_voltage = request.POST["facilities_voltage"]
#             facilities.objects.create(Date=Date, facilities_name=facilities_name, facilities_info=facilities_info, facilities_voltage=facilities_voltage)
#             return JsonResponse({"post":"success"})
            
#         except:
#             return JsonResponse({"post":"fail"})

# # def put(request):
# #     if request.method == "PUT":
# #         facilities_name = request.PUT["facilities_name"]
# #         facilities_info = request.PUT["facilities_info"]
# #         facilities.objects.filter(id=1).update(facilities_name=facilities_name, facilities_info=facilities_info)
# #         return JsonResponse({"status":0})

# def get(request):
#     context = facilities.objects.all()
#     return render(request,"dorm.html",{"context":context})