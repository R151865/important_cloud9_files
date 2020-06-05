import datetime

import pytest

from essentials_kit_management.storages.form_storage_implementation import \
    FormStorageImplementation

from essentials_kit_management.interactors.storages.dtos import (
    GetFormItemDtoWithSectionId, GetFormBrandDtoWithItemId
    )


@pytest.mark.django_db
def test_get_brand_dtos_with_valid_details_return_dtos(populate_data):

    # Arrange
    item_dtos = [
        GetFormItemDtoWithSectionId(
                item_id=1,
                name="item1",
                description="item1",
                section_id=1),
        GetFormItemDtoWithSectionId(
                item_id=2,
                name="item2",
                description="item2",
                section_id=1)]

    expected_brand_dtos = [
        GetFormBrandDtoWithItemId(
            brand_id=1,
            name="brand1",
            min_quantity=1,
            max_quantity=5,
            price_per_item=100,
            item_id=1),
        GetFormBrandDtoWithItemId(
            brand_id=2,
            name="brand2",
            min_quantity=2,
            max_quantity=8,
            price_per_item=200,
            item_id=1),
        GetFormBrandDtoWithItemId(
            brand_id=3,
            name="brand3",
            min_quantity=3,
            max_quantity=9,
            price_per_item=300,
            item_id=2)
    ]

    storage = FormStorageImplementation()

    # Act
    actual_brand_dtos = storage.get_brand_dtos(item_dtos=item_dtos)

    # Assert
    assert actual_brand_dtos == expected_brand_dtos
