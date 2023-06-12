import oracledb
import random
import tgbot.config as config
import datetime

today = datetime.date.today()

def check_conn():
    try:
        config.cursor.execute("select sysdate from dual").fetchone()
        return config.cursor
    except oracledb.DatabaseError or oracledb.OperationalError:
        print("БД - ошибка связи")
        conn = oracledb.connect(user=config.DbConfig.user, password=config.DbConfig.password, dsn=config.DbConfig.host+config.DbConfig.database)
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
    cursor.execute("insert into st_user (u_id, pwd, def_lang, is_admin, tg_name, login)"
                   "values(:u_id, :pwd, 'RU', 0, :tg_name, :login)", [contact["user_id"], pwd, contact["first_name"], contact["phone_number"]])
    cursor.execute("insert into wt_enter_counter(u_id, date_change_pwd, counter)"
                   "values (:u_id, :t_date, 0)", [contact["user_id"], today])
    cursor.execute("commit")
    return pwd

def upd_pwd(u_id):
    cursor = check_conn()
    pwd = generate_password()
    cursor.execute("update st_user set pwd = :pwd where u_id=:u_id", [pwd, u_id])
    cursor.execute("update wt_enter_counter set date_change_pwd = :t_date, counter = 1 where u_id = :u_id", [today, u_id])
    cursor.execute("commit")
    return pwd