import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

cur.executescript('''
drop table if exists Artist;
drop table if exists Genre;
drop table if exists Album;
drop table if exists Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);

''')

def lookup(entry, key):
    found = False
    for child in entry:
        if found: return child.text
        if child.tag == 'key' and child.text == key:
            found = True 
    return None

filename = input('Enter File Name:')
tree = ET.parse(filename)

all = tree.findall('dict/dict/dict')
for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : continue
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    genre = lookup(entry, 'Genre')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    
    if name is None or artist is None or album is None or genre is None: 
        continue

    cur.execute('insert or ignore into Artist(name) values(?)',(artist,))
    cur.execute('select id from Artist where name = ?',(artist,))
    artist_id = cur.fetchone()[0]
    
    cur.execute('insert or ignore into Genre(name) values(?)',(genre,))
    cur.execute('select id from Genre where name = ?',(genre,))
    genre_id = cur.fetchone()[0]

    cur.execute('insert or ignore into Album(artist_id,title) values(?,?)',(artist_id,album))
    cur.execute('select id from Album where title = ?',(album,))
    album_id = cur.fetchone()[0]

    cur.execute('insert or replace into Track(title, album_id, genre_id, len, rating, count) values(?,?,?,?,?,?)',(name,album_id,genre_id,length,rating,count))
    
    conn.commit()