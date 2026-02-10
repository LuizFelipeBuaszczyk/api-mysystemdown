from tenants.models import Client

from utils.logger import get_logger

logger = get_logger(__name__)

class ClientRepository():

    @staticmethod
    def create_client(data: dict):
        logger.debug(f"Starting repository create_client - name: {data['name']}")
        return Client.objects.create(**data)