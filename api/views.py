"""Представления для работы с конечными точками API, связанными с магазином."""
from datetime import datetime
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Store, Employee
from .serializers import StoreSerializer, VisitSerializer, ViewVisitSerializer

class StoresByPhoneNumber(generics.ListAPIView):
    """Представление для поиска магазинов по номеру телефона.
    Это представление позволяет получить список магазинов, 
    связанных c определенным телефонным номером."""
    serializer_class = StoreSerializer

    def get_queryset(self):
        phone_number = self.kwargs['phone_number']
        return Store.objects.filter(employee__phone_number=phone_number)


class CreateVisit(generics.CreateAPIView):
    serializer_class = VisitSerializer

    def create(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        store_pk = request.data.get('store_pk')
        coordinates = request.data.get('coordinates')

        try:
            employee = Employee.objects.get(phone_number=phone_number)
            store = Store.objects.get(pk=store_pk)

            # Проверьте, что переданный номер телефона Работника привязан к указанной Торговой точке.
            if store.employee != employee:
                return Response({"detail": "Номер телефона Работника не соответствует указанной Торговой точке."}, status=status.HTTP_400_BAD_REQUEST)

            # Создайте запись о посещении с текущей датой и временем.
            visit_datetime = datetime.now()
            serializer = self.get_serializer(data={
                "store": store.pk,
                "visit_datetime": visit_datetime,
                "latitude": coordinates['latitude'],
                "longitude": coordinates['longitude']
            })
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            visit = serializer.save()

            return Response(ViewVisitSerializer(visit).data, status=status.HTTP_201_CREATED)
        except Employee.DoesNotExist:
            return Response({"detail": "Работник с указанным номером телефона не найден."}, status=status.HTTP_404_NOT_FOUND)
        except Store.DoesNotExist:
            return Response({"detail": "Торговая точка с указанным PK не найдена."}, status=status.HTTP_404_NOT_FOUND)
        