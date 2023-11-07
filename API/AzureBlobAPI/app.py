
from azure.storage.blob import BlobServiceClient, generate_container_sas, ContainerSasPermissions, ResourceTypes
import datetime

# Azure Blob Storage connection string and container name
connection_string = ""
access_key = ''
container_name = "container_name"
blob_name = "file_name"

# Create a BlobServiceClient
# Create a BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Get the container client
container_client = blob_service_client.get_container_client(container_name)

# Check if the blob exists
if container_client.get_blob_client(blob_name).exists():
    # Define the permissions and expiration time for the SAS token
    sas_container_permissions = ContainerSasPermissions(read=True)  # Adjust permissions as needed
    sas_resource_types = ResourceTypes(object=True)

    sas_token = generate_container_sas(
        container_name=container_name,
        account_name=blob_service_client.account_name,
        account_key= access_key,  # Not needed when generating a SAS token
        permission=sas_container_permissions,
        expiry=datetime.datetime.utcnow() + datetime.timedelta(hours=1),  # Specify the expiration time for the SAS token
        resource_types=sas_resource_types
    )

    # Construct the URL with the SAS token
    sas_url = f"https://{container_client.account_name}.blob.core.windows.net/{container_name}/{blob_name}?{sas_token}"

    print(f"SAS URL for {blob_name}: {sas_url}")
else:
    print(f"Blob {blob_name} does not exist in container {container_name}")