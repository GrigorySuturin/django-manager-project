from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'manager_app'

urlpatterns = [
    path('', views.ManagerListView.as_view(), name='index'),
    path('<int:pk>/', views.ManagerDetailView.as_view(), name='detail'),
]
