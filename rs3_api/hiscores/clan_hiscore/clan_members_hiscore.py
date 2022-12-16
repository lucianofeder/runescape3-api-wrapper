from dataclasses import dataclass, field
from typing import List

import requests

from rs3_api.hiscores.exceptions import (ClanNotFoundException,
                                         UserNotFoundException)
from rs3_api.hiscores.types import ClanMember
from rs3_api.utils.const import BASE_URL


@dataclass
class ClanMembersHiscore:
    clan_name: str
    __api_data: str = field(default='', repr=False)
    __last_call: str = field(default='', repr=False)

    @property
    def members(self) -> List[ClanMember]:
        return self.__get_formatted_data(self.clan_name)

    def get_member(self, username: str) -> ClanMember:
        for member in self.members:
            if member.name.lower() == username.lower():
                return member
        raise UserNotFoundException(username)

    def __get_formatted_data(self, clan_name: str) -> List[ClanMember]:
        api_data = list(map(
            lambda data: data.split(','),
            self.__get_data(clan_name).split('\n')
        ))
        return [ClanMember(
            name=data[0],
            clan_rank=data[1],
            total_xp=int(data[2]),
            kills=int(data[3])
        ) for data in api_data[1:-1]]

    def __get_data(self, clan_name: str) -> str:
        current_call = f'clan_name: {clan_name}'
        if getattr(self, '__api_data', None) and current_call == self.__last_call:
            return self.__api_data
        res = requests.get(f'{BASE_URL}/m=clan-hiscores/members_lite.ws?clanName={clan_name}')
        if res.status_code == 200:
            self.__api_data = res.content.decode(errors='ignore')
            self.__last_call = current_call
            return self.__api_data
        raise ClanNotFoundException(clan_name)
