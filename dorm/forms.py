from django import forms
from .models import facilities
class facilitiesModelForm(forms.ModelForm):
    class Meta:
        model = facilities
        fields = '__all__'