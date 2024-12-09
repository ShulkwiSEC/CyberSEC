import sqlite3
import sys


db_name = 'search.db'


def int_db():
    global conn
    global cur
    conn = sqlite3.connect(db_name,check_same_thread=False)
    cur = conn.cursor()
    initdb = 'CREATE TABLE IF NOT EXISTS search_db(q)'
    cur.execute(initdb)
    conn.commit()


# SELECT q FROM search_db WHERE q = ''

def search(data):
    try:
        return cur.execute("SELECT q FROM search_db WHERE q = '%s'" % data).fetchone()
    except:
        return False


if __name__ == '__main__':
    int_db()
    dataToinsert = ['ahmed','omer','osman','abdo']
    for data in dataToinsert: 
        cur.execute("INSERT INTO search_db(q) VALUES(?)",(data,))
     
    if search(search(sys.argv[1])):
        print('Found')
    else:
        print('Not Found')