from abc import ABC, abstractmethod

from typing import Dict

from essentials_kit_management.interactors.storages.order_storage_interface \
    import OrderStorageInterface

from essentials_kit_management.models import Order


class OrderStorageImplementation(OrderStorageInterface):

    def create_new_orders(self,
                          user_id: int,
                          new_order_list: Dict):

        orders = Order.objects.bulk_create(
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

        order_ids = [order.order_id for order in update_order_list]
        orders_dict = self._convert_update_orders_dtos_to_dict(
            update_order_list=update_order_list)

        orders = Order.objects.filter(id__in=order_ids)

        for order in orders:
            update_order = orders_dict[order.id]

            order.brand_id = update_order.brand_id
            order.count = update_order.ordered_count
            order.out_of_stock = update_order.out_of_stock

        Order.objects.bulk_update(orders,
                                  ["brand_id", "count", "out_of_stock"])

    def _convert_update_orders_dtos_to_dict(self, update_order_list):
        dtos_dict = {}

        for order_dto in update_order_list:
            single_dict = {
                order_dto.order_id: order_dto
            }
            dtos_dict.update(single_dict)
        return dtos_dict

    def remove_orders(self, remove_order_list):
        order_ids = remove_order_list
        Order.objects.filter(id__in=order_ids).delete()

    def are_they_valid_order_ids(self, order_ids):
        order_ids = list(set(order_ids))
        count = len(order_ids)

        objs_count = Order.objects.filter(id__in=order_ids).count()

        are_all_valid_order_ids = objs_count == count
        return are_all_valid_order_ids
