from essentials_kit_management.interactors.storages.user_storage_interface \
    import UserStorageInterface

from essentials_kit_management.interactors.presenters. \
    user_presenter_interface import UserPresenterInterface

from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService

from essentials_kit_management.exceptions.exceptions import (
    InvalidPassword, InvalidUsername
)


class CreateUserSignUpInteractor:

    def __init__(self,
                 user_storage: UserStorageInterface,
                 user_presenter: UserPresenterInterface,
                 oauth2_storage: OAuth2SQLStorage):

        self.user_storage = user_storage
        self.user_presenter = user_presenter
        self.oauth2_storage = oauth2_storage

    def create_signup(self, name: str, username: str, password: str):

        is_username_already_exists = \
            self.user_storage.is_username_already_exists(username=username)

        if is_username_already_exists:
            self.user_presenter.raise_username_already_exists_exception()
            return

        user_id = self.user_storage.create_user(name=name,
                                                username=username,
                                                password=password)

        service = OAuthUserAuthTokensService(
            oauth2_storage=self.oauth2_storage
        )
        acces_token_dto = service.create_user_auth_tokens(user_id=user_id)

        response = self.user_presenter.get_access_token_response(
            acces_token_dto=acces_token_dto)

        return response
