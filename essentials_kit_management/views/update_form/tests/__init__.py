# pylint: disable=wrong-import-position

APP_NAME = "essentials_kit_management"
OPERATION_NAME = "update_form"
REQUEST_METHOD = "post"
URL_SUFFIX = "forms/update/"

from .test_case_01 import TestCase01UpdateFormAPITestCase

__all__ = [
    "TestCase01UpdateFormAPITestCase"
]
