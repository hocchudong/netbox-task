from netbox.api.routers import NetBoxRouter
from netbox_task.api.views import (
    NetboxTaskRootView,
    AWXServerViewSet
)

router = NetBoxRouter()
router.APIRootView = NetboxTaskRootView

router.register("awx_servers", AWXServerViewSet)

urlpatterns = router.urls