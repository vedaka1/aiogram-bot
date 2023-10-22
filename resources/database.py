from resources.config import DB
import psycopg2, traceback
from psycopg2.extensions import register_type, UNICODE


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
    
    def add_user(self, user_id, username):
        connection_db()
        cur.callproc("tg_bot.add_user", [user_id, username])
        conn.commit()
        close_connection()

    def set_echo_mode(self, user_id, mode):
        connection_db()
        cur.callproc("tg_bot.set_echo_mode", [user_id, mode])
        conn.commit()
        close_connection()

    def get_user_mode(self, user_id):
        connection_db()
        cur.callproc("tg_bot.get_user_mode", [user_id])
        mode = cur.fetchone()
        close_connection()
        return mode[0]
    
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