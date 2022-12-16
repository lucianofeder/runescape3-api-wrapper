class UserNotFoundException(Exception):
    def __init__(self, username: str) -> None:
        self.message = f'User "{username} "was not found'


class ClanNotFoundException(Exception):
    def __init__(self, clan_name: str) -> None:
        self.message = f'Clan "{clan_name} "was not found'
