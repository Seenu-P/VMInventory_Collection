import requests
import urllib3
import csv
from vmware.vapi.vsphere.client import create_vsphere_client

session = requests.session()

# Disable cert verification for demo purpose.
# This is not recommended in a production environment.
session.verify = False

# Disable the secure connection warning for demo purpose.
# This is not recommended in a production environment.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# f=open("PATH\\credentials.txt","r")
# lines=f.readlines()
# user=lines[0]
# print(type(user))
# pwd=lines[1]
# print(type(pwd))
# f.close()

# Connect to a vCenter Server using username and password
vsphere_client = create_vsphere_client(server='VC FQDN', username='USERNAME', password='PASSWORD')

# List all VMs inside the vCenter Server

# Get a list of VMs
vm_list = vsphere_client.vcenter.VM.list()
print("printing first set of VM list: ", vm_list)
vm_details = []
vm_IDs = []
# Write the VM list to a CSV file
for vm in vm_list:
    name = vm.vm
    vm_IDs.append(name)
print("printing first set of VM IDs: ", vm_IDs)
for vms in vm_IDs:
    vm_properties = vsphere_client.vcenter.VM.get(vms)
    print("printing VM properties: ", vm_properties)

    # Retrieve the full set of properties for the VM

    # Extract the relevant properties from the VM object
    # vm_id = vm_properties.vm
    name = vm_properties.name
    power_state = vm_properties.power_state
    memory = vm_properties.memory
    cpu = vm_properties.cpu
    guest_os = vm_properties.guest_os
    disks = vm_properties.disks
    # disk_usage = sum(disk.capacity for disk in disks)

    # Append the VM details to the list
    vm_details.append({
        # 'vm_id': vm_IDs,
        'name': name,
        'power_state': power_state,
        'memory': memory,
        'cpu': cpu,
        'guest_os': guest_os,
        # 'disk_usage': disk_usage
    })

print("printing VM details now : ", vm_details)

with open('PATH\\Python3.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Power State', 'Memory', 'CPU', 'Guest OS'])
    for vms in vm_details:
        name = vms.get("name")
        power_state = vms.get("power_state")
        memory = vms.get("memory")
        cpu = vms.get("cpu")
        guest_os = vms.get("guest_os")
        print(f'{name}: {power_state}, {memory} MB, {cpu} vCPU, {guest_os}')
        writer.writerow([name, power_state, memory, cpu, guest_os])



