from django.contrib import admin
from app2.models import Profile
# Register your models here.
#admin.site.register(Profile)

# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ['name', 'email', 'phone', 'age']

# admin.site.register(Profile, ProfileAdmin)


# using decorator

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'age']