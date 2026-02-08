from tenants.models import Client

class ClientRepository():

    @staticmethod
    def create_client(data: dict):
        return Client.objects.create(**data)