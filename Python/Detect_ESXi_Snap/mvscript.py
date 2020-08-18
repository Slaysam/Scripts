import configparser
from pyVim.connect import SmartConnectNoSSL
from pyVmomi import vim
import vmclass
import vmclass_snap




config = configparser.ConfigParser()
config.read("config.ini")


connection = SmartConnectNoSSL(**config["VSphere"])

def get_all_vms_size():
    content = connection.content
    container = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
    return [vmclass.VirtualMachine(managed_object_ref) for managed_object_ref in container.view]

def get_all_vms_snap():
    content = connection.content
    container = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
    return [vmclass_snap.VirtualMachine(managed_object_ref) for managed_object_ref in container.view]

# # отсортировать все виртуальные машины по занимаемому месту
# for virtual_machine in sorted(get_all_vms_size(), key=lambda vm: vm.usage_storage, reverse=True):
#      print(virtual_machine)

# показать виртуальные машины имеющие снапшоты
for virtual_machine in sorted(get_all_vms_snap(), key=lambda vm: vm.snapshot_size, reverse=True):
   if virtual_machine.snapshot_count > 0:
       print(virtual_machine)