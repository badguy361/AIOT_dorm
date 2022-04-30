from rest_framework import serializers 
from dorm.models import facilities
 
 
class FacilitiesSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = facilities
        fields = ('id',
                  'facilities_name',
                  'facilities_info'
                  )