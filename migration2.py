import cx_Oracle

connection = cx_Oracle.connect("hr", "hrpw", "localhost:1521/xe")
print(connection.version)

with connection:
   # cursor를 만들어줍니다
   cursor = connection.cursor()

   sql = '''select region_id, region_name from Regions'''

   #cursor.execute(sql, dept_id=30)

   cursor.execute(sql, (30,))

   rows = cursor.fetchall()

for row in rows:
   print(row)

   with myconn:
       cur = myconn.cursor()
       cur.execute("drop table if exists Regions")
       sql_crate = ''' 
        create table Regions(
            region_id smallint not null primary key,
            region_name varchar(36)
        )
       '''

       cur.execute(sql)

       sql_insert = "insert into Regions(region_id, region_name) values(%s, %s)"
       cur.executemany(sql_insert, rows)
       print("AffectedRowCount is", cur.rowcount)

