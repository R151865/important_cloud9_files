# pylint: disable=wrong-import-position

APP_NAME = "essentials_kit_management"
OPERATION_NAME = "get_user_ordered_details"
REQUEST_METHOD = "get"
URL_SUFFIX = "forms/{form_id}/ordered/details/"

from .test_case_01 import TestCase01GetUserOrderedDetailsAPITestCase

__all__ = [
    "TestCase01GetUserOrderedDetailsAPITestCase"
]
