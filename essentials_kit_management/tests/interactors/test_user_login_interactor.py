import pytest

from unittest.mock import create_autospec, patch
from django_swagger_utils.drf_server.exceptions import NotFound


from essentials_kit_management.interactors.storages.user_storage_interface \
    import UserStorageInterface
from essentials_kit_management.interactors.presenters.user_presenter_interface \
    import UserPresenterInterface

from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService


from essentials_kit_management.interactors.user_login_interactor import \
    UserLoginInteractor
from essentials_kit_management.exceptions.exceptions import (
    InvalidPassword, InvalidUsername
)

class TestUserLoginInteractor:

    @patch.object(OAuthUserAuthTokensService, "create_user_auth_tokens")
    def test_user_login_interactor_with_valid_details(
            self,
            create_user_auth_tokens):

        # Arrange
        username = "1234567890"
        password = "sulthan@123"
        user_id = 1
        acces_token_dto = []
        expected_access_token_dict = {
            "user_id":user_id,
            "access_token": "12334",
            "refresh_token": "123445",
            "expires_in": "2020-10-10"
        }

        user_storage = create_autospec(UserStorageInterface)
        user_presenter = create_autospec(UserPresenterInterface)
        oauth2_storage = create_autospec(OAuth2SQLStorage)
        interactor = UserLoginInteractor(
            user_storage=user_storage,
            user_presenter=user_presenter,
            oauth2_storage=oauth2_storage)
            
        user_storage.validate_username.return_value = user_id
        create_user_auth_tokens.return_value = acces_token_dto
        user_presenter.get_access_token_response.return_value = \
            expected_access_token_dict
    
        # Act
        actual_access_token_dict = interactor.user_login(username=username,
                                                    password=password)

        # Assert
        user_storage.validate_password.assert_called_once_with(
            password=password)
        user_storage.validate_username.assert_called_once_with(
            username=username,
            password=password)
        create_user_auth_tokens.assert_called_once_with(user_id=user_id)
        user_presenter.get_access_token_response.assert_called_once_with(
            acces_token_dto=acces_token_dto)
        assert actual_access_token_dict == expected_access_token_dict


    def test_user_login_interactor_with_invalid_password_raise_exception(
            self):

        # Arrange
        username = "1234567890"
        invalid_password = "12jfsj455"

        user_storage = create_autospec(UserStorageInterface)
        user_presenter = create_autospec(UserPresenterInterface)
        oauth2_storage = create_autospec(OAuth2SQLStorage)
        interactor = UserLoginInteractor(
            user_storage=user_storage,
            user_presenter=user_presenter,
            oauth2_storage=oauth2_storage)

        user_storage.validate_password.side_effect = InvalidPassword
        user_presenter.raise_invalid_password_exception.side_effect = NotFound
        # Act
        with pytest.raises(NotFound):
            interactor.user_login(username=username,
                                  password=invalid_password)

    def test_user_login_interactor_with_invalid_username_raise_exception(
            self):

        # Arrange
        invalid_username = "1234567890"
        password = "sulthan123"

        user_storage = create_autospec(UserStorageInterface)
        user_presenter = create_autospec(UserPresenterInterface)
        oauth2_storage = create_autospec(OAuth2SQLStorage)
        interactor = UserLoginInteractor(
            user_storage=user_storage,
            user_presenter=user_presenter,
            oauth2_storage=oauth2_storage)
            
        user_storage.validate_username.side_effect = InvalidUsername
        user_presenter.raise_invalid_username_exception.side_effect = NotFound
        # Act
        with pytest.raises(NotFound):
            interactor.user_login(username=invalid_username,
                                  password=password)
