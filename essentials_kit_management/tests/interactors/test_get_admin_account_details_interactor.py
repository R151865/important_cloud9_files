from unittest.mock import create_autospec

from essentials_kit_management.interactors.storages.user_storage_interface \
    import UserStorageInterface
from essentials_kit_management.interactors.presenters. \
    user_presenter_interface import UserPresenterInterface

from essentials_kit_management.interactors.storages.dtos import \
    AccountDetailsDto

from essentials_kit_management.interactors. \
    get_admin_account_details_interactor import \
    GetAdminAccountDetailsInteractor


def test_get_admin_account_details_interactor():

        # Arrange
        expected_dict = {
            "upi_id": "12356880987@SBI"
        }
        upi_id = "12356880987@SBI"
        account_dto = AccountDetailsDto(
            upi_id="12356880987@SBI",
            account_holder="sulthan the topu "
        )

        user_storage = create_autospec(UserStorageInterface)
        user_presenter = create_autospec(UserPresenterInterface)
        interactor = GetAdminAccountDetailsInteractor(
            user_storage=user_storage,
            user_presenter=user_presenter)

        user_storage.get_admin_account_dto.return_value = account_dto
        user_presenter.get_upi_id_response.return_value = expected_dict

        # Act
        actual_dict = interactor.get_admin_account_details()

        # Assert
        user_storage.get_admin_account_dto.assert_called_once()
        user_presenter.get_upi_id_response.assert_called_once_with(
            upi_id=upi_id)
        assert actual_dict == expected_dict
