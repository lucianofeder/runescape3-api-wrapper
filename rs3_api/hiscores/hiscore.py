from dataclasses import dataclass
from typing import Optional

from rs3_api.utils.const import AccountTypes

from .user_hiscore import UserHiscore


@dataclass
class Hiscore:

    def user(self, username: str, account_type: Optional[AccountTypes] = None) -> UserHiscore:
        return UserHiscore(username, account_type)