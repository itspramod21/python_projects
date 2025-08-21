if __name__ == "__main__":
    from azure.common.credentials import ServicePrincipalCredentials
    from azure.mgmt.resource import ResourceManagementClient
    from azure.mgmt.compute import ComputeManagementClient
    from azure.mgmt.network import NetworkManagementClient
    from azure.mgmt.compute.models import DiskCreateOption
SUBSCRIPTION_ID = '9cd085a2-228d-4568-b496-bf4da6ed72d8'
GROUP_NAME = 'RG-w2016con1'
LOCATION = 'southeastasia'
VM_NAME = 'w2016con1'
def get_credentials():
    credentials = ServicePrincipalCredentials(
        client_id = '126ee1bb-512c-42a2-a00c-84e35c5d4963',
        secret = '+NuwBXSoZ5F+UdfxLYa+6d4WQJsV//Sbd/xo75WyfF0=',
        tenant = '823e1f7a-5d1c-4595-8db2-e303ce3ffb4f'
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
           