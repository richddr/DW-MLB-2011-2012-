import psycopg2
import sys
import re
import MySQLdb as mdb

def PostgreSQL(query):	

	con = psycopg2.connect(database='postgres', user='postgres')

	cur = con.cursor()

	cur.execute(query)

	con.commit()
	try:
		return cur.fetchall()
	except:
		return None


PlayerQueries = open('../Queries/Player_Queries.txt', 'r')

for query in PlayerQueries:
	PostgreSQL(query);


BatQueries = open('../Queries/Batting_Queries.txt', 'r')

for query in BatQueries:
	PostgreSQL(query);

BatQueries = open('../Queries/Batting_Queries2011.txt', 'r')

for query in BatQueries:
	PostgreSQL(query);



FieldQueries = open('../Queries/Fielding_Queries.txt', 'r')

for query in FieldQueries:
	PostgreSQL(query);

FieldQueries = open('../Queries/Fielding_Queries2011.txt', 'r')

for query in FieldQueries:
	PostgreSQL(query);



PitchQueries = open('../Queries/Pitching_Queries.txt', 'r')

for query in PitchQueries:
	print query
	PostgreSQL(query);

PitchQueries = open('../Queries/Pitching_Queries2011.txt', 'r')

for query in PitchQueries:
	PostgreSQL(query);