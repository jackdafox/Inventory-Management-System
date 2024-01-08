from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/<int:pk>/', views.dashboard, name='dashboard'),
    path('dashboard/<int:pk>/delete/<int:pk2>/', views.dashboard_delete, name='dashboard-delete'),
    path('dashboard/<int:pk>/edit/<int:pk2>/', views.dashboard_edit, name='dashboard-edit'),
    path('dashboard/<int:pk>/edit-inventory/', views.dashboard_edit_inventory, name='dashboard-edit-inventory'),
    path('dashboard/<int:pk>/delete-inventory/', views.dashboard_delete_inventory, name='dashboard-delete-inventory'),
]