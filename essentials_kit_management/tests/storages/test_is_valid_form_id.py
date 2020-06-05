import pytest

from essentials_kit_management.storages.form_storage_implementation import \
    FormStorageImplementation

@pytest.mark.django_db
def test_is_valid_form_id_with_invalid_id_return_false(create_users,
                                                       create_brands,
                                                       create_items,
                                                       create_sections,
                                                       create_forms):

    # Arrange
    invalid_form_id = -1
    storage = FormStorageImplementation()

    # Act
    is_valid_form_id = storage.is_valid_form_id(form_id=invalid_form_id)

    # Assert
    assert is_valid_form_id is False

@pytest.mark.django_db
def test_is_valid_form_id_with_valid_id_return_true(create_users,
                                                    create_brands,
                                                    create_items,
                                                    create_sections,
                                                    create_forms):

    # Arrange
    form_id = 3
    storage = FormStorageImplementation()
    
    # Act
    is_valid_form_id = storage.is_valid_form_id(form_id=form_id)

    # Assert
    assert is_valid_form_id is True