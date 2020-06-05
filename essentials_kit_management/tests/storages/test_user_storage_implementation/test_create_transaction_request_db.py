import datetime

import pytest

from essentials_kit_management.storages.user_storage_implementation \
    import UserStorageImplementation

from essentials_kit_management.interactors.storages.dtos import (
    TransactionRequestDto
)

from essentials_kit_management.models import Transaction

from essentials_kit_management.constants.enums import (
    PaymentTypeEnum, TransactionStatusEnum
    )



@pytest.mark.django_db
def test_create_transaction_request_db_with_valid_details_create_request(
        create_users):

    # Arrange
    user_id = 1
    transaction_id = 333333
    amount_paid = 100
    payment_type = PaymentTypeEnum.PAYTM.value
    transaction_screenshot = "urls/photo.png"
    status = TransactionStatusEnum.PENDING.value
    
    transaction_request_dto = TransactionRequestDto(
                    amount_paid=amount_paid,
                    transaction_id=transaction_id,
                    payment_type=payment_type,
                    transaction_screenshot=transaction_screenshot)
    storage = UserStorageImplementation()

    # Act
    actual_transaction_dtos = storage.create_transaction_request_db(
        user_id=user_id,
        transaction_request_dto=transaction_request_dto)

    # Assert
    transaction_obj = Transaction.objects.get(transaction_id=transaction_id)

    assert transaction_obj.transaction_id == transaction_id
    assert transaction_obj.user_id == user_id
    assert transaction_obj.amount == amount_paid
    assert transaction_obj.payment_type == payment_type
    assert transaction_obj.status == status
    assert transaction_obj.screen_shot == transaction_screenshot 