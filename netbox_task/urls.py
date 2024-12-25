from django.urls import path

from netbox.views.generic import ObjectChangeLogView
from netbox_task import views
from netbox_task.models import AWXServer, AWXTemplate, VirtualMachineButtons

urlpatterns = [
    # AWX Server
    path(
        "awx-servers/", 
        views.AWXServerListView.as_view(), 
        name="awxserver_list"
    ),
    path(
        "awx-servers/add/", 
        views.AWXServerEditView.as_view(), 
        name="awxserver_add"
    ),
    path(
        "awx-servers/delete/", 
        views.AWXServerBulkDeleteView.as_view(), 
        name="awxserver_bulk_delete"
    ),
    path(
        "awx-servers/<int:pk>/", 
        views.AWXServerView.as_view(), 
        name="awxserver"
    ),
    path(
        "awx-servers/<int:pk>/delete/",
        views.AWXServerDeleteView.as_view(), 
        name="awxserver_delete"
    ),
    path(
        "awx-servers/<int:pk>/edit/", 
        views.AWXServerEditView.as_view(), 
        name="awxserver_edit"
    ),
    path(
        "awx-servers/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="awxserver_changelog",
        kwargs={"model": AWXServer},
    ),
    
    
    # AWX Task
    path(
        "awx-templates/", 
        views.AWXTemplateListView.as_view(), 
        name="awxtemplate_list"
    ),
    path(
        "awx-templates/add/", 
        views.AWXTemplateEditView.as_view(), 
        name="awxtemplate_add"
    ),
    path(
        "awx-templates/delete/", 
        views.AWXTemplateBulkDeleteView.as_view(), 
        name="awxtemplate_bulk_delete"
    ),
    path(
        "awx-templates/<int:pk>/", 
        views.AWXTemplateView.as_view(), 
        name="awxtemplate"
    ),
    path(
        "awx-templates/<int:pk>/delete/",
        views.AWXTemplateDeleteView.as_view(), 
        name="awxtemplate_delete"
    ),
    path(
        "awx-templates/<int:pk>/edit/", 
        views.AWXTemplateEditView.as_view(), 
        name="awxtemplate_edit"
    ),
    path(
        "awx-templates/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="awxtemplate_changelog",
        kwargs={"model": AWXTemplate},
    ),
    # path(
    #     'awx-servers/import/', 
    #     views.SoftwareProductBulkImportView.as_view(), 
    #     name='softwareproduct_import'
    # )
    
    
    # Virtual Machine Buttons 
    path(
        "vm-buttons/", 
        views.VirtualMachineButtonsListView.as_view(), 
        name="virtualmachinebuttons_list"
    ),
    path(
        "vm-buttons/add/", 
        views.VirtualMachineButtonsEditView.as_view(), 
        name="virtualmachinebuttons_add"
    ),
    path(
        "vm-buttons/delete/", 
        views.VirtualMachineButtonsBulkDeleteView.as_view(), 
        name="virtualmachinebuttons_bulk_delete"
    ),
    path(
        "vm-buttons/<int:pk>/", 
        views.VirtualMachineButtonsView.as_view(), 
        name="virtualmachinebutton"
    ),
    path(
        "vm-buttons/<int:pk>/delete/",
        views.VirtualMachineButtonsDeleteView.as_view(), 
        name="virtualmachinebuttons_delete"
    ),
    path(
        "vm-buttons/<int:pk>/edit/", 
        views.VirtualMachineButtonsEditView.as_view(), 
        name="virtualmachinebuttons_edit"
    ),
    path(
        "vm-buttons/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="virtualmachinebuttons_changelog",
        kwargs={"model": VirtualMachineButtons},
    ),
    path(
        "vm-buttons/runjob/",
        views.VirtualMachineButtonsRunjob.as_view(), 
        name="virtualmachinebuttons_runjob"
    ),
]