import oracledb
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
    
def get_user(t_user):
    cursor = check_conn()
    sql = cursor.execute("select * from st_user where u_id=:t_id", t_id=t_user).fetchone()
    print(sql)