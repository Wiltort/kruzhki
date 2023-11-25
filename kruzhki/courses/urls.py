from django.urls import include, path
from .views import RubricViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('api/v1/rubrics', RubricViewSet)


urlpatterns = [
    path('', include(router.urls)),
]