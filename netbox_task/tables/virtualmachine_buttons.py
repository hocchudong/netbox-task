import django_tables2 as tables
from django.db.models import Count, F

from netbox.tables import NetBoxTable, ToggleColumn, columns
from netbox_task.models import VirtualMachineButtons


class VirtualMachineButtonsTable(NetBoxTable):
    """Table for displaying VirtualMachineButtons objects."""

    pk = ToggleColumn()
    button_name = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = VirtualMachineButtons
        fields = (
            "button_name",
            "awx_template",
            "extra_param",
            "comments",
        )
        default_columns = (
            "button_name",
            "awx_template",
            "extra_param",
        )
        