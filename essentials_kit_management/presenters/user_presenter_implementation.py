import datetime
from common.dtos import UserAuthTokensDTO

from essentials_kit_management.interactors.presenters import \
    UserPresenterInterface

from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from essentials_kit_management.exceptions.exceptions import (
    InvalidPassword, InvalidUsername
    )

from essentials_kit_management.constants.exception_messages import (
    INVALID_PASSWORD, INVALID_USER_NAME, USERNAME_ARLEADY_EXISTS,
    INVALID_PAYMENT, TRANSACTION_ID_ALREADY_EXISTS
    )


class UserPresenterImplementation(UserPresenterInterface):

    @staticmethod
    def get_expires_time_fomate(datetime):
        return datetime.strftime("%Y-%m-%d %H:%M:%S.%f")

    @staticmethod
    def get_date_time_format(datetime):
        return datetime.strftime("%Y-%m-%d %H:%M:%S")

    def raise_invalid_password_exception(self):
        raise NotFound(*INVALID_PASSWORD)

    def raise_invalid_username_exception(self):
        raise NotFound(*INVALID_USER_NAME)

    def get_access_token_response(self, acces_token_dto: UserAuthTokensDTO): # ->access token Dto
        return {
            "user_id": acces_token_dto.user_id,
            "access_token": acces_token_dto.access_token,
            "refresh_token": acces_token_dto.refresh_token,
            "expires_in": self.get_expires_time_fomate(
                acces_token_dto.expires_in)
        }

    def raise_username_already_exists_exception(self):
        raise Forbidden(*USERNAME_ARLEADY_EXISTS)


    def get_user_transactions_response(self, my_wallet_dto):
        balance = my_wallet_dto.balance
        transaction_dtos = my_wallet_dto.transaction_dtos

        transaction_dicts = self._get_transaction_dicts_list(
            transaction_dtos=transaction_dtos)

        reponse_dict = {
            "balance": balance,
            "transactions": transaction_dicts
        }
        return reponse_dict


    def _get_transaction_dicts_list(self, transaction_dtos):
        transaction_dict_list = []

        for transaction in transaction_dtos:
            single_dict = {
                "transaction_id": transaction.transaction_id,
                "date": self.get_date_time_format(transaction.date),
                "amount": transaction.amount,
                "status": transaction.status,
                "type": transaction.transaction_type,
                "remark": transaction.remark
            }
            transaction_dict_list.append(single_dict)
        return transaction_dict_list


    def raise_invalid_payment_exception(self):
        raise NotFound(*INVALID_PAYMENT)

    def raise_transaction_id_already_exist_exception(self):
        raise NotFound(*TRANSACTION_ID_ALREADY_EXISTS)

    def get_upi_id_response(self, upi_id: str):
        return {
            "upi_id": upi_id
        }