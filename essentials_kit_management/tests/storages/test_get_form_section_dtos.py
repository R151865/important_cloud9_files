import datetime

import pytest

from essentials_kit_management.storages.form_storage_implementation import \
    FormStorageImplementation

from essentials_kit_management.interactors.storages.dtos import SectionDto


@pytest.mark.django_db
def test_get_form_section_dtos_with_valid_details_return_dtos(populate_data):
    # Arrange
    form_id = 1

    expected_section_dtos = [
        SectionDto(
            section_id=1,
            name="section1",
            description="section1"),
        SectionDto(
            section_id=2,
            name="section2",
            description="section2")
        ]

    storage = FormStorageImplementation()

    # Act
    actual_section_dtos = storage.get_form_sections_dtos(form_id=form_id)

    # Assert
    assert actual_section_dtos == expected_section_dtos
