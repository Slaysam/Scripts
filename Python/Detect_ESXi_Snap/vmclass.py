class VirtualMachine:
    def __init__(self, machine_object):
        self.vm = machine_object

    @property
    def name(self):
        return self.vm.name

    @property
    def provisioned_space(self):
        return int(self.vm.summary.storage.committed + self.vm.summary.storage.uncommitted) / 1024**3

    @property
    def guest_disk_usage(self):
        return sum([int(i.capacity - i.freeSpace) for i in self.vm.summary.vm.guest.disk]) / 1024**3

    @property
    def usage_storage(self):
        return int(self.vm.summary.storage.committed) / 1024**3

    def __repr__(self):
        return "{}  {:.2f}  {:.2f}  {:.2f}".format(self.name, self.provisioned_space,
                                                   self.guest_disk_usage, self.usage_storage)