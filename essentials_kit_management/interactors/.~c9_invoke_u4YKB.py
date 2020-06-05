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
                 form_storage:FormStorageInterface,
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
            form_id=form_id)
        item_dtos = self.form_storage.get_item_dtos(order_dtos)# -done no need of order here 
        brand_dtos = self.form_storage.get_brand_dtos(item_dtos)

        get_form_details_dto = self.get_form_details_dto(
            form_dto=form_dto,
            order_dtos=order_dtos,
            section_dtos=section_dtos,
            item_dtos=item_dtos,
            brand_dtos=brand_dtos)

        response = self.form_presenter.get_form_response(
            get_form_details_dto=get_form_details_dto
        )

        return response

    def get_form_details_dto(self,
                             form_dto,
                             order_dtos,
                             section_dtos,
                             item_dtos,
                             brand_dtos):

        section_details_dtos = self._get_section_details_dtos(
            section_dtos=section_dtos,
            order_dtos=order_dtos,
            item_dtos=item_dtos,
            brand_dtos=brand_dtos)

        get_form_dto = GetFormDto(form_id=form_dto.form_id,
                                  name=form_dto.name,
                                  close_date=form_dto.close_date,
                                  sections=section_details_dtos)
        return get_form_dto


    def _get_section_details_dtos(self,
                                  section_dtos,
                                  order_dtos,
                                  item_dtos,
                                  brand_dtos):

        section_dtos_list = []
        brand_dicts = self._convert_brands_to_dicts(brand_dtos)

        for section in section_dtos:
            section_order_dtos = self._get_section_orders(
                section_id=section.section_id,
                order_dtos=order_dtos
            )
            section_items_dtos = self._get_section_items(
                item_dtos=item_dtos, order_dtos=section_order_dtos
            )
            item_details_dtos = self._get_item_details_dtos(
                section_order_dtos=section_order_dtos,
                section_items_dtos=section_items_dtos,
                brand_dicts=brand_dicts
            )
            dto = GetFormSectionDto(section_id=section.section_id,
                                    name=section.name,
                                    description=section.description,
                                    items=item_details_dtos)
            section_dtos_list.append(dto)

        return section_dtos_list


    def _get_item_details_dtos(self,
                               section_order_dtos,
                               section_items_dtos,
                               brand_dicts):

        item_dto_list = []

        for item in section_items_dtos:
            brand_dtos = self._get_item_brands_dto_list(
                item=item,
                brand_dicts=brand_dicts)

            (order_id,
             brand_id,
             ordered_count,
             out_of_stock) = self._get_order_related_data_for_item(
                 item=item,
                 orders=section_order_dtos,
                 brand_dicts=brand_dicts)

            item_order_dto = GetFormItemOrderDto(order_id=order_id,
                                                 brand_id=brand_id,
                                                 ordered_count=ordered_count,
                                                 out_of_stock=out_of_stock)
                    
            dto = GetFormItemDto(item_id=item.item_id,
                                 name=item.name,
                                 description=item.description,
                                 brands=brand_dtos,
                                 order=item_order_dto)
            item_dto_list.append(dto)

        return item_dto_list


    def _get_order_related_data_for_item(self, item, orders, brand_dicts):

        order_obj = self._check_item_has_order_or_not_if_exits_return_obj(
                item_id=item.item_id, orders=orders
        )
        if order_obj:
            order_id = order_obj.order_id
            brand_id = order_obj.brand_id
            ordered_count = order_obj.count
            out_of_stock = order_obj.out_of_stock
        else:
            order_id = 0
            brand_id = 0
            ordered_count = 0
            out_of_stock = 0

        return  (order_id,
                 brand_id,
                 ordered_count,
                 out_of_stock)

    def  _check_item_has_order_or_not_if_exits_return_obj(self,
                                                          item_id,
                                                          orders):

        for order in orders:
            is_item_has_order = item_id == order.item_id
            if is_item_has_order:
                return order
        return False


    def _get_item_brands_dto_list(self, item, brand_dicts):
        brand_dto_list = []

        for brand in brand_dicts.values():
            is_items_belongs_to_brand = item.brand_id == brand.brand_id
            if is_items_belongs_to_brand:
                dto = BrandDto(brand_id=brand.brand_id,
                               name=brand.name,
                               min_quantity=brand.min_quantity,
                               max_quantity=brand.max_quantity,
                               price_per_item=brand.price_per_item)

                brand_dto_list.append(dto)
        return brand_dto_list

    def _convert_brands_to_dicts(self, brands_dtos):
        brands_dict = {}

        for brand in brands_dtos:
            single_dict = {
                brand.brand_id: brand
            }
            brands_dict.update(single_dict)
        return brands_dict


    def _get_section_items(self, item_dtos, order_dtos): # need to change the logic here

        items_list = []
        for order in order_dtos:
            for item in item_dtos:
                is_order_belongs_to_item = order.item_id == item.item_id
                if is_order_belongs_to_item:
                    items_list.append(item)
            return items_list


    def _get_section_orders(self,
                           section_id,
                           order_dtos):
        orders_list = []

        for order in order_dtos:
            is_order_belongs_to_section = section_id == order.section_id
            if is_order_belongs_to_section:
                orders_list.append(order)
        return orders_list

