from dataclasses import dataclass
from typing import Optional

from rs3_api.utils.const import AccountTypes

from .clan_hiscore import ClanMembersHiscore
from .seasonal_hiscore import SeasonalDetailsHiscore
from .user_hiscore import UserHiscore


@dataclass
class Hiscore:
    def user(self, username: str, account_type: Optional[AccountTypes] = None) -> UserHiscore:
        return UserHiscore(username, account_type)

    def clan(self, clan_name: str) -> ClanMembersHiscore:
        return ClanMembersHiscore(clan_name)

    @property
    def seasonal_events(self) -> SeasonalDetailsHiscore:
        return SeasonalDetailsHiscore()
