from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
# Register your models here.

class CustomerUserAdmin(UserAdmin):
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    list_display = ('username','first_name','email','last_name','role','is_staff')


admin.site.register(User,CustomerUserAdmin)
admin.site.register(UserProfile)