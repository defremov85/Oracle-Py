__author__ = 'defremov85'

#Import Oracle and Datetime modules
import cx_Oracle
import datetime

def dbrib_data():
    gcm_results_list = []
    gcm_list = []

    db_connection = cx_Oracle.connect('reports/password@192.168.1.201/xe')
    cursor = db_connection.cursor()
    cursor.execute("select * from GCM")
    for i in cursor:
        for item in i:
            if type(item) == datetime.datetime:
                dt = item.strftime("%d %B %Y %I:%M%p")
                gcm_list.append(dt)
            else:
                gcm_list.append(item)
        #print datetime.datetime(2015, 3, 22, 18, 33, 46).isoformat(' ')
        gcm_results_list = map(list, zip(*[iter(gcm_list)]*len(i)))

    for gcm,urg,impl,appr,server,crt,start in gcm_results_list:
        value = gcm,urg,impl,appr,server,crt,start
        f.write(str(value) + '\n')
    cursor.close()
    db_connection.close()

def html_table():
    fw.write('<table border="1" style="width:100%">\n')
    fw.write(' <tr>\n')
    fw.write('  <th>GCMid</th>\n')
    fw.write('  <th>Urgency</th>\n')
    fw.write('  <th>Implementer Group</th>\n')
    fw.write('  <th>Approver Group</th>\n')
    fw.write('  <th>CI List</th>\n')
    fw.write('  <th>Created Date</th>\n')
    fw.write('  <th>Planned Date</th>\n')
    fw.write('  <th>Action?</th>\n')
    fw.write(' </tr>\n')
    for line in f:
        fw.write(' <tr>\n')
        for i in line.split(', '):
            i = i.replace("'","")
            i = i.replace("(","")
            i = i.replace(")","")
            i = i.replace("\n","")
            fw.write('  <td>' + i + '</td>\n')
        fw.write('<td><form><input type="text" name="action"></form></td>\n')
        fw.write(' </tr>\n')
    fw.write('</table>\n')

f = open('output.html','r+')
f.truncate(0)
dbrib_data()
f.close()

f = open('output.html','r')
fw = open('good_output.html','w')
fw.truncate(0)
html_table()
f.close()
fw.close()