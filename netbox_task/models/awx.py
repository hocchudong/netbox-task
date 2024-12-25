from django.db import models
from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet
from django.urls import reverse

class Protocol(ChoiceSet):    
    CHOICES = [
       ('http', 'HTTP', 'indigo'),
       ('https', 'HTTPS', 'green'),
    ]

class AWXServer(NetBoxModel):
    name = models.CharField(
        max_length=255, 
        null=False, 
        blank=False,
        unique=True,
    )
    
    protocol = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        choices=Protocol
    )
    
    base_url = models.CharField(
        max_length=255, 
        null=False, 
        blank=False,
        unique=True,
        help_text="AWX server endpoint with http/https in base url. Eg: my-awx.com"
    )
    
    ssl_insecure = models.BooleanField(
        default=False
    )
    
    user = models.CharField(
        max_length=255, 
        null=False, 
        blank=False,
        help_text="The user has sufficient authority to perform the tasks"
    )
    
    password = models.CharField(
        max_length=255, 
        null=False, 
        blank=False
    )
    
    comments = models.TextField(
        blank=True
    )
    
    def __str__(self):        
        return self.name
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_task:awxserver', args=[self.pk])


class AWXTemplate(NetBoxModel):
    template_name = template_id = models.CharField(
        max_length=255, 
        null=False,
        blank=False,
        unique=True
    )
    
    awx_server = models.ForeignKey(
        to="netbox_task.AWXServer",
        on_delete=models.PROTECT,
    )

    template_id = models.CharField(
        max_length=255, 
        null=False,
        blank=False
    )

    describe = models.TextField(
        blank=True
    )
    
    comments = models.TextField(
        blank=True
    )
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_task:awxtemplate', args=[self.pk])
    
    def __str__(self):        
        return self.template_name
    

    class Meta:
        unique_together = ('template_id', 'awx_server')