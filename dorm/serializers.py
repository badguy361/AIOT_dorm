from rest_framework import serializers 
from dorm.models import facilities
 
 
class FacilitiesSerializer(serializers.ModelSerializer):
 
    class Meta: #預設傳application json格式
        model = facilities
        fields = '__all__'
        # fields = ('id',
        #           'facilities_name',
        #           'facilities_info'
        #           )