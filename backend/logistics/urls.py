from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("orders", views.get_orders, name="orders"),
    path("orders/create", views.create_order, name="create order"),
    path("waypoints/<int:order_id>", views.create_waypoint, name="create waypoint"),
]