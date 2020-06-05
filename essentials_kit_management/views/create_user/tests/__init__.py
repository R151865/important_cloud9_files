# pylint: disable=wrong-import-position

APP_NAME = "essentials_kit_management"
OPERATION_NAME = "create_user"
REQUEST_METHOD = "post"
URL_SUFFIX = "users/create/"

from .test_case_01 import TestCase01CreateUserAPITestCase

__all__ = [
    "TestCase01CreateUserAPITestCase"
]
