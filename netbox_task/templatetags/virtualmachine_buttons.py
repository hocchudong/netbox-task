from django import template
from netbox_task.models import VirtualMachineButtons

register = template.Library()

@register.simple_tag
def get_virtualmachine_buttons_object():
    return VirtualMachineButtons.objects.all()