import pytest
from freezegun import freeze_time

from essentials_kit_management.models import (
    User, Transaction, Account
)

from essentials_kit_management.constants.enums import (
    TransactionStatusEnum, TransactionTypeEnum
    )


users_list = [
    {
        "name": "stevejobs",
        "username": 9876543210,
        "password": "steve123"},
    {
        "name": "che",
        "username": 9876543212,
        "password": "che123"},
    {
        "name": "sulthan",
        "username": 9876543213,
        "password": "sulthan123"}
]

transaction_list = [
    {
        "transaction_id": 111111,
        "user_id": 1,
        "amount": 100,
        "status": TransactionStatusEnum.APPROVED.value,
        "transaction_type": TransactionTypeEnum.PHONE_PAY.value,
        "screen_shot": "12/12",
        "remark": "wallet"
    },
    {
        "transaction_id": 222222,
        "user_id": 1,
        "amount": 200,
        "status": TransactionStatusEnum.PENDING.value,
        "transaction_type": TransactionTypeEnum.GOOGLE_PAY.value,
        "screen_shot": "12/12",
        "remark": "snacks"
    }
]


account_list = [
    {
        "upi_id": "1234567890@SBI"
    }
]


@pytest.fixture()
@freeze_time("2020-10-10")
def create_transactions():
    for transaction in transaction_list:
        Transaction.objects.create(
            transaction_id=transaction['transaction_id'],
            user_id=transaction['user_id'],
            amount=transaction['amount'],
            status=transaction['status'],
            transaction_type=transaction["transaction_type"],
            screen_shot=transaction["screen_shot"],
            remark=transaction["remark"])



@pytest.fixture()
def create_users():

    for user in users_list:
        User.objects.create(name=user["name"],
                     username=user["username"],
                     password=user["password"])


@pytest.fixture()
def create_account():
    for account in account_list:
        Account.objects.create(upi_id=account["upi_id"])