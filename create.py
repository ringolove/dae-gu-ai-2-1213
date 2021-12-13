import sqlite3
# connect = sqlite3.connect('data.db')
with sqlite3.connect('data.db') as connect:
    cursor = connect.cursor()

    title = input('제목을 알려주세요: ')
    body = input('본문을 알려주세요: ')

    sql = 'INSERT INTO topics(title, body) VALUES(?,?)'
    cursor.execute(sql, (title, body))
        
    print('id', cursor.lastrowid)