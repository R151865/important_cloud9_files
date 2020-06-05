from essentials_kit_management.interactors.storages.user_storage_interface \
    import UserStorageInterface
from essentials_kit_management.interactors. \
    presenters.user_presenter_interface import UserPresenterInterface


from typing import Dict
from essentials_kit_management.interactors.storages.dtos import \
    TransactionRequestDto


class CreateTransactionRequestInteractor:

    def __init__(self,
                 user_storage: UserStorageInterface,
                 user_presenter: UserPresenterInterface):
        self.user_storage = user_storage
        self.user_presenter = user_presenter

    def create_transaction_request(self, user_id: int, transaction_dict: Dict):

        amount = transaction_dict["amount_paid"]
        transaction_id = transaction_dict["transaction_id"]

        is_valid_amount = self.user_storage.is_valid_payment(amount=amount)
        invalid_amount_given = not is_valid_amount

        if invalid_amount_given:
            self.user_presenter.raise_invalid_payment_exception()
            return

        is_transaction_id_exists = self.user_storage.is_transaction_id_exists(
            transaction_id=transaction_id)

        if is_transaction_id_exists:
            self.user_presenter.raise_transaction_id_already_exist_exception()
            return

        transaction_request_dto = self._convert_transaction_dict_to_dto(
                transaction_dict=transaction_dict)

        self.user_storage.create_transaction_request_db(
            user_id=user_id,
            transaction_request_dto=transaction_request_dto)

    def _convert_transaction_dict_to_dto(self, transaction_dict):
        return TransactionRequestDto(
                    amount_paid=transaction_dict["amount_paid"],
                    transaction_id=transaction_dict["transaction_id"],
                    payment_type=transaction_dict["payment_type"],
                    transaction_screenshot=transaction_dict["transaction_screenshot"])
