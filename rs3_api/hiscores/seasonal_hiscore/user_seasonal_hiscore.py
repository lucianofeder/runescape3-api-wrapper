from dataclasses import dataclass, field
from typing import List

import requests

from rs3_api.hiscores.exceptions import UserNotFoundException
from rs3_api.hiscores.types import UserSeason
from rs3_api.utils.const import BASE_URL


@dataclass
class UserSeasonalHiscore:
    __api_data: str = field(default='', repr=False)

    def get_season(self, username: str, archived: bool = False) -> List[UserSeason]:
        is_archived = '&status=archived' if archived else ''
        if not self.__api_data:
            res = requests.get(f'{BASE_URL}/m=temp-hiscores/getRankings.json?player={username + is_archived}')
            if res.status_code >= 400:
                raise UserNotFoundException(username)
        return [UserSeason(
            start_date=data.get('startDate'),
            end_date=data.get('endDate'),
            hiscore_id=data.get('hiscore_id'),
            rank=data.get('rank'),
            score_formatted=data.get('score_formatted'),
            score_raw=data.get('score_raw'),
            title=data.get('title')
        ) for data in res.json()]