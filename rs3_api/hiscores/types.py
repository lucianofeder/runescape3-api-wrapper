from dataclasses import dataclass
from typing import Optional

from rs3_api.utils.const import Minigames, Skills


@dataclass
class Skill:
    name: Skills
    rank: int
    level: int
    experience: int

    @property
    def __xp_table(self):
        if self.name == Skills.OVERALL:
            raise NotImplementedError


@dataclass
class Minigame:
    name: Minigames
    rank: int
    total: int


@dataclass
class UserSeason:
    start_date: str
    end_date: Optional[str]
    rank: int
    title: str
    score_formatted: int
    score_raw: int
    hiscore_id: int
