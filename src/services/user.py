from src.utils.service import IService
from src.domain.models.user import DomainUser
from typing import Type


class UserService(IService):

    async def add_user(self, user: DomainUser) -> Type[DomainUser]:
        """
        :param user: Type[DomainUser]
        :return: Type[DomainUser] if success
        :return: sqlalchemy.exc.IntegrityError if error
        """

        user_dict = user.__dict__
        uow = self.uow
        async with uow:
            domain_user = await uow.user.add_one(user_dict)
            await uow.commit()
            return domain_user

    async def add_user_by_id(self, user_id: int) -> Type[DomainUser]:
        """
        :param user_id: int
        :return: Type[DomainUser] if success
        :return: sqlalchemy.exc.IntegrityError if error
        """
        user = DomainUser(user_id=user_id)
        user_dict = user.__dict__
        uow = self.uow
        async with uow:
            domain_user = await uow.user.add_one(user_dict)
            await uow.commit()
            return domain_user

    async def get_user(self, user_id: int) -> Type[DomainUser]:
        """
        :param user_id: int
        :return: Type[DomainUser] if success
        :return: sqlalchemy.exc.NoResultFound if error
        """
        uow = self.uow
        async with uow:
            domain_user = await uow.user.find_one(user_id=user_id)
            await uow.commit()
            return domain_user

# class UserService:
#     @staticmethod
#     async def add_user(uow: IUnitOfWork, user: DomainUser):
#         user_dict = user.__dict__
#         async with uow:
#             user_id = uow.user.add_one(user_dict)
#             await uow.commit()
#             return user_id
