from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from dorm import models
from dorm.models import facilities
from django.views.decorators.csrf import csrf_exempt
from dorm.serializers import FacilitiesSerializer
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponseRedirect

# Create your views here.
class FacilitiesView(View):
    initial = facilities.objects.all()
    template_name = 'dorm.html'
    def get(self, request):
        initial=self.initial
        return render(request, self.template_name, {"context":initial})
        # return HttpResponse('result')
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         # <process form cleaned data>
    #         return HttpResponseRedirect('/success/')

    #     return render(request, self.template_name, {'context': initial})

# @csrf_exempt
def post(request):
    if request.method == "POST":
        try:
            Date = request.POST["Date"]
            facilities_name = request.POST["facilities_name"]
            facilities_info = request.POST["facilities_info"]
            facilities_voltage = request.POST["facilities_voltage"]
            facilities.objects.create(Date=Date, facilities_name=facilities_name, facilities_info=facilities_info, facilities_voltage=facilities_voltage)
            return JsonResponse({"post":"success"})
            
        except:
            return JsonResponse({"post":"fail"})

# # def put(request):
# #     if request.method == "PUT":
# #         facilities_name = request.PUT["facilities_name"]
# #         facilities_info = request.PUT["facilities_info"]
# #         facilities.objects.filter(id=1).update(facilities_name=facilities_name, facilities_info=facilities_info)
# #         return JsonResponse({"status":0})

def get(request):
    context = facilities.objects.all()
    return render(request,"dorm.html",{"context":context})