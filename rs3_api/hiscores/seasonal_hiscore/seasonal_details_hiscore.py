from dataclasses import dataclass, field
from typing import List

import requests

from rs3_api.hiscores.types import SeasonalEvent
from rs3_api.utils.const import BASE_URL


@dataclass
class SeasonalDetailsHiscore:
    __api_data: dict = field(default_factory=dict, repr=False)
    __last_call: str = field(default='', repr=False)


    @property
    def current(self) -> List[SeasonalEvent]:
        return self.__get_formatted_data()

    @property
    def all(self) -> List[SeasonalEvent]:
        return self.__get_formatted_data(True)

    def __get_formatted_data(self, archived: bool = False) -> List[SeasonalEvent]:
        res = self.__get_data(archived)
        return [SeasonalEvent(
            start_date=data.get('startDate'),
            end_date=data.get('endDate'),
            days_running=data.get('daysRunning'),
            months_running=data.get('monthsRunning'),
            recurrence=data.get('recurrence'),
            title=data.get('title'),
            name=data.get('name'),
            description=data.get('description'),
            status=data.get('status'),
            type=data.get('type'),
            id=data.get('id')
        ) for data in res] 

    def __get_data(self, archived: bool = False) -> dict:
        current_call = f'archived: {archived}'
        if getattr(self, '__api_data', None) and current_call == self.__last_call:
            return self.__api_data
        is_archived = '?status=archived' if archived else ''
        res = requests.get(f'{BASE_URL}/m=temp-hiscores/getHiscoreDetails.json{is_archived}')
        self.__api_data = res.json()
        return self.__api_data
        