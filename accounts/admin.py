from django.contrib import admin

from accounts.models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UserModel(UserAdmin):
    list_display = ['username', 'get_user_type_display']


# Register your models here.
admin.site.register(CustomUser, UserModel)
admin.site.register(Accountant)
admin.site.register(Cao)
admin.site.register(Engineer)
admin.site.register(SubEngineer)
admin.site.register(PlanningOfficer)
admin.site.register(Wadasachib)
admin.site.register(Ward)
admin.site.register(FiscalYear)
admin.site.register(CurrentFiscalYear)
admin.site.register(Budget_Type)
admin.site.register(Procurement_Type)
admin.site.register(Project)
admin.site.register(UserCommitte)
admin.site.register(Cost_Estimate)








