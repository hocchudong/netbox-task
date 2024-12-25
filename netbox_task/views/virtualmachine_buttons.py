from netbox.views import generic
from netbox_task.models import VirtualMachineButtons
from netbox_task import forms, tables
from django.views.generic import View
import requests
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages
import json

class VirtualMachineButtonsListView(generic.ObjectListView):
    """View for listing all existing VirtualMachineButtons."""

    queryset = VirtualMachineButtons.objects.all()
    table = tables.VirtualMachineButtonsTable

class VirtualMachineButtonsView(generic.ObjectView):
    """Display VirtualMachineButtons details"""

    queryset = VirtualMachineButtons.objects.all()


class VirtualMachineButtonsEditView(generic.ObjectEditView):
    """View for editing and creating a VirtualMachineButtons instance."""

    queryset = VirtualMachineButtons.objects.all()
    form = forms.VirtualMachineButtonForm


class VirtualMachineButtonsDeleteView(generic.ObjectDeleteView):
    """View for deleting a VirtualMachineButtons instance"""

    queryset = VirtualMachineButtons.objects.all()


class VirtualMachineButtonsBulkDeleteView(generic.BulkDeleteView):
    queryset = VirtualMachineButtons.objects.all()
    table = tables.VirtualMachineButtonsTable
    

    
class VirtualMachineButtonsRunjob(View):
    def post(self, request):
        
        vm_id = request.POST['vm_id']
        vm_name = request.POST['vm_name']
        vm_ip = request.POST['vm_ip']
        button_id = request.POST['button_id']

        button = VirtualMachineButtons.objects.get(id=button_id)
        
        awx_template_id = button.awx_template.template_id
        awx_protocol = button.awx_template.awx_server.protocol
        awx_base_url = button.awx_template.awx_server.base_url
        awx_user = button.awx_template.awx_server.user
        awx_password = button.awx_template.awx_server.password
        
        try:
            url = f"{awx_protocol}://{awx_base_url}/api/v2/job_templates/{awx_template_id}/launch/"
            headers = {'Content-Type': 'application/json'}
            data = {
                "extra_vars" : {
                    "vm_id": vm_id,
                    "vm_name": vm_name,
                    "vm_ip": vm_ip
                }
            }
            
            response = requests.post(url, auth=(awx_user, awx_password), headers=headers, data=json.dumps(data))
            if response.status_code == 201:
                messages.success(request, f"{button.button_name} has been Submit")
            else: 
                messages.error(request, f"{button.button_name} cannot Submit")      
        except Exception as ex:
            messages.error(request, "Something went wrong !!")
            print(ex)      
        
        return redirect(reverse('virtualization:virtualmachine', args=[vm_id]))   
