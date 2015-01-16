import re
import psycopg2
import sys

Teams = {   'NYY' : 2,
            'MIL' : 26,
            'MIN' : 12,
            'MIA' : 19,
            'WSH' : 18,
            'ATL' : 17,
            'BOS' : 1,
            'DET' : 11,
            'CIN' : 29,
            'NYM' : 16,
            'BAL' : 4,
            'COL' : 21,
            'OAK' : 8,
            'TEX' : 9,
            'TOR' : 3,
            'SEA' : 7,
            'CLE' : 10,
            'PIT' : 30,
            'STL' : 27,
            'CHI' : 25,
            'CWS' : 13,
            'HOU' : 28,
            'ARI' : 20,
            'PHI' : 15,
            'SDP' : 22,
            'LAD' : 23,
            'LAA' : 6,
            'KCR' : 14,
            'SFG' : 24,
            'TBD' : 5 
}

def PostgreSQL(query):  

    con = psycopg2.connect(database='prueba', user='mike')

    cur = con.cursor()

    cur.execute(query)

    con.commit()
    try:
        return cur.fetchall()
    except:
        return None


file = open("../CSV/fielding2011.txt")
fileoutput = open('../Queries/Fielding_Queries2011.txt', 'w')
i = 874
year = "2011";
team_rep = "Z@ZZLE_X24Y";
team_db = ""

while 1:
    line = file.readline()
    if not line:
        break
    else:
        flag = False
        line_s = line.split(',')
        insert_l= "insert into FILDEO_JUGADOR_EQUIPO values( "+ str(i) +", "+ team_rep +", " + year

        for x in range(0, len(line_s)): 
            if(len(line_s[x]) == 0):
                line_s[x] = "0"
            while(not line_s[x][-1].isalnum()):
                line_s[x] = line_s[x][0: -1]
            if x == 0:
                #insert_l += ", 2"
                full_name = line_s[x].split(' ')
                full_name[1] = full_name[1].replace("'", "''")
                codigo_jugador = PostgreSQL("select codigo from jugadores where nombre_preferido='"+ full_name[0] + "' and apellido='" + full_name[1] + "';")
                team_db = PostgreSQL("select team from jugadores where nombre_preferido='"+ full_name[0] + "' and apellido='" + full_name[1] + "';")

                if(codigo_jugador == []):
                    flag = True
                    break
                     
                insert_l += ", " + str(codigo_jugador[0][0])
                

            elif re.match("^\d*?\.\d+?$", line_s[x]) or line_s[x].isdigit():
                insert_l += ", " + line_s[x]
            else:
                insert_l += ", '" + line_s[x] + "'"     
        insert_l += ");"
        if flag==True:
            continue
    team = Teams[team_db[0][0]]
    insert_l = insert_l.replace(team_rep, str(team))            
    fileoutput.write(insert_l + '\n')
    i = i + 1