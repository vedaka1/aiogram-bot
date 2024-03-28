from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class BaseUserRepository(ABC):
    @abstractmethod
    async def add_user(self) -> None: ...

    @abstractmethod
    async def set_echo_mode(self) -> None: ...

    @abstractmethod
    async def get_user_mode(self) -> bool: ...

    @abstractmethod
    async def get_last_users(self) -> list[dict[str, str]]: ...
