from abc import ABC, abstractmethod

from typing import List

from essentials_kit_management.interactors.storages.dtos import \
    FormCompleteDetailsDto

from essentials_kit_management.interactors.storages.dtos import (
    OrderDto, ItemDto, BrandDto, SectionDto, FormDto
)

class FormStorageInterface():

    def get_forms_dtos(self, offset: int, limit: int) ->FormCompleteDetailsDto:
        pass

    def is_valid_form_id(self, form_id: int):
        pass

    def get_user_order_dtos(self, user_id) ->List[OrderDto]:
        pass

    def get_user_brand_dtos(self, orders) ->List[BrandDto]:
        pass

    def get_user_item_dtos(self, orders) ->List[ItemDto]:
        pass

    def get_form_dto(self, form_id: int) ->FormDto:
        pass

    def get_order_dtos(self, user_id: int, form_id: int) ->List[OrderDto]:
        pass

    def get_form_sections_dtos(self, form_id: int) ->List[SectionDto]:
        pass

    def get_item_dtos(self, section_dtos) ->List[ItemDto]:
        pass

    def get_brand_dtos(self, item_dtos) ->List[BrandDto]:
        pass

    def are_they_valid_offset_and_limit(self, offset: int, limit: int):
        pass
