import pymysql

conn = pymysql.connect(host='localhost',port=3306,user='root',password='a1234',db='user_information',charset='utf8')
curs = conn.cursor()

def sql_select():
    query = 'select * from user'
    curs.execute(query)
    rows = curs.fetchall()

    for row in rows:
        print(row)

def sql_insert():
    query = 'insert into user(id,pw,name) values("bbb","ccc","young")'
    curs.execute(query)

if __name__ =='__main__':
    sql_select()
    sql_insert()
    print('='*20)
    sql_select()
    print('=' * 20)

