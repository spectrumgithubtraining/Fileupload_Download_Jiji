from django.contrib import admin

# Register your models here.
# yourapp/admin.py
from django.contrib import admin
from .models import UploadedFile

admin.site.register(UploadedFile)
