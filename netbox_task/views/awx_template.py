from netbox.views import generic
from netbox_task.models import AWXTemplate
from netbox_task import forms, tables

class AWXTemplateListView(generic.ObjectListView):
    """View for listing all existing AWXTemplate."""

    queryset = AWXTemplate.objects.all()
    table = tables.AWXTemplateTable

class AWXTemplateView(generic.ObjectView):
    """Display AWXTemplate details"""

    queryset = AWXTemplate.objects.all()

    # def get_extra_context(self, request, instance):
    #     installation_count = instance.get_installation_count()
    #     return {"installations": installation_count}


class AWXTemplateEditView(generic.ObjectEditView):
    """View for editing and creating a AWXTemplate instance."""

    queryset = AWXTemplate.objects.all()
    form = forms.AWXTemplateForm


class AWXTemplateDeleteView(generic.ObjectDeleteView):
    """View for deleting a AWXTemplate instance"""

    queryset = AWXTemplate.objects.all()


class AWXTemplateBulkDeleteView(generic.BulkDeleteView):
    queryset = AWXTemplate.objects.all()
    table = tables.AWXTemplateTable


# class AWXTemplateBulkImportView(generic.BulkImportView):
#     queryset = AWXTemplate.objects.all()
#     model_form = forms.AWXTemplateImportForm


# views.py
# from django.http import JsonResponse
# import requests

# def launch_job_template(request):
#     url = 'http://172.16.99.150:8081/api/v2/job_templates/9/launch/'
#     username = 'admin'
#     password = 'bCD8kBLta7TTZ0ZuWzX6R224SuHlWw0g'
#     headers = {'Content-Type': 'application/json'}
#     data = '{"extra_vars": {"host": "172.16.99.151"}}'

#     response = requests.post(url, auth=(username, password), headers=headers, data=data)

#     print(response)
#     print(response.text)
#     print(response.json())
    
    
#     if response.status_code == 201:
#         return JsonResponse({"message": "Sync successfully"})
#     else:
#         return JsonResponse({"error": "Failed to launch job"}, status=500)