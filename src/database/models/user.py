from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, Boolean, BigInteger
from src.database.base import Base


class OrmUser(Base):
    __tablename__ = 'Users'

    user_id: Mapped[str] = mapped_column(BigInteger, primary_key=True, autoincrement=False)
    balance: Mapped[int] = mapped_column(Integer, default=0)
    is_banned: Mapped[Boolean] = mapped_column(Boolean, default=False)

    def __str__(self):
        return f"id: {self.user_id}, balance: {self.balance}, ban: {self.is_banned}"
