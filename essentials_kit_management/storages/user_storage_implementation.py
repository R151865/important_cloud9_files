from essentials_kit_management.interactors.storages.user_storage_interface \
    import UserStorageInterface
from essentials_kit_management.models import User, Transaction, Account

from essentials_kit_management.exceptions.exceptions import (
    InvalidPassword, InvalidUsername
)

from essentials_kit_management.interactors.storages.dtos import (
    TransactionDto, TransactionRequestDto, AccountDetailsDto
    )

from essentials_kit_management.constants.enums import (
    TransactionStatusEnum
    )


class UserStorageImplementation(UserStorageInterface):

    def create_user(self,
                    name: str,
                    username: str,
                    password: str):
        user_obj = User.objects.create(name=name,
                                       username=username,
                                       password=password)
        return user_obj.id

    def validate_password(self, password: str):

        is_valid_password = User.objects.filter(password=password).exists()
        in_valid_password_given = not is_valid_password
        
        if in_valid_password_given:
            raise InvalidPassword

    def validate_username(self, username: int, password: str):

        user_obj = User.objects.filter(username=username,
                                       password=password)
        invalid_username_given = not user_obj.exists()

        if invalid_username_given:
            raise InvalidUsername

        user_id = user_obj.first().id
        return user_id

    def is_username_already_exists(self, username: str):
        is_username_already_exists = User.objects \
                                         .filter(username=username).exists()
        return is_username_already_exists

    def get_transaction_dtos(self, user_id: int):
        transaction_objs = Transaction.objects.filter(user_id=user_id)
        transaction_dtos = [
            self._convert_transaction_obj_to_dto(transaction)
            for transaction in transaction_objs
            ]
        return transaction_dtos

    def _convert_transaction_obj_to_dto(self, transaction_obj):
        return TransactionDto(
            transaction_id=transaction_obj.transaction_id,
            user_id=transaction_obj.user_id,
            date=transaction_obj.date,
            amount=transaction_obj.amount,
            status=transaction_obj.status,
            transaction_type=transaction_obj.transaction_type,
            payment_type=transaction_obj.payment_type,
            screen_shot=transaction_obj.screen_shot,
            remark=transaction_obj.remark)

    def create_transaction_request_db(
            self,
            user_id: int,
            transaction_request_dto: TransactionRequestDto):

        transaction_obj = Transaction.objects.create(
            user_id=user_id,
            amount=transaction_request_dto.amount_paid,
            transaction_id=transaction_request_dto.transaction_id,
            payment_type=transaction_request_dto.payment_type,
            screen_shot=transaction_request_dto.transaction_screenshot,
            remark="Wallet")

    def get_admin_account_dto(self):
        account_obj = Account.objects.filter().first()
        account_dto = AccountDetailsDto(
            upi_id=account_obj.upi_id,
            account_holder=account_obj.account_holder)
        return account_dto

    def is_valid_payment(self, amount: int):
        is_positive_payment = amount > 0
        return is_positive_payment

    def is_transaction_id_exists(self, transaction_id: int):
        is_transaction_id_already_exists = \
            Transaction.objects.filter(transaction_id=transaction_id).exists()
        return is_transaction_id_already_exists
