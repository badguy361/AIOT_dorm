from rest_framework import serializers 
from dorm.models import facilities_firstfloor,facilities_secondfloor,\
        facilities_thirdfloor,facilities_fourthfloor,facilities_fifthfloor


class FacilitiesSerializer(serializers.ModelSerializer):

    class Meta: #預設傳application json格式
        model = facilities_fourthfloor
        fields = '__all__'
        # fields = ('id',
        #           'facilities_name',
        #           'facilities_info'
        #           )