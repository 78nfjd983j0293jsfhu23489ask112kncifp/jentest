import sqlite3
import hashlib
import uuid

DATABASE="./details.db"

def getDB():
    global DATABASE
    try:
        conn = sqlite3.connect(DATABASE)
    except Exception as e:
        print(e)
    return conn

def enumerateQuery(query):
    cur = getDB().execute(query)
    rv = cur.fetchall()
    cur.close()
    return rv

def executeQuery(connection,query):
    try:
        c = connection.cursor()
        c.execute(query)
        c.close()
    except Exception as e:
        print(e)
    return

def insertQuery(connection,query,data):
    try:
        c = connection.cursor()
        c.execute(query,data)
        connection.commit()
        c.close()
    except Exception as e:
        print(e)
    return


# create if tables and whole database not exists
def initDB():
    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        uid text PRIMARY KEY,
                                        username text NOT NULL,
                                        password text NOT NULL,
                                        badgeID text
                                    ); """

    sql_create_data_table = """CREATE TABLE IF NOT EXISTS data (
                                       dID        text NOT NULL,
                                       type       text NOT NULL,
                                       prediction text ,
                                       patientNameSurname text 
                                );"""

    conn = getDB()

    # create tables
    if conn is not None:
        executeQuery(conn, sql_create_users_table)
        executeQuery(conn, sql_create_data_table)
    else:
        print("Error! cannot create the database connection.")


def checkLoginState(request):
    for user in enumerateQuery('select * from users'):
        if(user[0]==request.cookies.get("uid")):
            return True
    return False

def addData(dID,type_,prediction,patientNameSurname):
    query=''' INSERT INTO data(dID,type,prediction,patientNameSurname)
              VALUES(?,?,?,?) '''
    conn=getDB()
    if conn!=None:
        insertQuery(conn,query,(dID,type_,prediction,patientNameSurname))
    return

def addUser(username,badgeID,password):
    query=''' INSERT INTO users(uid,username,password,badgeID)
              VALUES(?,?,?,?) '''
    conn=getDB()
    if conn!=None:
        print("INSERTING TO DB")
        insertQuery(conn,query,(str(uuid.uuid4()),username,str(hashlib.md5(password.encode("utf-8")).hexdigest()),badgeID))
    return

def getDetails(dID):
    for data in enumerateQuery('select * from data where dID='+"'{}'".format(dID)):
        return (data[1],data[2],data[3])
        
    return ("","","")

def checkLogin(username,password):
    password_hash=str(hashlib.md5(password.encode("utf-8")).hexdigest())
    for user in enumerateQuery('select * from users'):
        print(user)
        if(user[1]==username and user[2]==password_hash):
            return user
    return None

