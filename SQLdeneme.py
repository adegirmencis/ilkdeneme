import json
import sqlite3

class jsonImport:

    filename:any

    def __init__(self,jsonfile):
        self.filename = jsonfile
        pass

    def getFilename(self):
        return self.filename

    def getUsers(self):
        with open(self.filename) as dosya:
            jsonRead = json.load(dosya)
            return jsonRead
            # for user in jsonRead:
            #     print(user)

class Crud(jsonImport):

    def __init__(self, sqldb):

        self.conn = sqlite3.connect(sqldb)
        self.cursor = self.conn.cursor()
        self.conn.execute("""CREATE TABLE IF NOT EXISTS users (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	email VARCHAR(50) UNIQUE,
	gender VARCHAR(50),
	age INTEGER
);""")

        self.conn.commit()

    def addUser(self, user):
        self.conn.execute("INSERT INTO users (first_name,last_name,email,gender,age) values (?,?,?,?,?,?)",(user["first_name"],user["last_name"],user["email"],user["gender"],user["age"]))
        self.conn.commit()
        pass

    def addUsers(self, users):
        self.cursor.executemany('INSERT INTO users (first_name,last_name,email,gender,age)  values (?,?,?,?,?)',users)
        self.conn.commit()
        pass

    def delUser(self,user_id):
        self.conn.execute("DELETE FROM users WHERE id=?",(user_id,))
        self.conn.commit()

    def getUser(self,user_id):
        cun = self.cursor.execute('SELECT * FROM users where id=?',(user_id,))
        print(cun.fetchone())
        self.conn.commit()

    def updateUser(self,user):
        """
        :param user:
        (6 parametre gelecek ve sıralaması alttaki yapıya uygun olacak)
        :return:
        """
        self.cursor.execute("UPDATE users SET first_name=?, last_name=?, email=?,gender=?,age=? WHERE id=?",user)
        self.conn.commit()

    def search(self,column,searchvalue,limit=0):

        if (column == "" or column =="id"):
            sqlek = "SELECT * FROM users WHERE id=?"
        elif(column=="first_name"):
            sqlek="SELECT * FROM users WHERE first_name=?"
        elif (column == "last_name"):
            sqlek="SELECT * FROM users WHERE last_name=?"
        elif (column == "email"):
            sqlek="SELECT * FROM users WHERE email=?"
        elif (column == "age"):
            sqlek="SELECT * FROM users WHERE age=?"
        elif (column == "gender"):
            sqlek="SELECT * FROM users WHERE gender=?"
        else:
            return False

        self.cursor.execute(sqlek,(searchvalue,))
        self.conn.commit()
        return self.cursor.fetchall()

    def search_BOZUK(self,column,searchvalue,like=False,limit=0):

        if (column == "" or column =="id"):
            if(like==False):
                sqlek = "SELECT * FROM users WHERE id=?"
            else:
                sqlek = "SELECT * FROM users WHERE id LIKE '%??%'"
        elif(column=="first_name"):
            if (like == False):
                sqlek="SELECT * FROM users WHERE first_name=?"
            else:
                sqlek = "SELECT * FROM users WHERE first_name like '%?%'"
        elif (column == "last_name"):
            if (like == False):
                sqlek="SELECT * FROM users WHERE last_name=?"
            else:
                sqlek = "SELECT * FROM users WHERE last_name like '%?%'"
        elif (column == "email"):
            if (like == False):
                sqlek="SELECT * FROM users WHERE email=?"
            else:
                sqlek = "SELECT * FROM users WHERE email like '%?%'"
        elif (column == "age"):
            if (like == False):
                sqlek="SELECT * FROM users WHERE age=?"
            else:
                sqlek = "SELECT * FROM users WHERE age like '%?%'"
        elif (column == "gender"):
            if (like == False):
                sqlek="SELECT * FROM users WHERE gender=?"
            else:
                sqlek = "SELECT * FROM users WHERE gender like '%?%'"

        self.cursor.execute(sqlek,(searchvalue,))
        self.conn.commit()
        return self.cursor.fetchall()


C = Crud("users.db")

UserJson = jsonImport("users.json")
Users = UserJson.getUsers()

search = C.search("last_name","Tez")
print(search)

# C.delUser(31)
# C.getUser(7)
# newUser =('Rowland', 'Clampton', 'rclampton1@addthis.com', 'Male', 47,7)
# C.updateUser(newUser)
# C.getUser(7)

# users = []
# for i in Users:
#     # print(i)
#     users.append((i["first_name"],i["last_name"],i["email"],i["gender"],i["age"]))
#
#
# print(users)
# C.addUsers(users)







# userdatas = [
# ("Aydın","Tez","adegirmencis@gmail.com","male","35"),
# ("Neslihan","Tez","adegirmencis@gmail.com","female","35"),
# ("Zülal Nisa","Tez","adegirmencis@gmail.com","female","9"),
# ("Elif Hüma","Tez","adegirmencis@gmail.com","female","5"),
# ("Aybüke Sare","Tez","adegirmencis@gmail.com","female","1")
# ]

# C.addUsers(userdatas)
