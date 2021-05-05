from django import forms
   
# import GeeksModel from models.py
from .models import Save_test,Company,Quize
   
# create a ModelForm
class Save_test(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Save_test
        fields = "__all__"

class CompanyR(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Company
        fields = "__all__"

class QuizeF(forms.ModelForm):
    class Meta:
        model = Quize
        fields = "__all__"