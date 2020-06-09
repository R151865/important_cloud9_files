import datetime

from essentials_kit_management.interactors.presenters.form_presenter_interface \
    import FormPresenterInterface

from essentials_kit_management.interactors.storages.dtos import (
    HomePageFormDto
)
from django_swagger_utils.drf_server.exceptions import NotFound

from essentials_kit_management.constants.exception_messages import (
    INVALID_FORM_ID, INVALID_OFFSET_LENGTH
    )


from essentials_kit_management.constants.constants import DATE_TIME_FORMAT

class FormPresenterImplementation(FormPresenterInterface):

    def get_forms_response(self, form_dtos, total_forms_count: int):
        total_forms_count = total_forms_count

        forms = [
            {
                "form_id": form_dto.form_id,
                "form_name": form_dto.name,
                "form_status": form_dto.status,
                "close_date": self.convert_time_stamp(form_dto.close_date),
                "expected_delivery_date": \
                    self.convert_time_stamp(form_dto.expected_delivery_date),
                "items_count": form_dto.items_count,
                "estimated_cost": form_dto.estimated_cost,
                "items_pending_count": form_dto.items_pending_count,
                "cost_incurred": form_dto. \
                    cost_incurred_for_delivery,
            }
            for form_dto in form_dtos
            ]

        json_data = {
            "forms": forms,
            "total_forms_count": total_forms_count
        }

        return json_data

    @staticmethod
    def convert_time_stamp(datetime):
        return datetime.strftime(DATE_TIME_FORMAT)

    def raise_invalid_form_id_exception(self):
        raise NotFound(*INVALID_FORM_ID)

    def get_form_to_fill_response(self, form_dto):
        pass

    def get_form_response(self, get_form_details_dto):
        form = get_form_details_dto
        sections = form.sections

        section_dict_list = self._get_section_dict_list(sections)

        form_dict = {
            "form_id": form.form_id,
            "form_name": form.name,
            "close_date": self.convert_time_stamp(form.close_date),
            "sections": section_dict_list
        }
        return form_dict

    def _get_section_dict_list(self, sections):
        section_dict_list = []

        for section in sections:
            items = section.items
            item_dict_list = self._get_item_dict_list(items)
            section_dict = {
                "section_id": section.section_id,
                "name": section.name,
                "description": section.description,
                "items_details": item_dict_list
            }
            section_dict_list.append(section_dict)
        return section_dict_list

    def _get_item_dict_list(self, items):
        item_dict_list = []

        for item in items:
            brands = item.brands
            brand_dict_list = self._get_brand_dict_list(brands)
            order_dict = self._get_order_dict(item.order)
            item_dict = {
                "item_id": item.item_id,
                "item_name": item.name,
                "description": item.description,
                "brands": brand_dict_list,
                "order": order_dict
            }
            item_dict_list.append(item_dict)

        return item_dict_list

    def _get_order_dict(self, order):
        return {
            "order_id": order.order_id,
            "brand_id": order.brand_id,
            "ordered_count": order.ordered_count,
            "out_of_stock": order.out_of_stock
        }

    def _get_brand_dict_list(self, brands):
        brand_dict_list = [
            self._convert_brand_dto_to_dict(brand)
            for brand in brands
            ]
        return brand_dict_list

    def _convert_brand_dto_to_dict(self, brand):
        return {
            "brand_id": brand.brand_id,
            "brand_name": brand.name,
            "min_quantity": brand.min_quantity,
            "max_quantity": brand.max_quantity,
            "price_per_item": brand.price_per_item
        }

    def get_user_ordered_details_response(self, order_detail_dtos):
        order_details_list = [
            self._convert_to_get_user_order_dto_to_dict(user_order_dto)
            for user_order_dto in order_detail_dtos
            ]
        return order_details_list

    def _convert_to_get_user_order_dto_to_dict(self, user_order_dtos):
        return {
            "item_id": user_order_dtos.item_id,
            "item_name": user_order_dtos.item_name,
            "items_added": user_order_dtos.items_added,
            "items_recived": user_order_dtos.items_recived,
            "cost_incurred": user_order_dtos.cost_incurred,
            "out_of_stock": user_order_dtos.out_of_stock
        }

    def raise_invalid_offset_and_limit_exception(self):
        raise NotFound(*INVALID_OFFSET_LENGTH)
