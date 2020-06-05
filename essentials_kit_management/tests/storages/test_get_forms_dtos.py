import datetime

import pytest

from essentials_kit_management.storages.form_storage_implementation import \
    FormStorageImplementation

from essentials_kit_management.interactors.storages.dtos import FormDto



@pytest.mark.django_db
def test_get_forms_dtos_return_form_list(create_users,
                                         create_brands,
                                         create_items,
                                         create_sections,
                                         create_forms):

    # Arrange
    offset = 0
    limit = 2
    expected_actual_forms_count = 3
    form_dto1 = FormDto(
        form_id=1,
        name="form1",
        description="form1",
        close_date=datetime.datetime(2020, 10, 10, 0, 0, 0),
        expected_delivery_date=datetime.datetime(2020, 10, 10, 0, 0, 0),
        status="LIVE"
        ) 
    form_dto2 = FormDto(
        form_id=2,
        name="form2",
        description="form2",
        close_date=datetime.datetime(2020, 10, 10, 0, 0, 0),
        expected_delivery_date=datetime.datetime(2020, 10, 10, 0, 0, 0),
        status="CLOSED"
        ) 
    expected_list = [form_dto1, form_dto2]

    storage = FormStorageImplementation()

    # Act
    actual_list, actual_total_forms_count = \
        storage.get_forms_dtos(offset=offset, limit=limit)

    # Assert
    assert actual_list == expected_list
    assert actual_total_forms_count == expected_actual_forms_count
