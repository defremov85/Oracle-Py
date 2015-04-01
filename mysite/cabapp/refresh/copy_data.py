__author__ = 'defremov85'

# Import Oracle, Datetime and SafeConfigParser modules
import cx_Oracle
import datetime
from ConfigParser import SafeConfigParser

def copy_data():
    """Function to get data from Read-Only Oracle DB and paste it to Read-Write Oracle DB"""
    #A list to store a separate query results to modify it
    gcm_list = []

    #Default Action field value
    action = "''"

    #Default Flag field value
    flag = '0'

    """#Fetching credentials from db_connect.conf file
    config = SafeConfigParser()
    config.read('db_connect.conf')

    source_user = '"' + config.get('Source Database', 'source_user') + '"'
    source_pass = '"' + config.get('Source Database', 'source_pass') + '"'
    source_creds = "'" + config.get('Source Database', 'source_user') + '/' + config.get('Source Database', 'source_pass') \
               + '@' + config.get('Source Database', 'source_host') + '/' + config.get('Source Database', 'source_sid') + "'"
    #dsnStr = 'cx_Oracle.makedsn("192.168.1.201", "1521", "xe")'
    #print '%s' % dsnStr

    dest_creds = "'" + config.get('Destination Database', 'dest_user') + '/' + config.get('Destination Database', 'dest_pass') \
               + '@' + config.get('Destination Database', 'dest_host') + '/' + config.get('Destination Database', 'dest_sid') + "'"

    #abc = '"getdata", "getdata", cx_Oracle.makedsn("192.168.1.201", "1521", "xe")'
    #print "{0}".format(abc)
    #print abc"""

    #Connection and Query details - Source
    db_source_connection = cx_Oracle.connect('getdata/getdata@192.168.1.201/xe')
    #db_source_connection = cx_Oracle.connect(source_creds)
    #db_source_connection = cx_Oracle.connect("getdata", "getdata", cx_Oracle.makedsn("192.168.1.201", "1521", "xe"))
    #db_source_connection = cx_Oracle.Connection("{0}".format(abc), dsnStr)
    #db_source_connection = cx_Oracle.connect(abc)
    cursorGet = db_source_connection.cursor()
    cursorGet.execute("select * from GETDATA.GCM")

    #Connection and Query details - Destination
    db_dest_connection = cx_Oracle.connect('django/django@192.168.1.201/xe')
    #db_dest_connection = cx_Oracle.connect('%s' % dest_creds)
    cursorInsert = db_dest_connection.cursor()

    #Query to retrieve original data

    #Modifying query results to have a correct date format
    for i in cursorGet:
        for item in i:
            if type(item) == datetime.datetime:
                dt = item.strftime("%Y-%m-%d %H:%M:%S.%f")
                gcm_list.append(dt)
            else:
                gcm_list.append(item)

    #Creating a list with modified results - list to store modified query results from Read-Only DB
    gcm_results_list = map(list, zip(*[iter(gcm_list)] * len(i)))

    #Close cursorGet and close connection to Source DB
    cursorGet.close()
    db_source_connection.close()

    #Preparing a query before actual INSERT
    for ins_statement in gcm_results_list:
        ins_statement[5] = "TO_TIMESTAMP('" + ins_statement[5] + "', 'YYYY-MM-DD HH24:MI:SS.FF6')"
        ins_statement[6] = "TO_TIMESTAMP('" + ins_statement[6] + "', 'YYYY-MM-DD HH24:MI:SS.FF6')"
        ins_statement.append(action)
        ins_statement.append(flag)
        query = "insert into TOOLS (GCMID,URGENCY,IMPLEMENTER_GROUP,APPROVER_GROUP,CI_LIST,CREATED_DATE,PLANNED_DATE,ACTION,FLAG) VALUES (%s)" % ins_statement
        query = query.replace("[", "")
        query = query.replace("]", "")
        query = query.replace("\"", "")

        #Execute and commit query
        cursorInsert.execute(query)
        db_dest_connection.commit()

    #Close cursorInsert and close connection to Destination DB
    cursorInsert.close()
    db_dest_connection.close()
"""
    filelog = open('output.log',mode='r+')
    dt = str(datetime.datetime.now()) + '\n'
    filelog.write('Call successful\n')
    filelog.write(dt)
    filelog.close()
"""
copy_data()