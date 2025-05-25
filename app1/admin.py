from django.contrib import admin
from .models import Role

# Register your models here.
class RoleAdmin(admin.ModelAdmin):
    model = Role
    list_display = [i.name for i in Role._meta.fields]

admin.site.register(Role,RoleAdmin)