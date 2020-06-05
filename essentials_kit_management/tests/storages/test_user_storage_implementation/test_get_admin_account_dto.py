import pytest

from essentials_kit_management.storages.user_storage_implementation import \
    UserStorageImplementation

from essentials_kit_management.interactors.storages.dtos import \
    AccountDetailsDto

@pytest.mark.django_db
def test_get_account_dto(create_account):

    # Arrange
    expected_account_dto =  AccountDetailsDto(
        upi_id="1234567890@SBI",
        account_holder="")
    storage = UserStorageImplementation()

    # Act
    actual_account_dto = storage.get_admin_account_dto()

    # Assert
    assert actual_account_dto == expected_account_dto