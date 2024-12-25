from netbox.plugins import PluginMenuButton, PluginMenuItem


try:
    from netbox.plugins import PluginMenu
    HAVE_MENU = True
except ImportError:
    HAVE_MENU = False
    PluginMenu = PluginMenuItem

menu_buttons = (
    PluginMenuItem(
        link="plugins:netbox_task:awxserver_list",
        link_text="AWX Servers",
        permissions=[
            "netbox_task.list_awx_server",
            "netbox_task.add_awx_server",
        ],
        buttons=(
            PluginMenuButton(
                "plugins:netbox_task:awxserver_add",
                "Add",
                "mdi mdi-plus-thick",
                permissions=["netbox_task.add_awx_server"],
            ),
        ),
    ),
    PluginMenuItem(
        link="plugins:netbox_task:awxtemplate_list",
        link_text="AWX Templates",
        permissions=[
            "netbox_task.list_awx_awxtemplate",
            "netbox_task.add_awx_awxtemplate"
        ],
        buttons=(
            PluginMenuButton(
                "plugins:netbox_task:awxtemplate_add",
                "Add",
                "mdi mdi-plus-thick",
                permissions=["netbox_task.add_awx_awxtemplate"],
            ),
        ),
    ),
    PluginMenuItem(
        link="plugins:netbox_task:virtualmachinebuttons_list",
        link_text="VM Buttons",
        permissions=[
            "netbox_task.list_virtualmachinebutton",
            "netbox_task.add_virtualmachinebutton"
        ],
        buttons=(
            PluginMenuButton(
                "plugins:netbox_task:virtualmachinebuttons_add",
                "Add",
                "mdi mdi-plus-thick",
                permissions=["netbox_task.add_virtualmachinebutton"],
            ),
        ),
    ),

)


if HAVE_MENU:
    menu = PluginMenu(
        label=f'Netbox Task',
        groups=(
            ('Netbox Task', menu_buttons),
        ),
        icon_class='mdi mdi-clipboard-text-multiple-outline'
    )
else:
    # display under plugins
    menu_items = menu_buttons