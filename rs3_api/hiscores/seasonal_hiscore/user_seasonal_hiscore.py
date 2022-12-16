from dataclasses import dataclass, field
from typing import List

import requests

from rs3_api.hiscores.exceptions import UserNotFoundException
from rs3_api.hiscores.types import UserSeason
from rs3_api.utils.const import BASE_URL


@dataclass
class UserSeasonalHiscore:
    __api_data: dict = field(default_factory=dict, repr=False)
    __last_call: str = field(default='', repr=False)

    def get_season(self, username: str, archived: bool = False) -> List[UserSeason]:
        res = self.__get_data(username, archived)
        return [UserSeason(
            start_date=data.get('startDate'),
            end_date=data.get('endDate'),
            hiscore_id=data.get('hiscore_id'),
            rank=data.get('rank'),
            score_formatted=data.get('score_formatted'),
            score_raw=data.get('score_raw'),
            title=data.get('title')
        ) for data in res]

    def __get_data(self, username: str, archived: bool = False) -> dict:
        current_call = f'username: {username} - archived: {archived}'
        if getattr(self, '__api_data', None) and current_call == self.__last_call:
            return self.__api_data
        is_archived = '&status=archived' if archived else ''
        res = requests.get(f'{BASE_URL}/m=temp-hiscores/getRankings.json?player={username + is_archived}')
        if res.status_code >= 400:
            raise UserNotFoundException(username)
        self.__last_call = current_call
        self.__api_data = res.json()
        return self.__api_data
