from app import conn

conn.execute("CREATE TABLE IF NOT EXISTS courses(course_id TEXT PRIMARY KEY, coursedesc TEXT)")
cur =  conn.cursor()

conn.execute('CREATE TABLE IF NOT EXISTS studInfo(idno TEXT PRIMARY KEY , firstn TEXT, midname TEXT,lastn TEXT,'
             ' gnder TEXT, crse TEXT, yrlevel TEXT, FOREIGN KEY(crse) REFERENCES courses(course_id))')
conn.execute("CREATE VIEW IF NOT EXISTS joinedInfo AS SELECT course_id, idno, firstn, midname,lastn,"
             " gnder, coursedesc, yrlevel FROM studInfo CROSS JOIN courses WHERE courses.course_id = studInfo.crse")

conn.close()