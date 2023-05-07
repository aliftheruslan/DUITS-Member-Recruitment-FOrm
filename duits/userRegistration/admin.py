from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser
# Register your models here.
class CustomUserAdmin(BaseUserAdmin):
      list_display = ('registration_no','email','is_admin','is_active')
      search_fields = ('registration_no','email')
      # readonly_fields = ('date_joined','last_login')
      filter_horizontal=()
      list_filter=('is_active',)
      fieldsets=()
      add_fieldsets =(
       (None,{
        'classes':('wide'),
        'fields': ('registration_no','email','password'),
       }

       )
      )
      ordering=('registration_no',)
admin.site.register(CustomUser,CustomUserAdmin)