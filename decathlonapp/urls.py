from rest_framework import routers

from decathlonapp.views import SportClassifierViewSet

router = routers.DefaultRouter()
router.register(r'sportclassifier', SportClassifierViewSet, basename='sportclassifier')
urlpatterns = router.urls
