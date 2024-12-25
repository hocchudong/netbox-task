from django.forms import DateField
from django.urls import reverse_lazy

from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from netbox_task.models import VirtualMachineButtons
from utilities.forms.fields import CommentField, DynamicModelChoiceField, TagFilterField
from utilities.forms.rendering import FieldSet
from utilities.forms.widgets import APISelect, DatePicker
from netbox.forms import NetBoxModelImportForm
from django import forms

class VirtualMachineButtonForm(NetBoxModelForm):
    """Form for creating a new AWXServer object."""

    comments = CommentField()
    extra_param = forms.MultipleChoiceField(
        choices=[
            ('VM ID', 'vm_id'), 
            ('VM Name', 'vm_name'), 
            ('VM IP', 'vm_ip'),
    ], widget=forms.SelectMultiple)

    class Meta:
        model = VirtualMachineButtons
        fields = (
            "button_name",
            "awx_template",
            "extra_param",
            "comments",
        )
