import pytest

from essentials_kit_management.storages.order_storage_implementation \
    import OrderStorageImplementation

from essentials_kit_management.interactors.storages.dtos import (
    UpdateFormNewOrderDto, UpdateFormOrderDto
    )

from essentials_kit_management.models import Order

@pytest.mark.django_db
def test_update_orders_with_valid_details_create_orders(
        populate_data):

    # Arrange
    order_details1 = UpdateFormOrderDto(order_id=1,
                                        item_id=1,
                                        brand_id=4,
                                        ordered_count=100,
                                        out_of_stock=0)
    order_details2 = UpdateFormOrderDto(order_id=2,
                                        item_id=2,
                                        brand_id=1,
                                        ordered_count=1000,
                                        out_of_stock=0)

    update_order_list = [order_details1, order_details2]

    order_storage = OrderStorageImplementation()

    # Act
    order_storage.update_orders(update_order_list=update_order_list)

    # Assert
    upd_order1 = Order.objects.get(id=1)
    upd_order2 = Order.objects.get(id=2) 

    assert upd_order1.brand_id == order_details1.brand_id
    assert upd_order1.count == order_details1.ordered_count
    assert upd_order1.out_of_stock == order_details1.out_of_stock

    assert upd_order2.brand_id == order_details2.brand_id
    assert upd_order2.count == order_details2.ordered_count
    assert upd_order2.out_of_stock == order_details2.out_of_stock