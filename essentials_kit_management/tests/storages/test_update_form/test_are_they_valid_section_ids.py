import pytest

from essentials_kit_management.storages.section_storage_implementation \
    import SectionStorageImplementation

from essentials_kit_management.models import Section

@pytest.mark.django_db
def test_are_they_valid_section_ids_with_invalid_section_ids_return_false(
        populate_data):

    # Arrange
    invalid_section_ids = [1, 2, -1]
    section_storage = SectionStorageImplementation()

    # Act
    are_they_valid_section_ids = section_storage.are_they_valid_section_ids(
        section_ids=invalid_section_ids)

    # Assert
    assert are_they_valid_section_ids is False


@pytest.mark.django_db
def test_are_they_valid_section_ids_with_valid_section_ids_return_true(
        populate_data):

    # Arrange
    section_ids = [1, 2]
    section_storage = SectionStorageImplementation()

    # Act
    are_they_valid_section_ids = section_storage.are_they_valid_section_ids(
        section_ids=section_ids)

    # Assert
    assert are_they_valid_section_ids is True