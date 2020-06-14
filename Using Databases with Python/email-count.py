import sqlite3

conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()

cur.execute('drop table if exists Counts')
cur.execute('create table Counts(org TEXT, count INTEGER)')

filename = input('Enter File Name:')
fh = open(filename)

for line in fh:
    if not line.startswith('From:'): continue
    piece = line.split()
    org = piece[1].split('@')[1]

    cur.execute('select count from Counts where org = ?', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('insert into Counts(org, count) values(?, 1)', (org,))
    else:
        cur.execute('update Counts set count = count + 1 where org = ?', (org,))
    conn.commit()

statement = 'select org, count from Counts order by count DESC limit 10'
for row in cur.execute(statement):
    print(str(row[0]), row[1])
cur.close()