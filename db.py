import psycopg2


# Устанавливаем соединение с базой данных
conn = psycopg2.connect(dbname="postgres", 
                        user="postgres", 
                        password="1234", 
                        host="localhost")
cursor = conn.cursor()

# Выполняем SQL-запрос для получения данных из таблицы
cursor.execute("select count, data from git where lang = 'Php' order by data")

# Получаем все строки результата
rows = cursor.fetchall()

# Выводим полученные данные
for row in rows:
    print(row)

# Закрываем курсор и соединение
cursor.close()
conn.close()