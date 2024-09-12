from rest_framework import routers
from .views import VideosTxtsApi

router = routers.SimpleRouter()
router.register(r'videos-txts', VideosTxtsApi)

urlpatterns = router.urls
            