from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('user/<str:id>/', views.user_profile, name='profile')
]
