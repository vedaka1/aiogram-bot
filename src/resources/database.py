import traceback
import psycopg2
from psycopg2.extensions import register_type, UNICODE
from resources.config import DB


def connection_db():
    global cur, conn
    try:
        register_type(UNICODE)
        conn = psycopg2.connect(DB)
        cur = conn.cursor()
    except:
        print(traceback.format_exc())

def close_connection():
    cur.close()
    conn.close()


class Database:
    """Class for work with database"""
    def add_user(self, user_id, username):
        """Adds a user to the database"""
        connection_db()
        cur.callproc("tg_bot.add_user", [user_id, username])
        conn.commit()
        close_connection()

    def set_echo_mode(self, user_id, mode):
        """Sets the user echo mode"""
        connection_db()
        cur.callproc("tg_bot.set_echo_mode", [user_id, mode])
        conn.commit()
        close_connection()

    def get_user_mode(self, user_id):
        """Gets the mode from the database"""
        connection_db()
        cur.callproc("tg_bot.get_user_mode", [user_id])
        mode = cur.fetchone()
        conn.commit()
        close_connection()
        return mode[0]
    
    def get_last_users(self):
        connection_db()
        cur.execute("select * from tg_bot.users where last_use is not null")
        users = cur.fetchall()
        result = []
        for user in users:
            result.append(
                {
                    "username": user[4],
                    "last_use": user[5].strftime("%Y-%m-%d %H:%M")
                }
            )
        result = sorted(result, key=lambda user: user["last_use"], reverse=True)
        return result
    
    # def add_user_messages(self, user_id, messages):
    #     connection_db()
    #     cur.callproc("tg_bot.add_user_messages", [user_id, Json(messages)])
    #     conn.commit()
    #     close_connection()

    # def get_user_messages(self, user_id):
    #     connection_db()
    #     cur.callproc("tg_bot.get_user_messages", [user_id])
    #     messages = cur.fetchone()
    #     conn.commit()
    #     close_connection()
    #     return messages[0]