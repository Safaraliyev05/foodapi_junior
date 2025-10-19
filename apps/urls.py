from django.urls import path

from .views import FoodDetailView, FoodCreateView, FoodUpdateView, FoodDeleteView, FoodListView

urlpatterns = [
    path('foods', FoodListView.as_view(), name='courses'),
    path('food-create/', FoodCreateView.as_view(), name='course-create'),
    path('food/<int:pk>/', FoodDetailView.as_view(), name='course-detail'),
    path('food/<int:pk>/update/', FoodUpdateView.as_view(), name='course-update'),
    path('food/<int:pk>/delete/', FoodDeleteView.as_view(), name='course-delete'),
]
