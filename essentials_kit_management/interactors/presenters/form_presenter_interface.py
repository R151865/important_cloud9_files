from abc import ABC, abstractmethod

from typing import List

from essentials_kit_management.interactors.storages.dtos import (
    GetUserOrderDto
    )

class FormPresenterInterface():

    def get_forms_response(self, form_dtos,
                            total_forms_count: int):
        pass

    def raise_invalid_form_id_exception(self):
        pass

    def get_form_to_fill_response(self, form_dto):
        pass

    def get_form_response(self, get_form_details_dto):
        pass

    def get_user_ordered_details_response(
            self,
            order_detail_dtos: List[GetUserOrderDto]):
        pass

    def raise_invalid_offset_and_limit_exception(self):
        pass