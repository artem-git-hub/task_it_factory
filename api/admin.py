from django.contrib import admin
from .models import Employee, Store, Visit

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """Отображение работника в админ панели"""
    list_display = ('name', 'phone_number')
    search_fields = ('name', )

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    """Отображение магазина в админ панели"""
    list_display = ('name', 'employee')
    search_fields = ('name', )

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    """Отображение посещения в админ панели"""
    list_display = ('store', 'visit_datetime', 'latitude', 'longitude')
    search_fields = ('store__employee__name', 'store__name')
