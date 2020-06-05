from abc import ABC, abstractmethod

from essentials_kit_management.interactors.storages.dtos import (
    UserDto, TransactionRequestDto
)

class UserStorageInterface():

    def create_user(self, name: str, username: str, password: str) ->int:
        pass

    def validate_password(self, password: str):
        pass

    def validate_username(self, username: int, password: str):
        pass

    def get_transaction_dtos(self, user_id: int):
        pass

    def create_transaction_request_db(
            self,
            user_id: int,
            transaction_request_dto: TransactionRequestDto):
        pass

    def is_username_already_exists(self, username: str):
        pass

    def get_admin_account_dto(self):# need to mention dto here
        pass

    def is_valid_payment(self, amount: int):
        pass

    def  is_transaction_id_exists(self, transaction_id: int):
        pass
