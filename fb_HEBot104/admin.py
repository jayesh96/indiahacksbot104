# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Hospital

class HospitalAdmin(admin.ModelAdmin):
	list_display = ["title","address","pincode","contact","beds"]

admin.site.register(Hospital,HospitalAdmin)