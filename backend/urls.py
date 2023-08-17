from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from backend.account.views import UserViewSet


# Routers provide an easy way of automatically determining the URL conf.
# create router for product and everything and read about routers
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('backend.account.urls')),

]

