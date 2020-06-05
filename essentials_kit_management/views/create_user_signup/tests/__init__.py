# pylint: disable=wrong-import-position

APP_NAME = "essentials_kit_management"
OPERATION_NAME = "create_user_signup"
REQUEST_METHOD = "post"
URL_SUFFIX = "users/signup/"

from .test_case_01 import TestCase01CreateUserSignupAPITestCase

__all__ = [
    "TestCase01CreateUserSignupAPITestCase"
]
