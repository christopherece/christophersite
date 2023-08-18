from django.contrib import admin

# Register your models here.
from .models import Company, Experience


admin.site.register(Company)
admin.site.register(Experience)