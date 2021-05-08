from django import forms
   
# import GeeksModel from models.py
from .models import Save_test,Company,Quize,Test_name
   
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


class Test(forms.Form):
    test_name=forms.CharField(max_length=30)
    company_name=forms.CharField(max_length=50)
    def clean_company_name(self):
        company_name=self.cleaned_data["company_name"]
        if company_name == None:
            raise forms.validationError("Not be empty")
        return company_name 