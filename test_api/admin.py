from django.contrib import admin
from . models import Quize,Company,Save_test,Test_name
admin.site.register(Quize)
admin.site.register(Test_name)
admin.site.register(Company)
admin.site.register(Save_test)