# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView,
)
from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, SensorSerializer, MeasurementCreateSerializer


class SensorsViewCreate(ListCreateAPIView):
    """1. Создать датчик. Указываются название и описание датчика.
    4. Получить список датчиков.
    """

    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorUpdate(RetrieveUpdateAPIView):
    """2. Изменить датчик. Указываются название и/или описание.
    5. Получить информацию по конкретному датчику.
    """

    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementCreate(CreateAPIView):
    """3. Добавить измерение. Указываются ID датчика и температура."""

    serializer_class = MeasurementCreateSerializer
