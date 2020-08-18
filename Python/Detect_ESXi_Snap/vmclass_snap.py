import re

class VirtualMachine:
    def __init__(self, machine_object):
        self.vm = machine_object
        self.snapshot_count, self.snapshot_size = self._snapshot_info()

    @property
    def name(self):
        return self.vm.name

    def _snapshot_info(self):
        disk_list = self.vm.layoutEx.file
        size = 0
        count = 0
        for disk in disk_list:
            if disk.type == 'snapshotData':
                size += disk.size
                count += 1
            ss_disk = re.search('0000\d\d', disk.name)
            if ss_disk:
                size += disk.size
        return count, size / 1024**3

    def __repr__(self):
        return "Name: {}; Snapshot size: {:.2f} Gb; Snapshot count: {}".format(self.name, self.snapshot_size, self.snapshot_count)