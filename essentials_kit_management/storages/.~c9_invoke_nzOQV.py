from essentials_kit_management.interactors.storages.user_storage_interface \
    import UserStorageInterface
from essentials_kit_management.models import User, Transaction

from essentials_kit_management.exceptions.exceptions import (
    InvalidPassword, InvalidUsername
)

from essentials_kit_management.interactors.storages.dtos import (
    TransactionDto
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



    def _convert_transaction_obj_to_dto(self, transaction_obj):
        return TransactionDto(
            transaction_id=transaction_obj.transaction_id,
            user_id=transaction_obj.user_id,
            datetime=transaction_obj.date,
            amoutn=transaction_obj.amountcde fg
,
            transaction_id=transaction_obj.transaction_id
            
            
            )
class TransactionDto:
    transaction_id: int
    user_id: int
    date: datetime
    amount: int
    status: TransactionStatusEnum
    transaction_type: TransactionTypeEnum
    remark: str
