from rest_framework import serializers
from test_api.models import Company,Test_name,Quize,Save_test
from users.models import User

class companyS(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = Company
        fields=['company_name','tagline','website_url','company_type','user_id']

class Test_name_S(serializers.ModelSerializer):
    company = serializers.ReadOnlyField(source='profile.company')
    class Meta:
        model=Test_name
        fields=['test_name','company'] 

class QuizeS(serializers.ModelSerializer):
    # company=serializers.ReadOnlyField(source='profile.company')
    # test=serializers.ReadOnlyField(source='Test_name.test_name')
    class Meta:
        model=Quize
        fields=['question','option1','option2','option3','option4','answer','test','company']


class ScoreS(serializers.ModelSerializer):
    class Meta:
        model=Save_test
        fields=['company','test','user_id','score']