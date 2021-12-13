import sqlite3
with sqlite3.connect('data.db') as connect:
    cursor = connect.cursor()

    id = input('아이디를 입력해주세요: ')

    sql = 'DELETE FROM topics WHERE id = ?'
    cursor.execute(sql, (id,))
    #튜플로 arg 받는 방법. 파이썬에서 1,로 쓰면 자동으로 (1)인 튜플로 써준다
