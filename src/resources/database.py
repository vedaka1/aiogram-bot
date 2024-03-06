import traceback

import asyncpg

from resources.config import settings


class Database:
    """Class for work with database"""

    async def create_connection(self):
        try:
            conn = await asyncpg.connect(settings.DB_URL)
            return conn
        except:
            print(traceback.format_exc())

    async def add_user(self, user_id, username):
        """Adds a user to the database"""
        conn: asyncpg.connection.Connection = await self.create_connection()
        await conn.execute(f"select tg_bot.add_user({user_id}, '{username}')")
        await conn.close()

    async def set_echo_mode(self, user_id, mode):
        """Sets the user echo mode"""
        conn: asyncpg.connection.Connection = await self.create_connection()
        await conn.execute(f"select tg_bot.set_echo_mode({user_id}, {mode})")
        await conn.close()

    async def get_user_mode(self, user_id):
        """Gets the mode from the database"""
        conn: asyncpg.connection.Connection = await self.create_connection()
        result = await conn.fetchval(f"select tg_bot.get_user_mode({user_id})")
        await conn.close()
        return result

    async def get_last_users(self):
        conn: asyncpg.connection.Connection = await self.create_connection()
        users = await conn.fetch(
            "select * from tg_bot.users where last_use is not null"
        )
        await conn.close()
        result = []
        for user in users:
            result.append(
                {"username": user[4], "last_use": user[5].strftime("%Y-%m-%d %H:%M")}
            )
        result = sorted(result, key=lambda user: user["last_use"], reverse=True)
        return result
