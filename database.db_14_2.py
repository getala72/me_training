# Задача "Средний баланс пользователя":

# Для решения этой задачи вам понадобится решение предыдущей.

# Для решения необходимо дополнить существующий код:

# Удалите из базы данных not_telegram.db запись с id = 6.
# Подсчитать общее количество записей.
# Посчитать сумму всех балансов.
# Вывести в консоль средний баланс всех пользователя.

from sqlite3 import connect

conn = connect('not_telegram.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
    )
''')

for i in range (1,11):
    cursor.execute('''
        INSERT INTO Users(
        username,
        email,
        age,
        balance )
        VALUES (?,?,?,?)''', (f"User{i}",f'example{i}@gmail.com',f'{i}0','1000'))



for i in range (1,11):
    if not (i-1) % 2:
        cursor.execute('''UPDATE Users SET balance=500 WHERE id = ?''',(i,))



for i in range (1,11):
    if not (i-1) % 3:
        cursor.execute('''DELETE FROM Users WHERE id = ?''',(i,))

cursor.execute('''DELETE FROM Users WHERE id = ?''',(6,))
cursor.execute('''SELECT COUNT(*) FROM Users''')
total_users=cursor.fetchone()[0]
cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

cursor.execute('''SELECT SUM(balance) FROM Users''')
all_balances=cursor.fetchone()[0]


# Пример результата выполнения программы:

# Выполняемый код:

# # Код из предыдущего задания

# # Удаление пользователя с id=6

# # Подсчёт кол-ва всех пользователей

# # Подсчёт суммы всех балансов

print(all_balances / total_users)

conn.close()



# Вывод на консоль:

# 700.0

