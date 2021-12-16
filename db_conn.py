import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

# def create_table(conn, create_table_sql):
#     try:
#         c = conn.cursor()
#         c.execute(create_table_sql)
#     except Error as e:
#         print(e)

if __name__ == '__main__':
    
    database = r"transaksi.db"
    conn = create_connection(database)
    
    # create table
    # sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS transaksi (
    #                                     id integer PRIMARY KEY AUTOINCREMENT,
    #                                     username text NOT NULL,
    #                                     invoice_code text NOT NULL,
    #                                     private_key integer NOT NULL
    #                                 ); """
    # if conn is not None:
    #     # create projects table
    #     create_table(conn, sql_create_projects_table)
    # else:
    #     print("Error! cannot create the database connection.")

    # Insert a row
    # sql = ''' INSERT INTO transaksi(username, invoice_code, private_key)
    #           VALUES('johndoe', 'INV/16-12-2021/101', 192788) '''
    # cur = conn.cursor()
    # cur.execute(sql)
    # conn.commit()

    # Select data
    cur = conn.cursor()
    cur.execute("SELECT private_key FROM transaksi WHERE username=? AND invoice_code=?", ('johndoe', 'INV/16-12-2021/101',))
    rows = cur.fetchone()
    print(rows[0])

    