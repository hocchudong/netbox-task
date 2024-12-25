from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from netbox_task.models import AWXServer, AWXTemplate, VirtualMachineButtons


class AWXServerSerializer(NetBoxModelSerializer):
    display = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:netbox_task-api:awx_server-detail")

    class Meta:
        model = AWXServer
        fields = (
            "id",
            "name",
            "protocol",
            "base_url",
            "ssl_insecure",
            "user",
            "password",
            "comments",
        )
        brief_fields = ("id", "base_url")

    def get_display(self, obj):
        return f"{obj}"
    
class AWXTemplateSerializer(NetBoxModelSerializer):
    display = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:netbox_task-api:awx_template-detail")

    class Meta:
        model = AWXTemplate
        fields = (
            "id",
            "template_name",
            "awx_server",
            "template_id",
            "describe",
            "comments",
        )
        brief_fields = ("id", "template_name")

    def get_display(self, obj):
        return f"{obj}"
    
class VirtualMachineButtonsSerializer(NetBoxModelSerializer):
    display = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:netbox_task-api:virtual_machine_buttons-detail")

    class Meta:
        model = VirtualMachineButtons
        fields = (
            "id",
            "button_name",
            "awx_template",
            "extra_param",
            "comments",
        )
        brief_fields = ("id", "button_name")

    def get_display(self, obj):
        return f"{obj}"