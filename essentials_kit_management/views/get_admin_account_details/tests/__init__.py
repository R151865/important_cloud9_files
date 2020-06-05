# pylint: disable=wrong-import-position

APP_NAME = "essentials_kit_management"
OPERATION_NAME = "get_admin_account_details"
REQUEST_METHOD = "get"
URL_SUFFIX = "admin/account/details/"

from .test_case_01 import TestCase01GetAdminAccountDetailsAPITestCase

__all__ = [
    "TestCase01GetAdminAccountDetailsAPITestCase"
]
