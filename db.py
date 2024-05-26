import psycopg2

class DB:
    conn = ''
    cursor = ''

    def __init__(self):
        self.conn = psycopg2.connect(dbname="postgres", 
                            user="postgres", 
                            password="1234", 
                            host="localhost")
        self.cursor = self.conn.cursor()        

    # Закрываем курсор и соединение
    def closeDB(self):
        self.cursor.close()
        self.conn.close()

    ###

    def intoHH():
        pass

    def intoGit():
        pass

    ###
    
    def getGitByLang(self, variable):
        # query = "select lang, count, data from git where lang = %s order by data"
        query = "select count, data from git where lang = %s order by data"
        self.cursor.execute(query, (variable,))
        return self.cursor.fetchall()
    
    def getGitAllLastData(self):
        # query = "select lang, count, data from git where lang = %s order by data"
        query = "SELECT * FROM git WHERE data = (SELECT MAX(data) FROM git)"
        self.cursor.execute(query)
        return self.cursor.fetchall()


    ###
    
    def getHHAllLastData(self):
        # query = "select lang, count, data from git where lang = %s order by data"
        query = "SELECT * FROM hh WHERE data = (SELECT MAX(data) FROM hh)"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def getHHRegionLastData(self, variable):
        # query = "select lang, count, data from git where lang = %s order by data"
        query = "SELECT lang, vac, vacref, res, region, data FROM hh WHERE data = (SELECT MAX(data) FROM hh) and region = %s"
        self.cursor.execute(query, (variable,))
        return self.cursor.fetchall()
    
    def getHHLengRegionData(self, lang, region):
        # query = "select lang, count, data from git where lang = %s order by data"
        query = "SELECT vac, vacref, res, data FROM hh WHERE lang = %s and region = %s order by data"
        self.cursor.execute(query, (lang, region))
        return self.cursor.fetchall()

# db = DB()
# rows = db.getGitByLang('Php')
# rows = db.getHHLengAllData('php')
# db.closeDB()

# print(type(rows[0]))
# print(rows[0][1])
# Выводим полученные данные
# for row in rows:
    # print(row)
