import sqlite3
from bottle import route,run,template,request,error
import re
import requests
@route('/mark')
def mark_list():
    conn = sqlite3.connect('mark.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM mark WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()
    output = template('make_table',rows=result)
    return output

@route('/new',method='GET')
def new_task():
    if request.GET.save:
        new = request.GET.task.strip()
        conn = sqlite3.connect('mark.db')
        c = conn.cursor()
        c.execute("INSERT INTO mark (task,status) VALUES(?,?)",(new,1))
        new_id = c.lastrowid
        conn.commit()
        c.close()
        return '<p>Data was added successfully with ID of %s</p>' %new_id
    else:
        return template('new_task')

@route('/edit/<no:int>',method='GET')
def edit_item(no):
    if request.GET.save:
        edit = request.GET.task.strip()
        status = request.GET.status.strip()
        if status == 'open':
            status = 1
        else:
            status = 0
        conn = sqlite3.connect('mark.db')
        c = conn.cursor()
        c.execute("UPDATE mark SET task=?,status=? WHERE id LIKE ?",(edit,status,no))
        conn.commit()
        return '<p>Successfully submitted plan id: %s</p>' %no
    else:
        conn = sqlite3.connect('mark.db')
        c = conn.cursor()
        c.execute("SELECT task FROM mark WHERE id LIKE ?",(str(no)))
        cur_data = c.fetchone()
        return template('edit_task',old=cur_data,no=no)

@route('/json<json:re:[0-9]+>')
def show_json(json):
    conn = sqlite3.connect('mark.db')
    c = conn.cursor()
    c.execute("SELECT task FROM mark WHERE id LIKE ?",(json,))
    result = c.fetchall()
    c.close()
    if not result:
        return {'task': 'This item number does not exist'}
    else:
        return {'task': result[0]}

@error(404)
def mistake404(code):
    return 'Sorry,The page you are looking that was eaten by the dog'


run(reload=True,host='localhost',port=8889)