import django_tables2 as tables
from django.db.models import Count, F

from netbox.tables import NetBoxTable, ToggleColumn, columns
from netbox_task.models import AWXTemplate


class AWXTemplateTable(NetBoxTable):
    """Table for displaying AWXTemplate objects."""

    pk = ToggleColumn()
    template_name = tables.Column(
        linkify=True
    )


    class Meta(NetBoxTable.Meta):
        model = AWXTemplate
        fields = (
            "template_name",
            "awx_server",
            "template_id",
            "describe",
            "comments",
        )
        default_columns = (
            "template_name",
            "awx_server",
            "template_id",
            "describe",
            # "comments",
        )
        