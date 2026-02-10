from tenants.models import Domain

from utils.logger import get_logger

logger = get_logger(__name__)

class DomainRepository():

    @staticmethod
    def create_domain(data: dict):
        logger.debug(f"Starting repository create_domain - domain: {data['domain']}")
        return Domain.objects.create(**data)