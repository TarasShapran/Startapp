from django.urls import path

from cars.views import CarsListCreateView, CarsRetrieveUpdatesDeleteView

urlpatterns = [
    path('', CarsListCreateView.as_view()),
    path('/<int:pk>', CarsRetrieveUpdatesDeleteView.as_view())
]
