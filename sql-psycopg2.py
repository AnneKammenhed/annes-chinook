import psycopg2


#connect to chinook-database
connection = psycopg2.connect(database="chinook")


#build a cursor object of the database(same as array in javascript)
cursor = connection.cursor()


#Query 1 - select all records from the "Artist" table
#cursor.execute('SELECT * FROM "Artist"')

#Query 2 - select the Name column from the Artist table
#cursor.execute('SELECT "Name" FROM "Artist"')

#Query 3 - select "Black Sabbath" from the Artists table
#cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Black Sabbath"])

#Query 4 - select "Queen" from the Artists table
#cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

#Query 5 - select only albums with ArtistId 12 from the "Album" table
cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [12])

#Query 6 - select all tracks where the composer is Queen
#cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])


#fetch results(multiple)
results = cursor.fetchall()


#fetch results(single)
#results = cursor.fetchone()

#close the connection
connection.close()

#print results
for result in results:
    print(result)