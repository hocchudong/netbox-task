from netbox.plugins import PluginConfig

__version__ = "1.0.2"


class DeviceSyncConfig(PluginConfig):
    name = "netbox_task"
    verbose_name = "Netbox Task"
    description = "Execute Any Ansbile Playbook from Netbox"
    version = __version__
    author = "huytm"
    author_email = "manhhuy173@gmail.com"
    base_url = "netbox_task"
    required_settings = []
    default_settings = {"version_info": False}


config = DeviceSyncConfig