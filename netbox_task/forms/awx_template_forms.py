from django.forms import DateField
from django.urls import reverse_lazy

from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from netbox_task.models import AWXTemplate
from utilities.forms.fields import CommentField, DynamicModelChoiceField, TagFilterField
from utilities.forms.rendering import FieldSet
from utilities.forms.widgets import APISelect, DatePicker
from netbox.forms import NetBoxModelImportForm
from django import forms

class AWXTemplateForm(NetBoxModelForm):
    """Form for creating a new AWXServer object."""

    comments = CommentField()

    class Meta:
        model = AWXTemplate
        fields = (
            "template_name",
            "awx_server",
            "template_id",
            "describe",
            "comments",
        )
    


# class SoftwareProductVersionFilterForm(NetBoxModelFilterSetForm):
#     model = SoftwareProductVersion
#     fieldsets = (FieldSet(None, ("q", "tag")),)
#     tag = TagFilterField(model)


# class SoftwareProductVersionImportForm(NetBoxModelImportForm):
#     software_product = forms.CharField(
#         max_length=255,
#         required=True,
#         help_text="SoftwareProduct Name. If any SoftwareProduct not found, your import will be failed !!!"
#     )

#     release_type = forms.CharField(
#         max_length=255,
#         required=False,
#         help_text="A=Alpha, B=Beta, RD=Release candidate, S=Stable release. Default is Stable release"
#     )

#     def clean_software_product(self):
#         software_product=self.cleaned_data.get('software_product')
#         try:
#             software_product = SoftwareProduct.objects.get(name=software_product)
#             return software_product
#         except: 
#             return None


#     class Meta:
#         model = SoftwareProductVersion
#         fields = ('name', 'comments', 'release_date', 'documentation_url', 'end_of_support', 'filename', 'file_checksum',
#             'file_link', 'release_type', 'software_product'
#         )