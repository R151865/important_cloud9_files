from abc import ABC, abstractmethod
from typing import Dict

from essentials_kit_management.interactors.storages.order_storage_interface \
    import OrderStorageInterface

from essentials_kit_management.models import Order


class OrderStorageImplementation(OrderStorageInterface):

    def create_new_orders(self,
                          user_id: int,
                          new_order_list: Dict):

        Order.objects.bulk_create(
            [
                Order(user_id=user_id,
                      form_id=order.form_id,
                      section_id=order.section_id,
                      brand_id=order.order_details.brand_id,
                      item_id=order.order_details.item_id,
                      count=order.order_details.ordered_count,
                      pending_count=0,
                      out_of_stock=order.order_details.out_of_stock)
                for order in new_order_list
            ]
        )


    def update_orders(self, update_order_list):
        #TODO: need bulk_update for optimization
        for order in update_order_list:
            Order.objects.filter(id=order.order_id).update(
                brand_id=order.brand_id,
                count=order.ordered_count,
                out_of_stock=order.out_of_stock)


    def remove_orders(self, remove_order_list):
        order_ids = remove_order_list
        Order.objects.filter(id__in=order_ids).delete()


    def are_they_valid_order_ids(self, order_ids):
        order_ids = list(set(order_ids))
        count = len(order_ids)

        objs_count = Order.objects.filter(id__in=order_ids).count()

        are_all_valid_order_ids = objs_count == count
        return are_all_valid_order_ids
