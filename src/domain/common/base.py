from abc import ABC, abstractmethod
from dataclasses import dataclass
from logging import Logger
from typing import Any, Generic, TypeVar

VT = TypeVar("VT", bound=Any)
LT = TypeVar("LT", bound=Logger)


@dataclass
class BaseTextModel(ABC):
    logger: LT

    @abstractmethod
    def create_message(self) -> dict[str, str]: ...

    @abstractmethod
    async def generate_response(self) -> str: ...


@dataclass
class BaseValueObject(ABC, Generic[VT]):
    value: VT

    def __post_init__(self):
        self.validate()

    @abstractmethod
    def validate(self): ...

    @abstractmethod
    def as_generic_type(self): ...
