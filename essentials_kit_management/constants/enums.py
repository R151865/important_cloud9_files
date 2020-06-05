import enum

from ib_common.constants import BaseEnumClass


class CodeLanguage(BaseEnumClass, enum.Enum):
    python = "PYTHON"
    c_language = "C"
    c_plus_plus = "CPP"
    python36 = "PYTHON36"
    python37 = "PYTHON37"
    python38 = "PYTHON38"
    python38_datascience = "PYTHON38_DATASCIENCE"
    python38_aiml = "PYTHON38_AIML"


class FormStatusEnum(enum.Enum):
    LIVE = "LIVE"
    CLOSED = "CLOSED"
    DONE = "DONE"


class TransactionStatusEnum(enum.Enum):
    APPROVED = "APPROVED"
    PENDING = "PENDING"
    REJECTED = "REJECTED"


class PaymentTypeEnum(enum.Enum):
    PHONE_PAY = "PHONE_PAY"
    GOOGLE_PAY = "GOOGLE_PAY"
    PAYTM = "PAYTM"


class TransactionTypeEnum(enum.Enum):
    CREDITED = "CREDITED"
    DEBITED = "DEBITED"