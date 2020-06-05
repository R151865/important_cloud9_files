from essentials_kit_management.interactors.storages.user_storage_interface \
    import UserStorageInterface
from essentials_kit_management.interactors.presenters.user_presenter_interface \
    import UserPresenterInterface


from essentials_kit_management.interactors.storages.dtos import (
    GetUserTransactionDto, GetMyWalletDto
    )

from essentials_kit_management.constants.enums import TransactionStatusEnum

class GetUserTransactionsInteractor:

    def __init__(self,
                 user_storage: UserStorageInterface,
                 user_presenter: UserPresenterInterface):

        self.user_storage = user_storage
        self.user_presenter = user_presenter

    def get_user_transactions(self, user_id: int):

        transaction_dtos = self.user_storage.get_transaction_dtos(
            user_id=user_id)

        my_wallet_dto  = self._get_my_wallet_details_dto(
            transaction_dtos)

        response = self.user_presenter.get_user_transactions_response(
            my_wallet_dto=my_wallet_dto)

        return response


    def _get_my_wallet_details_dto(self, transaction_dtos):

        dto_list, balance = self._get_transaction_dtos_list_and_balance(
            transaction_dtos)
        get_my_wallte_dto = GetMyWalletDto(balance=balance,
                                           transaction_dtos=dto_list)

        return get_my_wallte_dto

    def _get_transaction_dtos_list_and_balance(self, transaction_dtos):
        dto_list = []
        balance = 0

        for transaction in transaction_dtos:
            if self._is_approved_transaction(transaction=transaction):
                balance += transaction.amount
    
            dto = GetUserTransactionDto(
                transaction_id=transaction.transaction_id,
                date=transaction.date,
                amount=transaction.amount,
                status=transaction.status,
                remark=transaction.remark)
            dto_list.append(dto)

        return dto_list, balance


    def _is_approved_transaction(self, transaction):
        is_approved_status = \
            (transaction.status == TransactionStatusEnum.APPROVED.value)
            # i need clarity whethe is it giviing bool or typle
        return is_approved_status