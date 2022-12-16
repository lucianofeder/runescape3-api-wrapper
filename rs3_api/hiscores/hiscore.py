from dataclasses import dataclass
from typing import Optional

from rs3_api.utils.const import AccountTypes

from .seasonal_hiscore import SeasonalDetailsHiscore
from .user_hiscore import UserHiscore


@dataclass
class Hiscore:
    def user(self, username: str, account_type: Optional[AccountTypes] = None) -> UserHiscore:
        return UserHiscore(username, account_type)

    @property
    def seasonal_events(self) -> SeasonalDetailsHiscore:
        return SeasonalDetailsHiscore()
