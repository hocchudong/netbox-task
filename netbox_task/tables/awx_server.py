import django_tables2 as tables
from django.db.models import Count, F

from netbox.tables import NetBoxTable, ToggleColumn, columns
from netbox_task.models import AWXServer


class AWXServerTable(NetBoxTable):
    """Table for displaying AWXServer objects."""

    pk = ToggleColumn()
    name = tables.Column(
        linkify=True
    )
    password = tables.Column(
        accessor="password"
    )
    # name = tables.LinkColumn()
    
    # software_product = tables.Column(accessor="software_product", linkify=True)
    # manufacturer = tables.Column(accessor="software_product__manufacturer", linkify=True)
    # installations = tables.Column(accessor="get_installation_count")

    # tags = columns.TagColumn(url_name="plugins:netbox_svm:AWXServer_list")

    class Meta(NetBoxTable.Meta):
        model = AWXServer
        fields = (
            "name",
            "protocol",
            "base_url",
            "ssl_insecure",
            "user",
            "password",
            "comments",
        )
        default_columns = (
            "name",
            "protocol",
            "base_url",
            "ssl_insecure",
            "user",
            "password",
            # "comments",
        )
        # sequence = (
        #     "manufacturer",
        #     "software_product",
        #     "name",
        #     "installations",
        # )

    # def order_installations(self, queryset, is_descending):
    #     queryset = queryset.annotate(count=Count("softwareproductinstallation__id")).order_by(
    #         ("-" if is_descending else "") + "count"
    #     )
    #     return queryset, True