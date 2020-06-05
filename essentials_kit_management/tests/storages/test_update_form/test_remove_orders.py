import pytest

from essentials_kit_management.storages.order_storage_implementation \
    import OrderStorageImplementation

from essentials_kit_management.interactors.storages.dtos import (
    UpdateFormNewOrderDto, UpdateFormOrderDto
    )

from essentials_kit_management.models import Order

@pytest.mark.django_db
def test_remove_orders_with_valid_details_create_orders(
        populate_data):

    # Arrange
    remove_order_list = [1, 2]
    order_storage = OrderStorageImplementation()

    # Act
    order_storage.remove_orders(remove_order_list=remove_order_list)

    # Assert
    is_order1_exists = Order.objects.filter(id=1).exists()
    is_order2_exists = Order.objects.filter(id=2).exists()

    assert is_order1_exists is False
    assert is_order2_exists is False