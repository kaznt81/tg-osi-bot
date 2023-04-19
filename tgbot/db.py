import oracledb
import config

#from tgbot.config import load_config
from bot import config, logger

def check_conn():
    try:
        config.cursor.execute("select sysdate from dual").fetchone()
        return config.cursor
    except oracledb.DatabaseError or oracledb.OperationalError:
        logger.info("БД - ошибка связи")
        conn = oracledb.connect(user=config.db.user, password=config.db.password, dsn=config.db.host+config.db.database)
            #user=load_config(".env").db.user, password=load_config(".env").db.password, dsn=load_config(".env").db.host+load_config(".env").db.database)
        config.cursor = conn.cursor()
        return config.cursor