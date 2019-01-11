import pymysql

def get_conn(db):
    return pymysql.connect(
        host = 'localhost',
        user='dooo',
        password = 'dltkrtjd',
        port = 3306,
        db=db
        charset = 'utf8'
    )


conn_dooodb = get_conn('dooodb')
    
row = 0

with conn_dooodb:
    cur = conn_dooodb.cursor()
    cnt = "select count(*) from Subject"
    sql = "select id, name, prof, classroom from Subject"
    cur.execute(sql)
    row = cur.fetchall()

print (row)

conn_dadb = pymysql.connect(
    host = 'localhost',
    user = 'dooo',
    password = 'dltkrtjd',
    port = 3306,
    db = 'dadb',
    charset = 'utf8'
)

with conn_dooodb:
    cur = conn_dooodb.cursor()
    cur.execute('truncate table Subject')
    sql = "insert into Subject(id,name, prof, classroom) values(%s, %s, %s, %s)
    cur.executemany(sql, rows)
    print("AffecedRowCount is", cur.rowcout)
    conn_dadb.commit()
