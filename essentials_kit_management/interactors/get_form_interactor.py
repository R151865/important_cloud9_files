from essentials_kit_management.interactors.storages import \
    FormStorageInterface
from essentials_kit_management.interactors.presenters import \
    FormPresenterInterface

from essentials_kit_management.interactors.storages.dtos import (
    GetFormItemDto, GetFormSectionDto, GetFormDto, BrandDto,
    GetFormItemOrderDto
)


class GetFormInteractor:

    def __init__(self,
                 form_storage: FormStorageInterface,
                 form_presenter: FormPresenterInterface):

        self.form_storage = form_storage
        self.form_presenter = form_presenter

    def get_form(self,
                 form_id: int,
                 user_id: int):

        is_valid_form_id = self.form_storage.is_valid_form_id(form_id=form_id)
        invalid_form_id_given = not is_valid_form_id

        if invalid_form_id_given:
            self.form_presenter.raise_invalid_form_id_exception()
            return

        form_dto = self.form_storage.get_form_dto(form_id=form_id)
        order_dtos = self.form_storage.get_order_dtos(user_id=user_id,
                                                      form_id=form_id)
        section_dtos = self.form_storage.get_form_sections_dtos(
            form_id=form_id
        )
        item_dtos = self.form_storage.get_item_dtos(section_dtos)
        brand_dtos = self.form_storage.get_brand_dtos(item_dtos)

        get_form_details_dto = self._get_form_details_dto(
            form_dto=form_dto,
            order_dtos=order_dtos,
            section_dtos=section_dtos,
            item_dtos=item_dtos,
            brand_dtos=brand_dtos)

        response = self.form_presenter.get_form_response(
            get_form_details_dto=get_form_details_dto)
        return response

    def _get_form_details_dto(self,
                              form_dto,
                              order_dtos,
                              section_dtos,
                              item_dtos,
                              brand_dtos):

        brand_dicts = self._convert_brand_dtos_to_dicts(brand_dtos)
        section_details_dtos = self._get_section_details_dtos(
            section_dtos=section_dtos,
            order_dtos=order_dtos,
            item_dtos=item_dtos,
            brand_dicts=brand_dicts)

        form_details_dto = GetFormDto(form_id=form_dto.form_id,
                                      name=form_dto.name,
                                      close_date=form_dto.close_date,
                                      sections=section_details_dtos)

        return form_details_dto

    def _get_section_details_dtos(self,
                                  section_dtos,
                                  order_dtos,
                                  item_dtos,
                                  brand_dicts):
        section_details_dto_list = []

        for section in section_dtos:
            section_id = section.section_id
            items_details_dtos = self._get_items_details_dtos(
                section_id=section_id,
                order_dtos=order_dtos,
                item_dtos=item_dtos,
                brand_dicts=brand_dicts)

            dto = GetFormSectionDto(section_id=section.section_id,
                                    name=section.name,
                                    description=section.description,
                                    items=items_details_dtos)
            section_details_dto_list.append(dto)
        return section_details_dto_list

    def _get_items_details_dtos(self,
                                section_id,
                                order_dtos,
                                item_dtos,
                                brand_dicts):
        item_dtos_list = []

        section_items = self._get_section_items(
            section_id=section_id,
            item_dtos=item_dtos)

        for item in section_items:
            item_id = item.item_id
            item_brands = self._get_item_brands_dtos(item_id=item_id,
                                                     brand_dicts=brand_dicts)
            order_dto = self._get_item_order_dto(item_id=item_id,
                                                 order_dtos=order_dtos)

            dto = GetFormItemDto(item_id=item.item_id,
                                 name=item.name,
                                 description=item.description,
                                 brands=item_brands,
                                 order=order_dto)
            item_dtos_list.append(dto)

        return item_dtos_list

    def _get_item_order_dto(self, item_id, order_dtos):
        order_dto = self._is_item_has_order_if_exists_return_order_obj(
            item_id=item_id,
            order_dtos=order_dtos)

        if order_dto:
            # i have user print statement here
            print("ordered count ", order_dto.count)
            return GetFormItemOrderDto(order_id=order_dto.order_id,
                                       brand_id=order_dto.brand_id,
                                       ordered_count=order_dto.count,
                                       out_of_stock=order_dto.out_of_stock)
        else:
            return GetFormItemOrderDto(order_id=0,
                                       brand_id=0,
                                       ordered_count=0,
                                       out_of_stock=0)

    def _is_item_has_order_if_exists_return_order_obj(self,
                                                      item_id,
                                                      order_dtos):
        for order in order_dtos:
            is_item_has_order = item_id == order.item_id
            if is_item_has_order:
                return order
        return False

    def _get_item_brands_dtos(self, item_id, brand_dicts):
        brand_dtos_list = []

        for brand in brand_dicts.values():
            is_brand_belongs_this_item = item_id == brand.item_id
            if is_brand_belongs_this_item:
                brand_dtos_list.append(brand)
        return brand_dtos_list

    def _get_section_items(self, section_id, item_dtos):
        items_list = []

        for item in item_dtos:
            is_this_item_belongs_to_section = section_id == item.section_id
            if is_this_item_belongs_to_section:
                items_list.append(item)
        return items_list

    def _convert_brand_dtos_to_dicts(self, brand_dtos):
        brand_dicts = {}

        for brand in brand_dtos:
            single_dict = {
                brand.brand_id: brand
            }
            brand_dicts.update(single_dict)
        return brand_dicts
