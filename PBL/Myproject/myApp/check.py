from myApp.push import make_a_connection
def get_ids_of_databases():
    conn,cur=make_a_connection()
    q='select id from myapp_createddatabases where is_published=1'
    cur.execute(q)
    ids=[]
    for i in cur:
        ids.append(i[0])
    return ids
    conn.close()
def get_tables_which_published(ids):
    conn,cur=make_a_connection()
    for id in ids:
        q="select table_name from myapp_adding_branch where Cdid="+str(id)
        cur.execute(q)
        tables=[]
        for i in cur:
            tables.append(i[0])
    return tables
def search_result(rollno,dob,tables):
    conn,cur=make_a_connection( )
    q2="SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA =%s AND TABLE_NAME =%s ORDER BY ORDINAL_POSITION"
    for table in tables:
        q1=" select * from "+table+" where hallticket=%s and dob=%s"
        v1=(rollno,dob)
        cur.execute(q1,v1)
        fr=[i for i in cur]
        if len(fr)!=0:
            v2=('main',table)
            cur.execute(q2,v2)
            sub=[i for i in cur]     
            sb=[]
            for i in sub:
                sb.append(i[0])       
            return clean_result(list(fr[0]),sb)
        else:
            continue


def clean_result(fr,sub):
    final_values=fr[1:6]+fr[7:]
    final_keys=sub[1:6]+sub[7:]
    print(final_keys)
    print(final_values)
    final_data=dict(zip(final_keys,final_values))
    return final_data

    