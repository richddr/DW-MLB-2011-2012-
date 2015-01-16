import psycopg2
import sys
import re
import MySQLdb as mdb
import datetime


def PostgreSQL(query):	

	con = psycopg2.connect(database='postgres', user='postgres')

	cur = con.cursor()

	cur.execute(query)

	con.commit()
	try:
		return cur.fetchall()
	except:
		return None


def MySQL(query):
	
	print query
	
	Mycon = mdb.connect('localhost', 'root', '1234', 'mysql');

	with Mycon:
		
		Mycur = Mycon.cursor()
		
		Mycur.execute(query)

		result =  Mycur.fetchall() 

		return list(result) if result != () else []
		

def difference(a, b):
	""" show whats in list b which isn't in list a """
	return list(set(b).difference(set(a))
)
def Populate_DIM(New_Data_Query, Dimension):
	new_data = PostgreSQL(New_Data_Query) 
	existing_data = MySQL("select * from " + Dimension)

	[MySQL("insert into " + Dimension + " values(" + ','.join("'" + str(dato).replace("'", "''") + "'" if type(dato) is str or type(dato) is datetime.date else str(dato) for dato in data ) + ")") for data in difference(existing_data, new_data)]


"""
# Creamos las tablas utilizando los queries leyendolos de un archivo.

Dimensiones = open('../Queries/Dimensional_Queries.txt', 'r')

for query in Dimensiones:
	MySQL(query)

"""
#Query_DIM_EQUIPOS = """select e.codigo, e.division, e.nombre_equipo, e.nombre_abreviado, e.nombre_estadio, l.codigo, l.nombre_liga, l.nombre_abreviado
#							 from ligas l, equipos e where e.liga_equipo=l.codigo"""

#Query_DIM_JUGADORES = """select codigo,nombre,nombre_preferido,apellido,jersey,posicion,bats, throws, height, weight_lb, born, birthcountry,highschool,college,debut
#	from jugadores"""

Query_FACT_BATEO = """select equipo , anio ,posicion,jugador, edad , games_pp , plate_appearances , at_bats , runs_sa , hits_sa ,doubles_sa , triples_sa 
, hr_sa , rbi , stolen_bases , caught_stealing , walks , strikeouts , hits_attacks ,obp,slg,ops,ops_plus , total_bases , grounded_dp , hbp , sacrifice_hits 
, sacrifice_flies , intentional_walks from BATEO_JUGADOR_EQUIPO"""

Query_FACT_PITCH = """select equipo , anio ,posicion, jugador, edad , wins , losses , wl_p , era , games_played , games_started , games_finished , complete_games , shutouts , saves , innings_pitched , hits 
, runs , earned_runs , home_runs , walks ,intentional_walks , strikeouts , hpb , balks , wild_pitches , batters_faced , era_plus , whip , h9 , hr9 , bb9 , so9 
,sobb from PITCHEO_JUGADOR_EQUIPO"""

Query_FACT_FIELD = """select equipo , anio,jugador , edad , games , games_started , complete_games , innings_played , defensive_chances , putouts , assists , errors , double_plays , fielding_percentage , 
rtot , rot_year , r_drs , r_drs_year , range_factor9 , rfg , passed_balls , wild_pitches 
, stolen_bases , caugh_stealing , caught_stealingp ,lgcps, pickoffs , pos_summary from FILDEO_JUGADOR_EQUIPO"""

#Populate_DIM(Query_DIM_EQUIPOS, 'DIM_EQUIPOS')
#Populate_DIM(Query_DIM_JUGADORES, 'DIM_JUGADORES')

Populate_DIM(Query_FACT_BATEO, 'FACT_BATEO')
Populate_DIM(Query_FACT_FIELD, 'FACT_FILDEO')
Populate_DIM(Query_FACT_PITCH, 'FACT_PITCHEO')
