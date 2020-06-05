from essentials_kit_management.interactors.storages import \
    FormStorageInterface
from essentials_kit_management.interactors.presenters import \
    FormPresenterInterface

from essentials_kit_management.interactors.storages.dtos import (
    GetUserOrderDto
)

from essentials_kit_management.constants.enums import FormStatusEnum


class GetUserOrderedDetailsInteractor:

    def __init__(self,
                 form_storage: FormStorageInterface,
                 form_presenter: FormPresenterInterface):

        self.form_storage = form_storage
        self.form_presenter = form_presenter

    def get_user_ordered_details(self, user_id: int, form_id: int):

        is_valid_form_id = self.form_storage.is_valid_form_id(form_id=form_id)
        invalid_form_id_given = not is_valid_form_id

        if invalid_form_id_given:
            self.form_presenter.raise_invalid_form_id_exception()
            return

        user_order_dtos = self.form_storage.get_order_dtos(user_id=user_id,
                                                           form_id=form_id)
        user_brand_dtos = self.form_storage.get_user_brand_dtos(
            user_order_dtos
        )
        user_item_dtos = self.form_storage.get_user_item_dtos(user_order_dtos)

        brand_dicts = self._convert_brand_to_dicts(brand_dtos=user_brand_dtos)
        item_dicts = self._convert_item_to_dicts(item_dtos=user_item_dtos)

        order_detail_dtos = self._get_user_order_detail_dtos(
            orders=user_order_dtos,
            brand_dicts=brand_dicts,
            item_dicts=item_dicts)

        response = self.form_presenter.get_user_ordered_details_response(
            order_detail_dtos)

        return response

    def _convert_brand_to_dicts(self, brand_dtos):
        dicts = {}

        for brand in brand_dtos:
            single_dict = {
                brand.brand_id: brand
            }
            dicts.update(single_dict)
        return dicts

    def _convert_item_to_dicts(self, item_dtos):
        dicts = {}

        for item in item_dtos:
            single_dict = {
                item.item_id: item
            }
            dicts.update(single_dict)
        return dicts

    def _get_user_order_detail_dtos(self, orders, brand_dicts, item_dicts):
        order_dtos_list = []

        for order in orders:
            cost_incurred, recieved_count = \
                self._get_incurred_cost_and_recieved_count(
                    order=order,
                    brand_dicts=brand_dicts)
            print(item_dicts[order.item_id])
            dto = GetUserOrderDto(item_id=order.item_id,
                                  item_name=item_dicts[order.item_id].name,
                                  items_added=order.count,
                                  items_recived=recieved_count,
                                  cost_incurred=cost_incurred,
                                  out_of_stock=order.out_of_stock)
            order_dtos_list.append(dto)
        return order_dtos_list

    def _get_incurred_cost_and_recieved_count(self,
                                              order,
                                              brand_dicts):
        price_per_item = brand_dicts[order.brand_id].price_per_item
        recieved_count = order.count - order.pending_count
        cost_incurred = recieved_count * price_per_item  # have dout
        # i have to start from here

        return cost_incurred, recieved_count
