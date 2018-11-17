from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('user/<str:id>/', views.user_profile, name='profile'),
  path('review/<str:review_id>/', views.review_detail, name='review'),
  path('business/<str:business_id>/', views.business_detail, name='business'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
