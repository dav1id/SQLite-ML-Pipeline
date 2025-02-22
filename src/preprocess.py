'''
Processing data from sql database, here I'll generate and create the sample database,
and clean it up. Then I'll add some more to it later!
'''
import csv 
import sqlite3
import random as rand

con = sqlite3.connect("sampleDatabase.db")
cobj = con.cursor()

cobj.execute('''
             CREATE TABLE IF NOT EXISTS sampleDatabase(
             Prediction1 TEXT NOT NULL,
             Prediction2 TEXT NOT NULL,
             Prediction3 TEXT NOT NULL 
             );
             '''
             )

cobj.execute('''INSERT INTO sampleDatabase VALUES('P1', 'P2', 'P3');''')
con.commit()

def createTestCases(incr, cursor):
    for i in range(incr):
        text = """
            INSERT INTO sampleDatabase VALUES('{0}', '{1}', '{2}');
            """.format(rand.randint(1,50), rand.randint(1,50), rand.randint(1,50))
        cursor.execute(text)
    con.commit() #Commit to sql db 


#createTestCases(20, cobj)
statement = '''SELECT * FROM sampleDatabase'''
cobj.execute(statement)

rows = cobj.fetchall()

if (rows):
    for text in (cobj.fetchall()):
        print(text)
    print('Fetched rows!')
else:
    print("Rows not generated")

