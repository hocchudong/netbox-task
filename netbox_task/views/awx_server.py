from netbox.views import generic
from netbox_task.models import AWXServer
from netbox_task import forms, tables

class AWXServerListView(generic.ObjectListView):
    """View for listing all existing AWXServer."""

    queryset = AWXServer.objects.all()
    table = tables.AWXServerTable

class AWXServerView(generic.ObjectView):
    """Display AWXServer details"""

    queryset = AWXServer.objects.all()

    # def get_extra_context(self, request, instance):
    #     installation_count = instance.get_installation_count()
    #     return {"installations": installation_count}


class AWXServerEditView(generic.ObjectEditView):
    """View for editing and creating a AWXServer instance."""

    queryset = AWXServer.objects.all()
    form = forms.AWXServerForm


class AWXServerDeleteView(generic.ObjectDeleteView):
    """View for deleting a AWXServer instance"""

    queryset = AWXServer.objects.all()


class AWXServerBulkDeleteView(generic.BulkDeleteView):
    queryset = AWXServer.objects.all()
    table = tables.AWXServerTable
