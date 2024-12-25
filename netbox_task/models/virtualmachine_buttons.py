from django.db import models
from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet
from django.urls import reverse
# from netbox_task.models import AWXTemplate

class VirtualMachineButtons(NetBoxModel):
    button_name = models.CharField(
        max_length=255, 
        null=False, 
        blank=False,
        unique=True,
    )
    
    awx_template = models.ForeignKey(
        to="netbox_task.AWXTemplate",
        on_delete=models.PROTECT,
    )
    
    extra_param = models.CharField(
        max_length=255, 
        null=False, 
        blank=False,
        help_text="These param will be passed into 'extra_vars' AWX Job"
    )
    
    comments = models.TextField(
        blank=True
    )
    
    def __str__(self):        
        return self.button_name
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_task:virtualmachinebutton', args=[self.pk])