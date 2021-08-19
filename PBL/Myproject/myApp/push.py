import pandas as pd 
import MySQLdb
def get_columns(path):
    df=pd.read_csv(path)
    return list(df.columns)
def make_a_connection():
    conn=MySQLdb.connect(host='localhost',user='root',passwd='waste@mysql80',database='main')
    cur=conn.cursor()
    return conn,cur
def create_a_table_in_database(table_name,path):
    l=get_columns(path)
    q='create table '+table_name+'('
    for i in l:
        if i.lower()=='sno':
            q+=i
            q+=" "
            q+="int,"
        elif i.lower()=='sgpa,':
            q+=i
            q+=" "
            q+="decimal(4,2)"
        elif i.lower()=='dob':
            q+=i 
            q+=" "
            q+="date,"
        else:
            q+=i
            q+=" "
            q+="varchar(10),"
    q+='primary key(hallticket))'
    conn,cur=make_a_connection()
    cur.execute(q)
    conn.close()
def push_data_to_table(path,t_name):
    df=pd.read_csv(path)
    r=int(df.shape[0])
    c=int(df.shape[1])
    q1='insert into '+t_name.lower()+' values'+'('+'%s,'*(c-1)+'%s)'
    conn,cur=make_a_connection()
    for i in range(r):
        v=tuple(df.iloc[i])
        cur.execute(q1,v)
        conn.commit()
    conn.close()


