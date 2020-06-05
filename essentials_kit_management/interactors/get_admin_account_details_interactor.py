from essentials_kit_management.interactors.storages.user_storage_interface \
    import UserStorageInterface
from essentials_kit_management.interactors. \
    presenters.user_presenter_interface import UserPresenterInterface


class GetAdminAccountDetailsInteractor:

    def __init__(self,
                 user_storage: UserStorageInterface,
                 user_presenter: UserPresenterInterface):

        self.user_storage = user_storage
        self.user_presenter = user_presenter

    def get_admin_account_details(self):

        account_dto = self.user_storage.get_admin_account_dto()
        upi_id = account_dto.upi_id

        response = self.user_presenter.get_upi_id_response(upi_id=upi_id)
        return response
