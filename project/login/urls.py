from django.urls import path, include
from login import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'market', views.MarketApi, basename = 'market')

router.register(r'bedroomdata', views.BedroomDataApi, basename = 'bedroomdata')

urlpatterns = [
    path("",include(router.urls))
]