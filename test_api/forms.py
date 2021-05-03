from django import forms
   
# import GeeksModel from models.py
from .models import Save_test
   
# create a ModelForm
class Save_test(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Save_test
        fields = "__all__"