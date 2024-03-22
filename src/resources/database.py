import traceback
from contextlib import asynccontextmanager

import asyncpg

from resources.config import settings


class Database:
    """Class for work with database"""

    __db_schema = "tg_bot"
    __db_url = settings.DB_URL

    @classmethod
    @asynccontextmanager
    async def create_connection(cls):
        try:
            conn: asyncpg.connection.Connection = await asyncpg.connect(cls.__db_url)
            yield conn
        except:
            print(traceback.format_exc())
        finally:
            await conn.close()

    async def add_user(self, user_id, username) -> None:
        """Adds a user to the database"""
        async with self.create_connection() as conn:
            await conn.execute(
                f"select {self.__db_schema}.add_user({user_id}, '{username}')"
            )

    async def set_echo_mode(self, user_id, mode) -> None:
        """Sets the user echo mode"""
        async with self.create_connection() as conn:
            await conn.execute(
                f"select {self.__db_schema}.set_echo_mode({user_id}, {mode})"
            )

    async def get_user_mode(self, user_id) -> bool:
        """Gets the mode from the database"""
        async with self.create_connection() as conn:
            result = await conn.fetchval(
                f"select {self.__db_schema}.get_user_mode({user_id})"
            )
            return result

    async def get_last_users(self) -> list:
        async with self.create_connection() as conn:
            users = await conn.fetch(
                f"select * from {self.__db_schema}.users where last_use is not null"
            )
            result = []
            for user in users:
                result.append(
                    {
                        "username": user[4],
                        "last_use": user[5].strftime("%Y-%m-%d %H:%M"),
                    }
                )
            result = sorted(result, key=lambda user: user["last_use"], reverse=True)
            return result


db = Database()
