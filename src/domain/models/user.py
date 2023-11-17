class DomainUser:
    def __init__(self, user_id: int, balance: int = 0, is_banned: bool = False):
        self.user_id = user_id
        self.balance = balance
        self.is_banned = is_banned

    def __str__(self):
        return f"user_id: {self.user_id}, balance: {self.balance}, ban: {self.is_banned}"
