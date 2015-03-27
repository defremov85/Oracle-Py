__author__ = 'defremov'

import cx_Oracle
import datetime

def date_insert():
    gcm_results_list = []
    gcm_list = []

    #select gcmid,urgency,implementer_group,approver_group,ci_list,created_date,planned_date from gcm;

    db_connection = cx_Oracle.connect('reports/password@192.168.1.201/xe')
    cursor = db_connection.cursor()
    cursorInsert = db_connection.cursor()
    #cursor.execute("select * from GCM")




    ts = datetime.datetime(2015, 1, 22, 18, 33, 46)
    print ts
    cursor.prepare("INSERT INTO TOOLS (created_date) VALUES(:t_val)")
    cursor.setinputsizes(t_val=cx_Oracle.TIMESTAMP)
    cursor.setinputsizes(t_val=cx_Oracle.TIMESTAMP)
    cursor.execute(None, {'t_val':ts})
    cursor.close()
    db_connection.commit()

date_insert()
