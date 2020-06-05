import pytest
from essentials_kit_management.presenters.user_presenter_implementation \
    import UserPresenterImplementation


def test_get_user_transactions_interactor(
        get_user_transaction_dto_and_expected_dict):

    # Arrange
    my_wallet_dto = get_user_transaction_dto_and_expected_dict[0]
    expected_dict = get_user_transaction_dto_and_expected_dict[1]
    presenter = UserPresenterImplementation()

    # Act
    actual_dict = presenter.get_user_transactions_response(
        my_wallet_dto=my_wallet_dto)

    # Assert
    assert actual_dict == expected_dict