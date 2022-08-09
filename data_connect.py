import pymysql

connect = pymysql.connect(host="192.168.1.54",user="root",database="information",charset='utf8')

cur = connect.cursor()

sql = """create table bbb (
        id int(10) NOT NULL AUTO_INCREMENT,
        name varchar(20),
        age int(10),
        birthday varchar(20),
        height varchar(20),
        primary key (id)
        );"""

cur.execute(sql)

cur.close()

connect.commit()

connect.close()
