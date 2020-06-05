import pytest

from unittest.mock import create_autospec, patch
from django_swagger_utils.drf_server.exceptions import NotFound

from essentials_kit_management.interactors.storages.user_storage_interface \
    import UserStorageInterface
from essentials_kit_management.interactors.presenters.user_presenter_interface \
    import UserPresenterInterface

from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService

from essentials_kit_management.interactors.create_user_signup_interactor \
    import CreateUserSignUpInteractor


class TestCreateUserSignUpInteractor:

    @patch.object(OAuthUserAuthTokensService, "create_user_auth_tokens")
    def test_create_user_singup_interactor(self,
                                           create_user_auth_tokens):

        # Arrange
        name = "Sulthi Bhai"
        username = "1234567890"
        password = "sulthan@123"
        user_id = 1
        acces_token_dto = []
        expected_access_token_dict = {
            "user_id": user_id,
            "access_token": "12334",
            "refresh_token": "123445",
            "expires_in": "2020-10-10"
        }

        user_storage = create_autospec(UserStorageInterface)
        user_presenter = create_autospec(UserPresenterInterface)
        oauth2_storage = create_autospec(OAuth2SQLStorage)
        interactor = CreateUserSignUpInteractor(
            user_storage=user_storage,
            user_presenter=user_presenter,
            oauth2_storage=oauth2_storage)

        user_storage.is_username_already_exists.return_value = False
        user_storage.create_user.return_value = user_id
        create_user_auth_tokens.return_value = acces_token_dto
        user_presenter.get_access_token_response.return_value = \
            expected_access_token_dict

        # Act
        actual_access_token_dict = interactor.create_signup(name=name,
                                                            username=username,
                                                            password=password)

        # Assert
        user_storage.is_username_already_exists.assert_called_once_with(
            username=username)
        user_storage.create_user.assert_called_once_with(name=name,
                                                         username=username,
                                                         password=password)
        create_user_auth_tokens.assert_called_once_with(user_id=user_id)
        assert actual_access_token_dict == expected_access_token_dict



    def test_create_user_singup_interactor_with_exists_username_raise_exception(
            self):

        # Arrange
        name = "Sulthi Bhai"
        username = "1234567890"
        password = "Sulthan@143"

        user_storage = create_autospec(UserStorageInterface)
        user_presenter = create_autospec(UserPresenterInterface)
        oauth2_storage = create_autospec(OAuth2SQLStorage)
        interactor = CreateUserSignUpInteractor(
            user_storage=user_storage,
            user_presenter=user_presenter,
            oauth2_storage=oauth2_storage)

        user_storage.is_username_already_exists.return_value = True
        user_presenter.raise_username_already_exists_exception.side_effect = \
            NotFound

        # Act
        with pytest.raises(NotFound):
            interactor.create_signup(name=name,
                                     username=username,
                                     password=password)