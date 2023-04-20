import oracledb
import random
import tgbot.config as config

#from ..bot import logger

def check_conn():
    try:
        config.cursor.execute("select sysdate from dual").fetchone()
        return config.cursor
    except oracledb.DatabaseError or oracledb.OperationalError:
        print("БД - ошибка связи")
        conn = oracledb.connect(user=config.db.user, password=config.db.password, dsn=config.db.host+config.db.database)
        config.cursor = conn.cursor()
        return config.cursor

def generate_password():
    return random.randint(100000, 999999)
    
def get_user(t_user):
    cursor = check_conn()
    sql = cursor.execute("select * from st_user where u_id=:t_id", t_id=t_user).fetchone()
    return sql

def add_user(contact):
    cursor = check_conn()
    pwd = generate_password()
    cursor.execute("insert into st_user (u_id, pwd, def_lang, is_admin, tg_name)"
                   "values(:u_id, :pwd, 'RU', 0, :tg_name)", [contact["user_id"], pwd, contact["first_name"]])
    cursor.execute("commit")
    return pwd