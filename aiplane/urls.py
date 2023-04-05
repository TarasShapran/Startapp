from django.urls import path

from aiplane.views import AirPlaneListCreateView, AirPlaneRetriveUpdateView

urlpatterns = [
    path('', AirPlaneListCreateView.as_view()),
    path('/<int:pk>', AirPlaneRetriveUpdateView.as_view())
]
