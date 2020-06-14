'''
Once you have made the necessary changes to the program and it has been run successfully reading the above JSON data, run the following
SQL command:

SELECT hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X
'''

import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
);
''')

filename = input('Enter File Name:')
data = open(filename).read()
tree = json.loads(data)

for item in tree:
    name = item[0]
    title = item[1]
    role = item[2]
    cur.execute('insert or ignore into User(name) values(?) ',(name,))
    cur.execute('select id from User where name = ?',(name,))
    user_id = cur.fetchone()[0]

    cur.execute('insert or ignore into Course(title) values(?)', (title,))
    cur.execute('select id from Course where title = ?',(title,))
    course_id = cur.fetchone()[0]

    cur.execute('insert or ignore into Member(user_id, course_id, role) values(?,?,?)',(user_id,course_id,role))
conn.commit()
