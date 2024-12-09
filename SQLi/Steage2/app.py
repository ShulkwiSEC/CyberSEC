# login app
import sqlite3
import os


db = 'users.sql'

def init_db():
    try:
        global cur
        global conn
        conn = sqlite3.connect(db,check_same_thread=False)
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS users')
        qeruy = 'CREATE TABLE users(username,password,flag)'
        cur.execute(qeruy)
        conn.commit()
    except Exception as error:
        print(error)

def game_init():
    print('username/passsword/Flags Has Been Planted')
    try:
        username = f'administrator'
        password = str(int.from_bytes(os.urandom(10)))
        flag = "ShulkwiSEC{" +str(int.from_bytes(os.urandom(40)))+ "}"
        qeruy = "INSERT INTO users(username,password,flag) VALUES(?,?,?)"
        cur.execute(qeruy,(username,password,flag))
        conn.commit()
        return True
    except Exception as error:
        print(f'GAME_INIT {error}')
        return False

def login(username,password):
    try:
        qeruy = "SELECT flag FROM users WHERE username='%s' AND password='%s'" % (username,password)
        return cur.execute(qeruy).fetchone()
    except Exception as error:
        # print(error)
        return []


def main():
    init_db()
    game_init()
    totla_attempt = 100
    for i in range(totla_attempt):
        username = input('username: ')
        password = input('password: ')
        resp = login(username,password)
        if not resp:
            print('Not Found\n')
        else:
            print(f'Congraltion !!! here is your flag => {resp[0]}')
            print('Bye !')
            exit(1)
        print(f'{totla_attempt - i} attempts left\n')

main()