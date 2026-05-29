"""Dataclasses for integration metadata in order requests."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class OrderSponsor:
    """Sponsoring marketplace owner associated with an order.

    Attributes:
        id: MercadoPago user ID of the sponsoring marketplace owner. Type: str.
    """

    id: Optional[str] = None


@dataclass
class OrderIntegrationData:
    """Integration metadata for an order request.

    Identifies the integrator, platform, and corporation associated with the
    integration. Use this dataclass to build the ``integration_data`` payload
    at the root of the order create request. Convert to dict with
    ``dataclasses.asdict()``.

    Attributes:
        integrator_id: Identifier of the certified integrator. Type: str.
        platform_id: Platform identifier assigned by MercadoPago. Type: str.
        corporation_id: Corporation identifier for multi-account setups. Type: str.
        sponsor: Sponsoring marketplace owner information.
    """

    integrator_id: Optional[str] = None
    platform_id: Optional[str] = None
    corporation_id: Optional[str] = None
    sponsor: Optional[OrderSponsor] = None
