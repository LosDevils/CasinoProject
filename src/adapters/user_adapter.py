from src.utils.adapter import Adapter
from src.domain.models.user import DomainUser
from src.database.models.user import OrmUser


class UserAdapter(Adapter):
    __orm_model = OrmUser
    __domain_model = DomainUser

    def to_domain_model(self, orm_model: OrmUser) -> DomainUser:
        domain_model = self.__domain_model
        return domain_model(user_id=orm_model.user_id, balance=orm_model.balance, is_banned=orm_model.is_banned)

    def to_orm_model(self, domain_model: DomainUser) -> OrmUser:
        orm_model = self.__orm_model()
        orm_model.user_id = domain_model.user_id
        orm_model.balance = domain_model.balance
        orm_model.is_banned = domain_model.is_banned
        return orm_model
