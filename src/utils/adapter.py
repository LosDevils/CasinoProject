from abc import ABC, abstractmethod
from typing import Type


class IAdapter(ABC):

    @abstractmethod
    def to_orm_model(self, domain_model):
        raise NotImplementedError

    def to_domain_model(self, orm_model):
        raise NotImplementedError


class Adapter(IAdapter):
    __orm_model = None
    __domain_model = None

    def to_orm_model(self, domain_model) -> Type[__orm_model]:
        orm_model = self.__orm_model()
        attributes = vars(domain_model)
        for (attr_name, attr_value) in attributes.items():
            setattr(orm_model, attr_name, attr_value)
        return orm_model

    def to_domain_model(self, orm_model) -> Type[__domain_model]:
        domain_model = self.__domain_model()
        attributes = vars(orm_model)
        for (attr_name, attr_value) in attributes.items():
            setattr(domain_model, attr_name, attr_value)
        return domain_model
