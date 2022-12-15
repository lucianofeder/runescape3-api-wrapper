class UserNotFoundException(Exception):
    def __init__(self, username: str) -> None:
        self.message = f'User "{username} "was not found'
