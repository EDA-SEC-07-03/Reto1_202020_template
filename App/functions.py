import config as cf
import sys
import csv
from time import process_time

from ADT import list as lt
from DataStructures import liststructure as lt
from Sorting import selectionsort as selectionsort
from Sorting import insertionsort as insertionsort
from Sorting import shellsort as shellsort
import reto as rt 


#tipos de EDA 'ARRAY_LIST' y "'SINGLE_LINKED'"
#"themoviesdb/AllMoviesDetailsCleaned.csv"
#"themoviesdb/AllMoviesCastingRaw.csv"

#"themoviesdb/MoviesCastingRaw-small.csv"
#"themoviesdb/SmallMoviesDetailsCleaned.csv"
movies=rt.loadMovies("themoviesdb/SmallMoviesDetailsCleaned.csv")

def conocer_a_director(director,datos_casting)->tuple:
    tiempo1=process_time()
    datos_movies=rt.loadMovies("themoviesdb/AllMoviesDetailsCleaned.csv")  
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
def ordenadorx(objeto1,objeto2):
    pass
def crear_ranking_gen(movies=movies,orden="count",tipo="Ascendente",numero_de_peliculas=10,genero="Crime"):
    if(tipo.lower() == "ascendente"):
        if(orden.lower() == "count" ):
            peliculas_genero=lt.newList("ARRAY_LIST")
            for i in range(1,lt.size(movies)):
                elemento=lt.getElement(movies,i)
                if(genero.lower() in elemento["genres"].lower()):
                    pelis={}
                    pelis[elemento["title"]]=float(elemento["vote_count"])
                    lt.addLast(peliculas_genero,pelis)
                if(lt.size(peliculas_genero) == numero_de_peliculas):
                    break
            print(peliculas_genero)
        elif(orden.lower() == "average"):
            peliculas_genero=lt.newList("ARRAY_LIST")
            for i in range(1,lt.size(movies)):
                elemento=lt.getElement(movies,i)
                pelis={}
                if(genero.lower() in elemento["genres"].lower()):
                    pelis[elemento["title"]]=float(elemento["vote_average"])
                lt.addLast(peliculas_genero,pelis)

    """elif(tipo.lower() == "descendente"):
        if(orden.lower() == "count" ):
            peliculas_genero=lt.newList("ARRAY_LIST")
            for i in range(1,lt.size(movies)):
                elemento=lt.getElement(movies,i)
                pelis={}
                if(genero.lower() in elemento["genres"].lower()):
                    pelis[elemento["title"]]=float(elemento["vote_count"])
                lt.addLast(peliculas_genero,pelis)
        elif(ordenamiento.lower() == "average"):
            peliculas_genero=lt.newList("ARRAY_LIST")
            for i in range(1,lt.size(movies)):
                elemento=lt.getElement(movies,i)
                pelis={}
                if(genero.lower() in elemento["genres"].lower()):
                    pelis[elemento["title"]]=float(elemento["vote_average"])
                lt.addLast(peliculas_genero,pelis)"""
crear_ranking_gen()







