# netbox-task
Plugin dùng netbox để thực thi các nhiệm vụ/yêu cầu cần thiết qua ansible playbook hoặc script..

## Prerequisite

Netbox >= 4.0

## Description

Lets say i want to run some task for update infomation from VirtualMachine that be in our Hypervisor to the Netbox
or leverage exist ansible playbook to perform some simple action such as install package, reboot server ...

![Flow](images/flow.png)

## How to install 

Install this plugin from pypi

```
cd /opt/netbox
source venv/bin/activate
pip install netbox-task
```

Enable the plugin in `/opt/netbox/netbox/netbox/configuration.py`

```
PLUGINS = [
   'netbox_task'
]
```

Migrate the model to create newly databases

```
python netbox/manage.py migrate netbox_task
systemctl restart netbox
```

## Known Isssues
- The current version only support with Netbox VirtualMachine and only some default parameter will be passed into the request.
- There is no asynchronous processing, because task status that depend on AWX runtime. 