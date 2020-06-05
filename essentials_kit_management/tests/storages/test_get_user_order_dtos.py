import datetime

import pytest

from essentials_kit_management.storages.form_storage_implementation import \
    FormStorageImplementation

from essentials_kit_management.interactors.storages.dtos import OrderDto



@pytest.mark.django_db
def test_get_user_order_dtos_with_valid_details_return_dtos(create_users,
                                                            create_brands,
                                                            create_items,
                                                            create_orders,
                                                            create_sections,
                                                            create_forms):

    # Arrange
    user_id = 1
    order1 = OrderDto(
        order_id=1,
        user_id=1,
        item_id=1,
        brand_id=1,
        form_id=1,
        section_id= 1,
        count=10,
        pending_count=5,
        out_of_stock=0)
    order2 = OrderDto(
        order_id=2,
        user_id=1,
        item_id=2,
        brand_id=2,
        form_id=2,
        section_id= 1,
        count=10,
        pending_count=5,
        out_of_stock=0)
    
    expected_list = [order1, order2]

    storage = FormStorageImplementation()

    # Act
    actual_list = storage.get_user_order_dtos(user_id=user_id)

    # Assert
    assert actual_list == expected_list
