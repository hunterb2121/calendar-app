import os
import psycopg2


def connect_database():
    try:
        return psycopg2.connect(database=os.environ('DB_NAME'),
                                user=os.environ('DB_USER'),
                                password=os.environ('DB_PASS'),
                                host=os.environ('DB_HOST'),
                                port=os.environ('DB_PORT'))
    except Exception as e:
        return {
            "status": 404,
            "errorMessage": e
        }  