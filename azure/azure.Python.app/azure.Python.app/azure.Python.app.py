if __name__ == "__main__":
    from azure.common.credentials import ServicePrincipalCredentials
    from azure.mgmt.resource import ResourceManagementClient
    from azure.mgmt.compute import ComputeManagementClient
    from azure.mgmt.network import NetworkManagementClient
    from azure.mgmt.compute.models import DiskCreateOption

GROUP_NAME = 'RG-w2016con1'
LOCATION = 'southeastasia'
VM_NAME = 'w2016con1'
def get_credentials():
    
) 
    return credentials
credentials = get_credentials()
if resource_group_client = ResourceManagementClient(
    credentials,
    subscription_id
)
network_client = NetworkManagementClient(
    credentials,
    SUBSCRIPTION_ID
)
compute_client = ComputeManagementClient(
    credentials,
    SUBSCRIPTION_ID
)
           
