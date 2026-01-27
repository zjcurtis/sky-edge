from datetime import datetime
from itertools import combinations

from requests import Response

from sky_edge.api.constituent import (
    Address,
    address_list_constituent_get,
)


def _addresses_have_same_location(addr1: Address, addr2: Address) -> bool:
    """Check if two addresses represent the same physical location."""
    return (
        addr1.address_lines == addr2.address_lines
        and addr1.city == addr2.city
        and addr1.state == addr2.state
        and addr1.postal_code == addr2.postal_code
        and addr1.country == addr2.country
        and addr1.county == addr2.county
        and addr1.suburb == addr2.suburb
        and addr1.region == addr2.region
        and addr1.type == addr2.type
    )


def _date_ranges_overlap(
    start1: datetime | None,
    end1: datetime | None,
    start2: datetime | None,
    end2: datetime | None,
) -> bool:
    """
    Check if two date ranges overlap.

    A None start is treated as infinitely in the past.
    A None end is treated as infinitely in the future (ongoing).
    """
    # For overlap: start1 <= end2 AND start2 <= end1
    # With None handling:
    # - If start is None, it's always <= any end
    # - If end is None, any start is always <= it

    start1_before_end2 = start1 is None or end2 is None or start1 <= end2
    start2_before_end1 = start2 is None or end1 is None or start2 <= end1

    return start1_before_end2 and start2_before_end1


def get_overlapping_addresses(
    constituent_id: str, include_inactive: bool = True
) -> list[tuple[Address, Address]] | Response:
    """
    Get addresses for a constituent that have overlapping dates with the same
    address information.

    Args:
        constituent_id: The ID of the constituent to get addresses for.
        include_inactive: Whether to include inactive addresses. Defaults to True
            since we want to find all potential overlaps.

    Returns:
        A list of pairs of addresses that share the same location information
        and have overlapping date ranges. Returns a Response object if the API
        call fails.
    """
    result = address_list_constituent_get(
        constituent_id=constituent_id, include_inactive=include_inactive
    )

    if isinstance(result, Response):
        return result

    addresses = result.value

    if len(addresses) < 2:
        return []

    overlapping_pairs: list[tuple[Address, Address]] = []

    for addr1, addr2 in combinations(addresses, 2):
        if _addresses_have_same_location(addr1, addr2) and _date_ranges_overlap(
            addr1.start, addr1.end, addr2.start, addr2.end
        ):
            overlapping_pairs.append((addr1, addr2))

    return overlapping_pairs
