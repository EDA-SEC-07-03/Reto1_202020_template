import config as cf
import sys
import csv
from time import process_time

from ADT import list as lt
from DataStructures import liststructure as lt
from Sorting import selectionsort as sel
from Sorting import insertionsort as ins
from Sorting import shellsort as she
import reto as rt 


#tipos de EDA 'ARRAY_LIST' y "'SINGLE_LINKED'"
#"themoviesdb/AllMoviesDetailsCleaned.csv"
#"themoviesdb/AllMoviesCastingRaw.csv"

#"themoviesdb/MoviesCastingRaw-small.csv"
#"themoviesdb/SmallMoviesDetailsCleaned.csv"

def comparador_ascendente(pos1,pos2):
    if float(pos1["votos"]) > float(pos2["votos"]):
        return True
    return False
def comparador_descendente(pos1,pos2):
    if float(pos1["votos"]) < float(pos2["votos"]):
        return True
    return False

def comparador_ascendente_average(pos1,pos2):
    if float(pos1["promedio"]) > float(pos2["promedio"]):
        return True
    return False
def comparador_descendente_average(pos1,pos2):
    if float(pos1["promedio"]) < float(pos2["promedio"]):
        return True
    return False

def conocer_a_director(director,datos_casting,datos_movies)->tuple:
    tiempo1=process_time()
    peliculas=[]
    promedio=0
    pos_directores=[]
    for i in range(1,datos_casting["size"]):
        filas=lt.getElement(datos_casting,i)
        if(filas['director_name'].lower() == director.lower()):
            pos_directores.append(int(filas["id"]))

    for i in pos_directores:
        x=1
        while x < lt.size(datos_movies):
            fila=lt.getElement(datos_movies,x)
            if(int(fila["\ufeffid"]) == i):
                peliculas.append(fila["title"])
                promedio+=float(fila['vote_average'])
                break
            x+=1
    numero_de_peliculas=len(pos_directores)
    if(numero_de_peliculas != 0):
        promedio=promedio/numero_de_peliculas
    retorno=((peliculas),(round(promedio,2)),(numero_de_peliculas))
    tiempo2=process_time()
    print("Su tiempo fue de",tiempo2-tiempo1,"segundos.")
    return retorno

#usuario elige si es AVERAGE O COUNT
#usuario elige si desea una lista ascendente o descendente
"""usuario elige si desea resultados votos(vote_count) o votos en promedio(vote_average), 
los resultados descendentes son re ordenados de nuevo usando los votos si el usuario eligio promedio, 
o usando el promedio si el usuario eligio datos""" 


def crear_ranking_gen(movies,orden,tipo,genero,numero_de_peliculas=10):
    if(tipo.lower() == "ascendente"):
        if(orden.lower() == "votos" ):
            peliculas_genero=lt.newList("ARRAY_LIST")
            eleccion_usuario=lt.newList("ARRAY_LIST")
            for i in range(1,lt.size(movies)):
                elemento=lt.getElement(movies,i)
                if(genero.lower() in elemento["genres"].lower()):
                    pelis={}
                    pelis["titulo"]=elemento["title"]
                    pelis["votos"]=float(elemento["vote_count"])
                    pelis["promedio"]=float(elemento["vote_average"])
                    lt.addLast(peliculas_genero,pelis)
            she.shellSort(peliculas_genero,comparador_ascendente)
            for i in range(1,lt.size(peliculas_genero)):
                lt.addLast(eleccion_usuario,lt.getElement(peliculas_genero,i))
                if(lt.size(eleccion_usuario) == numero_de_peliculas):
                    break
            return eleccion_usuario
            
        elif(orden.lower() == "promedio" ):
            peliculas_genero=lt.newList("ARRAY_LIST")
            eleccion_usuario=lt.newList("ARRAY_LIST")
            for i in range(1,lt.size(movies)):
                elemento=lt.getElement(movies,i)
                if(genero.lower() in elemento["genres"].lower()):
                    pelis={}
                    pelis["titulo"]=elemento["title"]
                    pelis["votos"]=float(elemento["vote_count"])
                    pelis["promedio"]=float(elemento["vote_average"])
                    lt.addLast(peliculas_genero,pelis)
            she.shellSort(peliculas_genero,comparador_ascendente_average)
            for i in range(1,lt.size(peliculas_genero)):
                lt.addLast(eleccion_usuario,lt.getElement(peliculas_genero,i))
                if(lt.size(eleccion_usuario) == numero_de_peliculas):
                    break
            return eleccion_usuario

    elif(tipo.lower() == "descendente"):
        if(orden.lower() == "votos" ):
            peliculas_genero=lt.newList("ARRAY_LIST")
            eleccion_usuario=lt.newList("ARRAY_LIST")
            for i in range(1,lt.size(movies)):
                elemento=lt.getElement(movies,i)
                if(genero.lower() in elemento["genres"].lower()):
                    pelis={}
                    pelis["titulo"]=elemento["title"]
                    pelis["votos"]=float(elemento["vote_count"])
                    pelis["promedio"]=float(elemento["vote_average"])
                    lt.addLast(peliculas_genero,pelis)
            she.shellSort(peliculas_genero,comparador_descendente)
            for i in range(1,lt.size(peliculas_genero)):
                lt.addLast(eleccion_usuario,lt.getElement(peliculas_genero,i))
                if(lt.size(eleccion_usuario) == numero_de_peliculas):
                    break
            she.shellSort(eleccion_usuario,comparador_descendente_average)
            return eleccion_usuario
            
        elif(orden.lower() == "promedio" ):
            peliculas_genero=lt.newList("ARRAY_LIST")
            eleccion_usuario=lt.newList("ARRAY_LIST")
            for i in range(1,lt.size(movies)):
                elemento=lt.getElement(movies,i)
                if(genero.lower() in elemento["genres"].lower()):
                    pelis={}
                    pelis["titulo"]=elemento["title"]
                    pelis["votos"]=float(elemento["vote_count"])
                    pelis["promedio"]=float(elemento["vote_average"])
                    lt.addLast(peliculas_genero,pelis)
            she.shellSort(peliculas_genero,comparador_descendente_average)
            for i in range(1,lt.size(peliculas_genero)):
                lt.addLast(eleccion_usuario,lt.getElement(peliculas_genero,i))
                if(lt.size(eleccion_usuario) == numero_de_peliculas):
                    break
            she.shellSort(eleccion_usuario,comparador_descendente)
            return eleccion_usuario









