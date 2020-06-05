import datetime

import pytest

from essentials_kit_management.storages.user_storage_implementation \
    import UserStorageImplementation

from essentials_kit_management.interactors.storages.dtos import (
    TransactionDto
)

@pytest.mark.django_db
def test_get_transaction_dtos_with_valid_details_return_dtos(
        create_users,
        create_transactions):

    # Arrange
    user_id = 1
    transaction1 = TransactionDto(
            transaction_id=111111,
            user_id=1,
            date=datetime.datetime(2020, 10, 10, 0, 0, 0),
            amount=100,
            status="APPROVED",
            transaction_type="PHONE_PAY",
            screen_shot="12/12",
            remark="wallet")

    transaction2 = TransactionDto(
            transaction_id=222222,
            user_id=1,
            date=datetime.datetime(2020, 10, 10, 0, 0, 0),
            amount=200,
            status="PENDING",
            transaction_type="GOOGLE_PAY",
            screen_shot="12/12",
            remark="snacks")
    expected_transaction_dtos = [transaction1, transaction2]
    storage = UserStorageImplementation()

    # Act
    actual_transaction_dtos = storage.get_transaction_dtos(
        user_id=user_id)

    # Assert
    assert actual_transaction_dtos == expected_transaction_dtos