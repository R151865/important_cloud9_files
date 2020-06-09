from essentials_kit_management.interactors.storages import \
    FormStorageInterface
from essentials_kit_management.interactors.presenters import \
    FormPresenterInterface

from essentials_kit_management.interactors.storages.dtos import (
    FormCompleteDetailsDto, HomePageFormDto
)

from essentials_kit_management.constants.enums import FormStatusEnum


class GetFormsInteractor:

    def __init__(self,
                 form_storage: FormStorageInterface,
                 form_presenter: FormPresenterInterface):

        self.form_storage = form_storage
        self.form_presenter = form_presenter

    def get_forms(self, user_id: int, offset=0, limit=30):

        are_they_valid_offset_and_limit = \
            self.form_storage.are_they_valid_offset_and_limit(
                offset=offset, limit=limit)
        invalid_offset_and_limit_given = not are_they_valid_offset_and_limit

        if invalid_offset_and_limit_given:
            self.form_presenter.raise_invalid_offset_and_limit_exception()
            return

        forms_dtos, total_forms_count = self.form_storage.get_forms_dtos(
            offset=offset, limit=limit)

        user_order_dtos = self.form_storage.get_user_order_dtos(user_id)

        user_brand_dtos = self.form_storage.get_user_brand_dtos(
            user_order_dtos
        )
        user_item_dtos = self.form_storage.get_user_item_dtos(user_order_dtos)

        form_complete_details_dtos = \
            self.arrange_details_and_return_form_complete_details_dtos(
                forms=forms_dtos,
                orders=user_order_dtos,
                brands=user_brand_dtos,
                items=user_item_dtos)

        form_details_dtos = self.get_forms_details_dto_list(
            form_complete_details_dtos)

        response = self.form_presenter.get_forms_response(
            form_dtos=form_details_dtos, total_forms_count=total_forms_count)

        return response

    def arrange_details_and_return_form_complete_details_dtos(
            self, forms, orders, brands, items):

        form_complete_details_dtos = []

        for form in forms:
            form_id = form.form_id,
            order_dtos = self._get_form_orders(form_id=form.form_id,
                                               orders=orders)
            brand_dtos = self._get_order_brands(orders=order_dtos,
                                                brands=brands)
            item_dtos = self._get_order_items(orders=order_dtos, items=items)

            dto = FormCompleteDetailsDto(form_dto=form,
                                         brand_dtos=brand_dtos,
                                         order_dtos=order_dtos,
                                         item_dtos=item_dtos)
            form_complete_details_dtos.append(dto)
        return form_complete_details_dtos

    def _get_form_orders(self, form_id, orders):
        form_orders_list = []

        for order in orders:
            is_form_order = order.form_id == form_id
            if is_form_order:
                form_orders_list.append(order)
        return form_orders_list

    def _get_order_brands(self, orders, brands):
        order_brand_list = []

        for order in orders:
            for brand in brands:
                is_order_brand = brand.brand_id == order.brand_id
                if is_order_brand:
                    order_brand_list.append(brand)
        return order_brand_list

    def _get_order_items(self, orders, items):
        items_list = []

        for order in orders:
            for item in items:
                is_item_belongs_to_order = order.item_id == item.item_id
                if is_item_belongs_to_order:
                    items_list.append(item)
        return items_list

    def get_forms_details_dto_list(self, forms_dtos):
        form_dtos_list = []

        for form in forms_dtos:
            form_dto = self._get_form_details(form)
            form_dtos_list.append(form_dto)

        return form_dtos_list

    def _get_form_details(self, form_obj):

        form = form_obj.form_dto
        orders = form_obj.order_dtos
        brands = form_obj.brand_dtos
        items = form_obj.item_dtos

        brand_dicts = self._get_brands_dicts(brands)

        total_items_count = self._get_total_ordered_items_count(orders=orders)
        estimated_cost = self._get_estimated_cost(orders=orders,
                                                  brand_dicts=brand_dicts)

        pending_items_count = self._get_pending_items(orders)
        incurred_cost = self._get_incurred_cost(orders=orders,
                                                brand_dicts=brand_dicts)

        form_status = \
            self.is_form_is_closed_with_no_pending_item_update_form_status(
                form.status, pending_items_count)

        home_page_form_dto = HomePageFormDto(
             form_id=form.form_id,
             name=form.name,
             status=form_status,
             close_date=form.close_date,
             expected_delivery_date=form.expected_delivery_date,
             items_count=total_items_count,
             estimated_cost=estimated_cost,
             items_pending_count=pending_items_count,
             cost_incurred_for_delivery=incurred_cost
        )

        return home_page_form_dto

    def is_form_is_closed_with_no_pending_item_update_form_status(
            self, form_status,
            pending_items_count):
        if_form_closed = form_status == FormStatusEnum.CLOSED.value
        no_pending_items = pending_items_count == 0

        if if_form_closed and no_pending_items:
            form_status = FormStatusEnum.DONE.value

        return form_status

    def _get_total_ordered_items_count(self, orders):
        count = 0

        for order in orders:
            count = count + order.count

        return count

    def _get_estimated_cost(self, orders, brand_dicts):
        cost = 0

        for order in orders:
            brand = brand_dicts[order.brand_id]
            price_per_item = brand.price_per_item
            cost = cost + order.count*price_per_item
        return cost

    def _get_incurred_cost(self, orders, brand_dicts):
        cost = 0

        for order in orders:
            price_per_item = brand_dicts[order.brand_id].price_per_item

            cost = cost + (order.count-order.pending_count)*price_per_item
        return cost

    def _get_pending_items(self, orders):
        count = 0

        for order in orders:
            count = count + order.pending_count
        return count

    def _get_brands_dicts(self, brands):
        brand_dicts = {}

        for brand in brands:
            single_dict = {brand.brand_id: brand}
            brand_dicts.update(single_dict)
        return brand_dicts
