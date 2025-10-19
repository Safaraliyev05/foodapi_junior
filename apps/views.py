from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from .models import Food
from .serializers import FoodSerializer


@extend_schema(tags=["Food List"])
class FoodListView(ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


@extend_schema(tags=['Course Detail'])
class FoodDetailView(RetrieveAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


@extend_schema(tags=['Course Create'])
class FoodCreateView(CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


@extend_schema(tags=['Course Update'])
class FoodUpdateView(UpdateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


@extend_schema(tags=['Course Delete'])
class FoodDeleteView(DestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
