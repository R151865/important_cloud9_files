from abc import ABC, abstractmethod

from essentials_kit_management.interactors.storages.dtos import (
    GetMyWalletDto
    )

class UserPresenterInterface():

    def raise_invalid_password_exception(self):
        pass

    def raise_invalid_username_exception(self):
        pass

    def get_access_token_response(self, acces_token_dto): # need to write acces token dto
        pass

    def get_user_transactions_response(self,
                                      my_wallet_dto: GetMyWalletDto):
        pass

    def raise_username_already_exists_exception(self):
        pass

    def get_upi_id_response(self, upi_id: int):
        pass

    def raise_invalid_payment_exception(self):
        pass

    def raise_transaction_id_already_exist_exception(self):
        pass
