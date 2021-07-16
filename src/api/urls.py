from rest_framework.routers import DefaultRouter

from . import views

api_name = 'api'

router = DefaultRouter()
router.register(prefix='articles', viewset=views.PostAPIViewSet, basename='article')

urlpatterns = router.urls
