from netbox.plugins import PluginTemplateExtension
# from .models import SoftwareProductInstallation


class VirtualMachineSyncButton(PluginTemplateExtension):
    def buttons(self):
        return self.render('netbox_task/inc/virtual_machine_addition_button.html')

class VirtualMachineDeviceSyncButton(VirtualMachineSyncButton):
    model = 'virtualization.virtualmachine'
    kind = 'virtualmachine'
    # def right_page(self):
    #     return ""

template_extensions = (
    VirtualMachineDeviceSyncButton,
)
