import pytest

from unittest.mock import create_autospec

from essentials_kit_management.interactors.storages.user_storage_interface \
    import UserStorageInterface
from essentials_kit_management.interactors.presenters. \
    user_presenter_interface import UserPresenterInterface
from essentials_kit_management.interactors.get_user_transactions_interactor \
    import GetUserTransactionsInteractor


def test_get_user_transactions_interactor(
        get_user_transaction_dtos_and_my_wallet_dto):

    # Arrange
    user_id = 1
    expected_dict = {}
    transaction_dtos = get_user_transaction_dtos_and_my_wallet_dto[0]
    my_wallet_dto = get_user_transaction_dtos_and_my_wallet_dto[1]

    user_storage = create_autospec(UserStorageInterface)
    user_presenter = create_autospec(UserPresenterInterface)
    interactor = GetUserTransactionsInteractor(user_storage=user_storage,
                                               user_presenter=user_presenter)

    user_storage.get_transaction_dtos.return_value = transaction_dtos
    user_presenter.get_user_transactions_response.return_value = expected_dict

    # Act
    actual_dict = interactor.get_user_transactions(user_id=user_id)

    # Assert
    user_storage.get_transaction_dtos.assert_called_once_with(user_id=user_id)
    user_presenter.get_user_transactions_response.assert_called_once_with(
        my_wallet_dto=my_wallet_dto)
    assert actual_dict == expected_dict
