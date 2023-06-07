from pocketbase import PocketBase  # Client also works the same
from pocketbase.client import FileUpload

client = PocketBase('http://localhost:8090')

# authenticate as regular user
user_data = client.collection("users").auth_with_password("joe", "joejoejoe")

def update_inventory(pb_client):
    inventory = client.collection("inventory").get_all()
    for item in inventory:
        







