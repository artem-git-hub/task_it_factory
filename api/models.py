"""Модели для API приложения"""
from django.db import models

class Employee(models.Model):
    """Модель работника"""
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    
    def __str__(self):
        return str(f"Name: {self.name}; Phone: {self.phone_number};")

class Store(models.Model):
    """Модель торговой точки"""
    name = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return str(f"Name: {self.name};")

class Visit(models.Model):
    """Модель посещения"""
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    visit_datetime = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return str(f"{self.store} - {self.visit_datetime};")
