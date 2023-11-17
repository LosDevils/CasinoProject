from src.database.models.user import OrmUser
from src.utils.repository import SQLAlchemyRepository
from src.adapters.user_adapter import UserAdapter


class UserRepository(SQLAlchemyRepository):
    model = OrmUser
    adapter = UserAdapter()
