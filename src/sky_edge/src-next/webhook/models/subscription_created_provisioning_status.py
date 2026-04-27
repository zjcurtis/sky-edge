from enum import Enum


class SubscriptionCreatedProvisioningStatus(str, Enum):
    ERROR = "Error"
    PENDING = "Pending"
    PROVISIONED = "Provisioned"
    PROVISIONING = "Provisioning"

    def __str__(self) -> str:
        return str(self.value)
