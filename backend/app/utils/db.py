import os
import psycopg2


def create_connection():
    try:
        return psycopg2.connect(database=os.environ('DB_NAME'),
                                user=os.environ('DB_USER'),
                                password=os.environ('DB_PASS'),
                                host=os.environ('DB_HOST'),
                                port=os.environ('DB_PORT'))
    except Exception as e:
        return {
            'status': 404,
            'errorMessage': e
        }
    

def create_cursor(conn):
    try:
        return conn.cursor()
    except Exception as e:
        return {
            'status': 404,
            'errorMessage': e
        }


def commit_to_db(conn):
    try:
        conn.commit()
    except Exception as e:
        return {
            'status': 404,
            'errorMessage': e
        }
    

def close_connection(conn):
    try:
        conn.close()
    except Exception as e:
        return {
            'status': 404,
            'errorMessage': e
        }

def execute_query(query, parameters=None):
    conn = create_connection()
    cur = create_cursor(conn)

    try:
        if parameters:
            cur.execute(query, parameters)
        else:
            cur.execute(query)
    except Exception as e:
        return {
            'status': 404,
            'errorMessage': e
        }
    commit_to_db(conn)
    close_connection(conn)


def fetch_all(cur):
    try:
        return cur.fetchall()
    except Exception as e:
        return {
            'status': 404,
            'errorMessage': e
        }


def fetch_one(cur):
    try:
        return cur.fetchone()
    except Exception as e:
        return {
            'status': 404,
            'errorMessage': e
        }


def get_all_results(query, parameters=None):
    conn = create_connection()
    cur = create_cursor(conn)

    try:
        if parameters:
            cur.execute(query, parameters)
        else:
            cur.execute(query)
    except Exception as e:
        return {
            'status': 404,
            'errorMessage': e
        }
    
    results = fetch_all(cur)
    close_connection(conn)

    if len(results) > 0:
        return results
    
    return None


def get_one_result(query, parameters=None):
    conn = create_connection()
    cur = create_cursor(conn)

    try:
        if parameters:
            cur.execute(query, parameters)
        else:
            cur.execute(query)
    except Exception as e:
        return {
            'status': 404,
            'errorMessage': e
        }
    
    results = fetch_one(cur)
    close_connection(conn)

    if results is not None:
        return results
    
    return None
    

