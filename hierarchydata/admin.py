from django.contrib import admin
from .models import HierarchyData

class HierarchyDataAdmin(admin.ModelAdmin):
    model = HierarchyData
    list_display = ['si_no', 'title']

admin.site.register(HierarchyData, HierarchyDataAdmin)
