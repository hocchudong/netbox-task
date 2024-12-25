from rest_framework.routers import APIRootView

from netbox.api.viewsets import NetBoxModelViewSet
from netbox_task.api.serializers import (
    AWXServerSerializer
)
# from netbox_svm.filtersets import (
#     SoftwareProductFilterSet,
#     SoftwareProductVersionFilterSet,
#     SoftwareProductInstallationFilterSet,
#     SoftwareLicenseFilterSet,
# )
from netbox_task.models import AWXServer


class NetboxTaskRootView(APIRootView):
    """
    NetboxTask API root view
    """

    def get_view_name(self):
        return "NetboxTask"


class AWXServerViewSet(NetBoxModelViewSet):
    queryset = AWXServer.objects.all()
    serializer_class = AWXServerSerializer
