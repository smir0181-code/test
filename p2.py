import sqlite3

conn=sqlite3.connect('database.db')
cursor=conn.cursor()

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT NOT NULL,
#         password TEXT NOT NULL
#     )
# ''')
# users=[
#     ('user1', 'password1'),
#     ('user2', 'password2'),
#     ('Галина', 'Крвмова')
# ]
# cursor.executemany("INSERT INTO users (username, password) VALUES (?, ?)", users)
# #cursor.execute("INSERT INTO users (username, password) VALUES (?,?)",('user2','password2'))
users=cursor.execute("DELETE FROM users WHERE id=1")
# users=cursor.fetchall()
# print(*users,sep='\n')
# for user in users:
#     print(user[1])

conn.commit()
# print("Данные добавлены в базу данных")