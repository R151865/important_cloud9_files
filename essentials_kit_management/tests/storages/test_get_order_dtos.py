import datetime

import pytest

from essentials_kit_management.storages.form_storage_implementation import \
    FormStorageImplementation

from essentials_kit_management.interactors.storages.dtos import OrderDto



@pytest.mark.django_db
def test_get_order_dtos_with_valid_details_return_dtos(create_users,
                                                       create_brands,
                                                       create_items,
                                                       create_orders,
                                                       create_sections,
                                                       create_forms):

    # Arrange
    user_id = 1
    form_id = 1

    expected_order_dtos = [
        OrderDto(
            order_id=1,
            user_id=1,
            item_id=1,
            brand_id=1,
            form_id=1,
            section_id= 1,
            count=10,
            pending_count=5,
            out_of_stock=0)
        ]

    storage = FormStorageImplementation()

    # Act
    actual_order_dtos = storage.get_order_dtos(user_id=user_id,
                                         form_id=form_id)

    # Assert
    assert actual_order_dtos == expected_order_dtos
