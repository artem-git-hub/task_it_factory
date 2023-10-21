"""Сериализаторы для отображения моделей"""
from rest_framework import serializers
from .models import Employee, Store, Visit

class EmployeeSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения работника"""
    class Meta:
        """Класс отображения полей"""
        model = Employee
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения торговой точки"""
    class Meta:
        """Класс отображения полей"""
        model = Store
        fields = '__all__'

class VisitSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения посещения"""
    class Meta:
        """Класс отображения полей"""
        model = Visit
        fields = '__all__'


class ViewVisitSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения посещения"""
    class Meta:
        """Класс отображения полей"""
        model = Visit
        fields = ('id', 'visit_datetime')