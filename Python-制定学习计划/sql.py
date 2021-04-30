import sqlite3
conn = sqlite3.connect('mark.db')
conn.execute("CREATE TABLE mark (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")
conn.execute("INSERT INTO mark (task,status) VALUES ('明天复习Java哦',1)")
conn.execute("INSERT INTO mark (task,status) VALUES ('每天晚上坚持一个罗翔法律知识哦',1)")
conn.execute("INSERT INTO mark (task,status) VALUES ('今天笑了吗',0)")
conn.commit()