import pytest

from essentials_kit_management.storages.order_storage_implementation \
    import OrderStorageImplementation

from essentials_kit_management.interactors.storages.dtos import (
    UpdateFormNewOrderDto, UpdateFormOrderDto
    )

from essentials_kit_management.models import Order

@pytest.mark.django_db
def test_are_they_valid_order_ids_with_invalid_order_ids_return_false(
        populate_data):

    # Arrange
    invalid_order_ids = [1, 2, -1]
    order_storage = OrderStorageImplementation()

    # Act
    are_they_valid_order_ids = order_storage.are_they_valid_order_ids(
        order_ids=invalid_order_ids)

    # Assert
    assert are_they_valid_order_ids is False


@pytest.mark.django_db
def test_are_they_valid_order_ids_with_valid_order_ids_return_true(
        populate_data):

    # Arrange
    order_ids = [1, 2, 3]
    order_storage = OrderStorageImplementation()

    # Act
    are_they_valid_order_ids = order_storage.are_they_valid_order_ids(
        order_ids=order_ids)

    # Assert
    assert are_they_valid_order_ids is True