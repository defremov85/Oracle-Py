__author__ = 'defremov85'

import cx_Oracle

def truncate_table():
    """Function to get data from Read-Only Oracle DB and paste it to Read-Write Oracle DB"""
    #Connection and Query details - Destination
    db_dest_connection = cx_Oracle.connect('django/django@192.168.1.201/xe')

    #db_dest_connection = cx_Oracle.connect('%s' % dest_creds)
    cursorTruncate = db_dest_connection.cursor()

    #Prepare TRUNCATE query
    truncate_query = "TRUNCATE TABLE tools"

    #Execute and commit query
    cursorTruncate.execute(truncate_query)
    db_dest_connection.commit()

    #Close cursorInsert and close connection to Destination DB
    cursorTruncate.close()
    db_dest_connection.close()

truncate_table()