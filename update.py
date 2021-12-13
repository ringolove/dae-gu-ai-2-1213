import sqlite3
with sqlite3.connect('data.db') as connect:
    cursor = connect.cursor()
    id = input('업데이트하려는 아이디를 알려주세요: ')
    sql = 'SELECT id, title, body FROM topics WHERE id = ?'
    cursor.execute(sql, (id,))
    row = cursor.fetchone()
    title = row[1]
    body = row[2]
    input_title = input(f'제목({title}):' )
    input_body = input(f'본목({body}):' )
    
    sql = 'UPDATE topics SET title=?, body=?, WHERE=i?'
    cursor.execute(sql, (input_title, input_body, id))