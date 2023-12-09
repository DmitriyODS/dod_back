import psycopg2
from consts import PSQL_URL


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance


class PDB(metaclass=Singleton):
    def __init__(self):
        self.__conn = None
        if self.__conn is None:
            try:
                self.__conn = psycopg2.connect(PSQL_URL)
            except Exception as e:
                print("Ошибка подключения к БД:", e)

    def close_db(self):
        self.__conn.close()
        self.__conn = None

    def execute_fetchall(self, *args):
        with self.__conn:
            with self.__conn.cursor() as cur:
                cur.execute(*args)
                return cur.fetchall()

    def execute_fetchone(self, *args):
        with self.__conn:
            with self.__conn.cursor() as cur:
                cur.execute(*args)
                return cur.fetchone()
