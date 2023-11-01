import psycopg2
from config import *


try:
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        port=port
    )
except Exception as ex:
    print(f'[ERROR] Error while connecting to db: {ex}')
finally:
    pass
