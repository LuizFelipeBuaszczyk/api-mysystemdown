from tenants.models import Domain

class DomainRepository():

    @staticmethod
    def create_domain(data: dict):
        return Domain.objects.create(**data)