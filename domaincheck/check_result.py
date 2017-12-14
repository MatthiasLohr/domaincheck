
from enum import Enum


class CheckResult(Enum):
    INVALID = {'key': 1}
    USED = {'key': 2}
    FOR_SALE = {'key': 3}
    AVAILABLE = {'key': 4}
