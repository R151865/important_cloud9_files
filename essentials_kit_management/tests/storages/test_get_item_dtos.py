import datetime

import pytest

from essentials_kit_management.storages.form_storage_implementation import \
    FormStorageImplementation

from essentials_kit_management.interactors.storages.dtos import (
    SectionDto, GetFormItemDtoWithSectionId
    )


@pytest.mark.django_db
def test_get_item_dtos_with_valid_details_return_dtos(populate_data):

    # Arrange
    section_dtos = [
        SectionDto(
            section_id=1,
            name="section1",
            description="section1"),
        SectionDto(
            section_id=2,
            name="section2",
            description="section2")
        ]

    expected_item_dtos = [
        GetFormItemDtoWithSectionId(
                item_id=1,
                name="item1",
                description="item1",
                section_id=1),
        GetFormItemDtoWithSectionId(
                item_id=2,
                name="item2",
                description="item2",
                section_id=1),
        GetFormItemDtoWithSectionId(
                item_id=3,
                name="item3",
                description="item3",
                section_id=2)]

    storage = FormStorageImplementation()

    # Act
    actual_item_dtos = storage.get_item_dtos(section_dtos=section_dtos)

    # Assert
    assert actual_item_dtos == expected_item_dtos
