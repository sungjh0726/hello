 sql_job_history = '''select employee_id, start_date, end_date, job_id, department_id from Job_history'''
   cursor.execute(sql_job_history)
   job_history = cursor.fetchall()
 
 
 
 
 cur.execute("drop table if exists Job_history")
    job_history_create = '''create table Job_history(
                    employee_id int unsigned not null ,
                    start_date date not null ,
                    end_date date not null,
                    job_id varchar(10) not null,
                    department_id smallint(4),
                    primary key(employee_id, start_date)
                   );'''

   cur.execute(job_history_create)
   job_history_insert = '''insert into Job_history(employee_id, start_date, end_date, job_id, department_id)
                   values(%s, %s, %s, %s)'''
   cur.executemany(job_history_insert, job_history)


   print("AffectedRows-->", cur.rowcount)


   conn_dadb.commit()