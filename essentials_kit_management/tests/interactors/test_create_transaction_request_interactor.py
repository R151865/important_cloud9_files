import pytest
from unittest.mock import create_autospec

from django_swagger_utils.drf_server.exceptions import NotFound

from essentials_kit_management.interactors.storages.user_storage_interface \
    import UserStorageInterface
from essentials_kit_management.interactors.presenters.user_presenter_interface \
    import UserPresenterInterface

from essentials_kit_management.interactors. \
    create_transaction_request_interactor import \
        CreateTransactionRequestInteractor

from essentials_kit_management.interactors.storages.dtos import \
    TransactionRequestDto
# i need to add test cases for it

def test_create_transaction_request_interactor():

    # Arrange
    user_id = 1
    amount_paid=10001
    transaction_id = 1234567890
    transaction_dict = {
        "amount_paid": amount_paid,
        "transaction_type": "PAYTM",
        "transaction_id": transaction_id,
        "transaction_screenshot": "screenshot/photo.png"
    }
    expected_transaction_request_dto = TransactionRequestDto(
        amount_paid=10001,
        transaction_type="PAYTM",
        transaction_id=transaction_id,
        transaction_screenshot="screenshot/photo.png"
    )

    user_storage = create_autospec(UserStorageInterface)
    user_presenter = create_autospec(UserPresenterInterface)
    interactor = CreateTransactionRequestInteractor(
        user_storage=user_storage,
        user_presenter=user_presenter)
    user_storage.is_transaction_id_exists.return_value = False

    # Act
    interactor.create_transaction_request(user_id=user_id,
                                          transaction_dict=transaction_dict)
           

    # Assert
    user_storage.is_valid_payment.assert_called_once_with(amount=amount_paid)
    user_storage.is_transaction_id_exists.assert_called_once_with(
        transaction_id=transaction_id)
    user_storage.create_transaction_request_db.assert_called_once()


def test_create_transaction_request_interactor_with_invalid_payment_raise_exception(
    ):

    # Arrange
    user_id = 1
    invalid_payment = -10
    transaction_dict = {
        "amount_paid": invalid_payment,
        "transaction_type": "PAYTM",
        "transaction_id": 1234567890,
        "transaction_screenshot": "screenshot/photo.png"
    }

    user_storage = create_autospec(UserStorageInterface)
    user_presenter = create_autospec(UserPresenterInterface)
    interactor = CreateTransactionRequestInteractor(
        user_storage=user_storage,
        user_presenter=user_presenter)
    user_storage.is_valid_payment.return_value = False
    user_presenter.raise_invalid_payment_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_transaction_request(
            user_id=user_id,
            transaction_dict=transaction_dict)


def test_create_transaction_request_interactor_with_existed_transaction_id_raise_exception(
    ):

    # Arrange
    user_id = 1
    invalid_payment = 10
    transaction_dict = {
        "amount_paid": invalid_payment,
        "transaction_type": "PAYTM",
        "transaction_id": 1234567890,
        "transaction_screenshot": "screenshot/photo.png"
    }

    user_storage = create_autospec(UserStorageInterface)
    user_presenter = create_autospec(UserPresenterInterface)
    interactor = CreateTransactionRequestInteractor(
        user_storage=user_storage,
        user_presenter=user_presenter)

    user_storage.is_transaction_id_exists.return_value = True
    user_presenter.raise_transaction_id_already_exist_exception.side_effect = \
        NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_transaction_request(
            user_id=user_id,
            transaction_dict=transaction_dict)
