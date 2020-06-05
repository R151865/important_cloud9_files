import datetime

import pytest

from essentials_kit_management.storages.form_storage_implementation import \
    FormStorageImplementation

from essentials_kit_management.interactors.storages.dtos import FormDto


@pytest.mark.django_db
def test_get_form_dto_return_form_dto(create_users,
                                      create_brands,
                                      create_items,
                                      create_sections,
                                      create_forms):

    # Arrange
    form_id = 1
    expected_form_dto = FormDto(
        form_id=1,
        name="form1",
        description="form1",
        close_date=datetime.datetime(2020, 10, 10, 0, 0, 0),
        expected_delivery_date=datetime.datetime(2020, 10, 10, 0, 0, 0),
        status="LIVE"
        )

    storage = FormStorageImplementation()

    # Act
    actual_form_dto = storage.get_form_dto(form_id=form_id)

    # Assert
    assert actual_form_dto == expected_form_dto