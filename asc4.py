import xml.etree.ElementTree as ET
import json
import sqlite3


# for assignment 2 of Using Database With Python

# conn = sqlite3.connect('emaildb.sqlite')
# cur = conn.cursor()

# cur.execute('''DROP TABLE IF EXISTS Counts''')
# cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')
# 
# fh = open('emaildb.txt')
# for line in fh:
#     if not line.startswith('From: ') : continue
#     pieces = line.split()
#     org = re.findall("\S+@(\S+)", pieces[1])
#     #print org
#     cur.execute('SELECT count FROM Counts WHERE org = ? ', (org[0], ))
#     row = cur.fetchone()
#     if row is None:
#         cur.execute('''INSERT INTO Counts (org, count) 
#                 VALUES ( ?, 1 )''', (org[0], ) )
#     else : 
#         cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', 
#             (org[0], ))
#     # This statement commits outstanding changes to disk each 
#     # time through the loop - the program can be made faster 
#     # by moving the commit so it runs only after the loop completes
# conn.commit()

# # https://www.sqlite.org/lang_select.html
# sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

# print
# print "Counts:"
# for row in cur.execute(sqlstr) :
#     print str(row[0]), row[1]

# cur.close()

# for assignment 3 of Using Database With Python

# conn = sqlite3.connect('trackdb.sqlite')
# cur = conn.cursor()

# # Make some fresh tables using executescript()
# cur.executescript('''
# DROP TABLE IF EXISTS Artist;
# DROP TABLE IF EXISTS Album;
# DROP TABLE IF EXISTS Genre;
# DROP TABLE IF EXISTS Track;

# CREATE TABLE Artist (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name    TEXT UNIQUE
# );

# CREATE TABLE Genre (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name    TEXT UNIQUE
# );

# CREATE TABLE Album (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     artist_id  INTEGER,
#     title   TEXT UNIQUE
# );

# CREATE TABLE Track (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     title TEXT  UNIQUE,
#     album_id  INTEGER,
#     genre_id  INTEGER,
#     len INTEGER, rating INTEGER, count INTEGER
# );
# ''')


# fname = raw_input('Enter file name: ')
# if ( len(fname) < 1 ) : fname = 'Library.xml'

# # <key>Track ID</key><integer>369</integer>
# # <key>Name</key><string>Another One Bites The Dust</string>
# # <key>Artist</key><string>Queen</string>
# def lookup(d, key):
#     found = False
#     for child in d:
#         if found : return child.text
#         if child.tag == 'key' and child.text == key :
#             found = True
#     return None

# stuff = ET.parse(fname)
# all = stuff.findall('dict/dict/dict')
# # print 'Dict count:', len(all)
# for entry in all:
#     if ( lookup(entry, 'Track ID') is None ) : continue

#     name = lookup(entry, 'Name')
#     artist = lookup(entry, 'Artist')
#     album = lookup(entry, 'Album')
#     genre = lookup(entry, 'Genre')
#     count = lookup(entry, 'Play Count')
#     rating = lookup(entry, 'Rating')
#     length = lookup(entry, 'Total Time')

#     if name is None or artist is None or album is None or genre is None: 
#         continue

#     # print name, artist, album, genre, count, rating, length

#     cur.execute('''INSERT OR IGNORE INTO Artist (name) 
#         VALUES ( ? )''', ( artist, ) )
#     cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
#     artist_id = cur.fetchone()[0]

#     cur.execute('''INSERT OR IGNORE INTO Genre (name) 
#         VALUES ( ? )''', ( genre, ) )
#     cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
#     genre_id = cur.fetchone()[0]

#     cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
#         VALUES ( ?, ? )''', ( album, artist_id ) )
#     cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
#     album_id = cur.fetchone()[0]

#     cur.execute('''INSERT OR REPLACE INTO Track
#         (title, album_id, genre_id, len, rating, count) 
#         VALUES ( ?, ?, ?, ?, ?, ?)''', 
#         ( name, album_id, genre_id, length, rating, count ) )

#     conn.commit()


# for assignment 4 of Using Database With Python

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some setup
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
)
''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'roster_data.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0];
    title = entry[1];
    role = entry[2];

    # print name, title

    cur.execute('''INSERT OR IGNORE INTO User (name) 
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title) 
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''', 
        ( user_id, course_id, role ) )

    conn.commit()
# for assignment 5 of Using Database With Python