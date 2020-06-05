from essentials_kit_management.interactors.storages. \
    form_storage_interface import FormStorageInterface
from essentials_kit_management.interactors.presenters. \
    form_presenter_interface import FormPresenterInterface
from essentials_kit_management.interactors.storages. \
    section_storage_interface import SectionStorageInterface
from essentials_kit_management.interactors.presenters. \
    section_presenter_interface import SectionPresenterInterface

from essentials_kit_management.interactors.storages. \
    item_storage_interface import ItemStorageInterface
from essentials_kit_management.interactors.presenters. \
    item_presenter_interface import ItemPresenterInterface
from essentials_kit_management.interactors.storages. \
    brand_storage_interface import BrandStorageInterface
from essentials_kit_management.interactors.presenters. \
    brand_presenter_interface import BrandPresenterInterface

from essentials_kit_management.interactors.storages. \
    order_storage_interface import OrderStorageInterface
from essentials_kit_management.interactors.presenters. \
    order_presenter_interface import OrderPresenterInterface

from essentials_kit_management.interactors.storages.dtos import (
    UpdateFormOrderDto, UpdateFormNewOrderDto
    )


class UpdateFormInteractor:

    def __init__(self,
                 order_storage: OrderStorageInterface,
                 order_presenter: OrderPresenterInterface,
                 form_storage: FormStorageInterface,
                 form_presenter: FormPresenterInterface,
                 section_storage: SectionStorageInterface,
                 section_presenter: SectionPresenterInterface,
                 item_storage: ItemStorageInterface,
                 item_presenter: ItemPresenterInterface,
                 brand_storage: BrandStorageInterface,
                 brand_presenter: BrandPresenterInterface):

        self.order_storage = order_storage
        self.order_presenter = order_presenter
        self.form_storage = form_storage
        self.form_presenter = form_presenter
        self.section_storage = section_storage
        self.section_presenter = section_presenter
        self.item_storage = item_storage
        self.item_presenter = item_presenter
        self.brand_storage = brand_storage
        self.brand_presenter = brand_presenter

    def update_form(self, user_id: int, orders_details):
        form_id = orders_details["form_id"]
        is_valid_form_id = self.form_storage.is_valid_form_id(form_id=form_id)
        invalid_form_id_given = not is_valid_form_id

        if invalid_form_id_given:
            self.form_presenter.raise_invalid_form_id_exception()
            return

        sections = orders_details["sections"]
        (new_orders_list,
         update_order_list,
         remove_order_list) = self._get_order_details(form_id=form_id,
                                                      sections=sections)

        (section_ids,
         order_ids,
         item_ids,
         brand_ids) = self._get_section_order_and_brand_ids_lis(
            new_orders_list=new_orders_list,
            update_order_list=update_order_list,
            remove_order_list=remove_order_list)

        are_they_valid_section_ids = \
            self.section_storage.are_they_valid_section_ids(
                section_ids=section_ids)
        in_valid_section_ids_given = not are_they_valid_section_ids

        if in_valid_section_ids_given:
            self.section_presenter.raise_invalid_section_id_exception()
            return

        are_they_valid_item_ids = \
            self.item_storage.are_they_valid_item_ids(
                item_ids=item_ids)
        in_valid_item_ids_given = not are_they_valid_item_ids

        if in_valid_item_ids_given:
            self.item_presenter.raise_invalid_item_id_exception()
            return

        are_they_valid_order_ids = \
            self.order_storage.are_they_valid_order_ids(
                order_ids=order_ids)
        in_valid_order_ids_given = not are_they_valid_order_ids

        if in_valid_order_ids_given:
            self.order_presenter.raise_invalid_order_id_exception()
            return

        are_they_valid_brand_ids = \
            self.brand_storage.are_they_valid_brand_ids(
                brand_ids=brand_ids)
        in_valid_brand_ids_given = not are_they_valid_brand_ids

        if in_valid_brand_ids_given:
            self.brand_presenter.raise_invalid_brand_id_exception()
            return

        self.order_storage.create_new_orders(user_id, new_orders_list)
        self.order_storage.update_orders(update_order_list)
        self.order_storage.remove_orders(remove_order_list)
        return

    def _get_section_order_and_brand_ids_lis(self,
                                             new_orders_list,
                                             update_order_list,
                                             remove_order_list):
        section_ids_list = []
        order_ids_list = []
        item_ids_list = []
        brand_ids_list = []

        for order_dtos in new_orders_list:
            section_ids_list.append(order_dtos.section_id)
            order = order_dtos.order_details
            item_ids_list.append(order.item_id)
            brand_ids_list.append(order.brand_id)

        for order in update_order_list:
            item_ids_list.append(order.item_id)
            brand_ids_list.append(order.brand_id)
            order_ids_list.append(order.order_id)

        order_ids_list += remove_order_list

        return (section_ids_list,
                order_ids_list,
                item_ids_list,
                brand_ids_list)

    def _get_order_details(self, form_id, sections):
        new_orders_list = []
        update_orders_list = []
        remove_order_list = []

        for section in sections:
                section_id = section["section_id"]
                order_details = section["order_details"]

                (new_orders,
                 update_orders,
                 remove_orders) = self._seperate_orders(
                     form_id=form_id,
                     section_id=section_id,
                     order_details=order_details)

                new_orders_list += new_orders
                update_orders_list += update_orders
                remove_order_list += remove_orders

        return new_orders_list, update_orders_list, remove_order_list

    def _seperate_orders(self, form_id, section_id, order_details):

        new_orders = self._seperate_new_orders(form_id=form_id,
                                               section_id=section_id,
                                               order_details=order_details)
        update_orders = self._seperate_update_orders(
            order_details=order_details
        )
        remove_orders = self._seperate_remove_orders(
            order_details=order_details)

        return new_orders, update_orders, remove_orders

    def _seperate_new_orders(self, form_id, section_id, order_details):
        orders_list = []

        for order in order_details:
            is_new_order = order["order_id"] == 0 and order["brand_id"] != 0
            if is_new_order:
                order_details_dto = \
                    self._convert_update_form_order_dict_to_obj(order=order)
                dto = UpdateFormNewOrderDto(form_id=form_id,
                                            section_id=section_id,
                                            order_details=order_details_dto)
                orders_list.append(dto)

        return orders_list

    def _seperate_update_orders(self, order_details):
        update_order_list = []

        for order in order_details:
            is_upated_order = (order["order_id"] != 0 and
                               order["brand_id"] != 0 and
                               order["ordered_count"])
            if is_upated_order:
                dto = self._convert_update_form_order_dict_to_obj(order=order)
                update_order_list.append(dto)

        return update_order_list

    def _convert_update_form_order_dict_to_obj(self, order):
        return UpdateFormOrderDto(item_id=order["item_id"],
                                  order_id=order["order_id"],
                                  brand_id=order["brand_id"],
                                  ordered_count=order["ordered_count"],
                                  out_of_stock=order["out_of_stock"])

    def _seperate_remove_orders(self, order_details):
        remove_order_list = []

        for order in order_details:
            is_remove_order = (order["order_id"] != 0 and
                               order["brand_id"] == 0)
            if is_remove_order:
                remove_order_list.append(order["order_id"])
        return remove_order_list
