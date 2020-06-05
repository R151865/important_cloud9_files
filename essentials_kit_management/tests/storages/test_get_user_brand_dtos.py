import datetime

import pytest

from essentials_kit_management.storages.form_storage_implementation import \
    FormStorageImplementation

from essentials_kit_management.interactors.storages.dtos import  (
    BrandDto, OrderDto)


@pytest.mark.django_db
def test_get_user_brand_dtos_wit_valid_detailsreturn_dtos(create_users,
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

    brand1 = BrandDto(brand_id=1,
                     name="brand1",
                     min_quantity=1,
                     max_quantity=5,
                     price_per_item=100)
    brand2= BrandDto(brand_id=2,
                     name="brand2",
                     min_quantity=2,
                     max_quantity=8,
                     price_per_item=200)
    
    order_dtos = [order1, order2]
    
    expected_list = [brand1, brand2]

    storage = FormStorageImplementation()

    # Act
    actual_list = storage.get_user_brand_dtos(order_dtos)

    # Assert
    assert actual_list == expected_list
