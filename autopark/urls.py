from django.urls import path

from autopark.views import AutoParkListView, AutoParkAddCarView, AutoParkRetrieveDestroyView

urlpatterns = [
    path('', AutoParkListView.as_view()),
    path('/<int:pk>/add_car', AutoParkAddCarView.as_view()),
    path('/<int:pk>', AutoParkRetrieveDestroyView.as_view())
]
