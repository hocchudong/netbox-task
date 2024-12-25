from django.forms import DateField
from django.urls import reverse_lazy

from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from netbox_task.models import AWXServer
from utilities.forms.fields import CommentField, DynamicModelChoiceField, TagFilterField
from utilities.forms.rendering import FieldSet
from utilities.forms.widgets import APISelect, DatePicker
from netbox.forms import NetBoxModelImportForm
from django import forms

class AWXServerForm(NetBoxModelForm):
    """Form for creating a new AWXServer object."""

    comments = CommentField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
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
