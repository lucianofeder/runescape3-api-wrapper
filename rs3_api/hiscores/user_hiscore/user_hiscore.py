from dataclasses import dataclass, field
from typing import Dict, List, Optional

import requests

from rs3_api.hiscores.exceptions import UserNotFoundException
from rs3_api.hiscores.seasonal_hiscore import UserSeasonalHiscore
from rs3_api.hiscores.types import Minigame, Skill, UserSeason
from rs3_api.utils.const import BASE_URL, AccountTypes, Minigames, Skills


@dataclass
class UserHiscore:
    username: str
    account_type: Optional[AccountTypes]
    skills: Dict[Skills, Skill] = field(init=False)
    minigames: Dict[Minigames, Minigame] = field(init=False)

    __api_data: str = field(init=False, repr=False)
    __seasonal_hiscore: UserSeasonalHiscore = field(default_factory=lambda: UserSeasonalHiscore(), repr=False) 

    def __post_init__(self):
        if not self.account_type:
            user = self.__get_without_account_type()
        else:
            user = self.__get_user(self.account_type)
        if not user:
            raise UserNotFoundException(self.username)
        self.__process()

    def get_season(self, archived: bool = False) -> List[UserSeason]:
        return self.__seasonal_hiscore.get_season(self.username, archived)

    def __process(self):
        api_data = list(map(
            lambda data: data.split(','),
            self.__api_data.split('\n')
        ))
        self.skills = self.__get_skills(api_data),
        self.minigames = self.__get_minigames(api_data)
        return self

    def __get_user(self, account_type: AccountTypes) -> str:
        if getattr(self, '__api_data', None):
            return self.__api_data
        TYPE_URL = {
            AccountTypes.NORMAL.value: '/m=hiscore',
            AccountTypes.IRONMAN.value: '/m=hiscore_ironman',
            AccountTypes.HARDCORE.value: '/m=hiscore_hardcore_ironman'
        }
        res = requests.get(
            f'{BASE_URL+TYPE_URL[account_type]}/index_lite.ws?player={self.username}'
        )
        if res.status_code == 200:
            self.__api_data = res.content.decode()
            self.account_type = account_type
            return self.__api_data
        return ''

    def __get_without_account_type(self) -> Optional[str]:
        for type in reversed(AccountTypes):
            user = self.__get_user(type)
            if user:
                return user
        return None

    def __get_minigames(self, api_data: List[List[str]]) -> Dict[Minigames, Minigame]:
        starting_point = len(Skills)
        data = {}
        for i, minigame in enumerate(Minigames):
            pos = i + starting_point
            data[minigame.value] = Minigame(
                name=minigame.value,
                rank=int(api_data[pos][0]),
                total=int(api_data[pos][1])
            )
        return data

    def __get_skills(self, api_data: List[List[str]]) -> Dict[Skills, Skill]:
        data = {}
        for i, skill in enumerate(Skills):
            data[skill.value] = Skill(
                name=skill.value,
                rank=int(api_data[i][0]),
                level=int(api_data[i][1]),
                experience=int(api_data[i][2]),
            )
        return data
