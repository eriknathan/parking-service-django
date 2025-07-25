from django.urls import path, include
from rest_framework.routers import DefaultRouter
from customers.views import CustomersViewSet


router = DefaultRouter()
router.register('customers', CustomersViewSet)


urlpatterns = [
    path('', include(router.urls))
]
