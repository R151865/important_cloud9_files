import pytest

from essentials_kit_management.storages.order_storage_implementation \
    import OrderStorageImplementation

from essentials_kit_management.interactors.storages.dtos import (
    UpdateFormNewOrderDto, UpdateFormOrderDto
    )

from essentials_kit_management.models import Order

@pytest.mark.django_db
def test_create_orders_with_valid_details_create_orders(
        populate_data):

    # Arrange
    user_id = 1
    new_order_dto1 = UpdateFormNewOrderDto(
        form_id=1,
        section_id=2,
        order_details=UpdateFormOrderDto(order_id=0,
                                         item_id=1,
                                         brand_id=4,
                                         ordered_count=1,
                                         out_of_stock=0)
    )
    new_order_dto2 = UpdateFormNewOrderDto(
        form_id=1,
        section_id=3,
        order_details=UpdateFormOrderDto(order_id=0,
                                         item_id=2,
                                         brand_id=3,
                                         ordered_count=6,
                                         out_of_stock=0)
    )
    new_order_list = [new_order_dto1, new_order_dto2]

    order_storage = OrderStorageImplementation()

    # Act
    order_storage.create_new_orders(user_id=user_id,
                                    new_order_list=new_order_list)

    # Assert
    is_order1_created = Order.objects.filter(item_id=1,
                                             brand_id=4,
                                             count=1,
                                             out_of_stock=0).exists()
    is_order2_created = Order.objects.filter(item_id=2,
                                             brand_id=3,
                                             count=6,
                                             out_of_stock=0).exists()
    
    assert is_order1_created is True
    assert is_order2_created is True