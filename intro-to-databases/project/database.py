from psycopg2 import pool


connection_pool = pool.SimpleConnectionPool(1,
                                            1,
                                            user='postgres',
                                            password='chandu',
                                            database='learning',
                                            host='localhost',
                                            port='5433')


class ConnectionFromPool:
    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = connection_pool.getconn()
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        connection_pool.putconn(self.connection)