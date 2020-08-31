"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv
import functions as fun


from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt

from time import process_time 

def crear_ranking_peliculas(lst : list, numero : int, eleccion_orden : str, eleccion_mejor : str):
    ## la eleccion orden es para saber si se pone del mejor al peor o como. 
    ##y la eleccion_mejor es para saber si quiere los mejores o las peores###
    n_votos = []
    p_votos = []
    nombres = []
    retorno = []
    for i in range(1, len(lst)-1):
        n_votos.append(int(lst[i]["vote_count"]))
        p_votos.append(float(lst[i]["vote_average"]))
        nombres.append(lst[i]["name"])
    x = 0
    if eleccion_mejor == "mejores":
        while x != numero:
            m = max(n_votos)
            busca = n_votos.index(x)
            retorno.append(nombres[busca])
            x += 1
    if eleccion_mejor == "peores":
        while x != numero:
            m = min(p_votos)
            busca = p_votos.index(x)
            retorno.append(nombres[busca])
            x +=1
    if eleccion_orden == "ascendente":
        return retorno
    if eleccion_orden == "descendente":
        return retorno.reverse()

def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Ranking de peliculas")
    print("3- Conocer un director")
    print("4- Conocer un actor")
    print("5- Entender un genero")
    print("6- Crear ranking")
    print("0- Salir")
        

def compareRecordIds (recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return -1


def loadCSVFile (file,cmpfunction):
    lst=lt.newList("ARRAY_LIST", cmpfunction)
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open( cf.data_dir + file, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for elemento in row: 
                lt.addLast(lst,elemento)
    except:
        print("Hubo un error con la carga del archivo")
    return lst

#"themoviesdb/MoviesCastingRaw-small.csv"
#"themoviesdb/SmallMoviesDetailsCleaned.csv"

def loadMovies(dire):
    lst = loadCSVFile(dire,compareRecordIds) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """


    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:

            if int(inputs[0])==1: #opcion 1
                datos_casting=loadMovies("themoviesdb/AllMoviesCastingRaw.csv")
                datos_movies=loadMovies("themoviesdb/AllMoviesDetailsCleaned.csv")

            elif int(inputs[0])==2: #opcion 2
                eleccion_mejor = input("Digite ´mejores´, si quiere un ranking de las mejores peliculas, o, de peores si quiere un ranking de las peores: ")
                numero = int(input("Digite cuantas peliculas quiere en el ranking: "))
                eleccion_orden = input("Digite si quiere que el ranking sea ascendente o descendente: ")
                funcion = crear_ranking_peliculas(datos_movies, numero, eleccion_orden, eleccion_mejor)
                pass

            elif int(inputs[0])==3: #opcion 3
                director=input("Digite el director que desea buscar:\n")
                conocer_director=fun.conocer_a_director(director,datos_casting,datos_movies)
                print("_________________________________________")
                print("Número de películas:",conocer_director[2],"  ","Promedio de calificación:",conocer_director[1])
                print("_________________________________________")
                x=1
                for i in conocer_director[0]:
                    print(x,i)
                    x+=1
                print("_________________________________________")


            elif int(inputs[0])==4: #opcion 4
                pass

            elif int(inputs[0])==5: #opcion 5
                pass

            elif int(inputs[0])==6: #opcion 6
                genero=input("¿Cuál género desea buscar?:\n")
                ascendente_descendente=input("Sí desea una lista de las mejores peliculas digite:ascendente,si desea una lista de las peores peliculas digite: descendente. \n")
                criterio=input("Elija con que criterio desea realizar su búsqueda, por número de votos digite: votos, para que sea con respecto al promedio digite: promedio. \n")
                deseo=input("¿desea un ranking por defecto(10 películas)?: Si o No:\n")
                tamaño=0
                if(deseo.lower() == "si" ):
                    resultado=fun.crear_ranking_gen(datos_movies,criterio,ascendente_descendente,genero)
                elif(deseo.lower() == "no" ):
                    tamaño=int(input("Elija el número de peliculas que desea para su ranking:\n"))
                    resultado=fun.crear_ranking_gen(datos_movies,criterio,ascendente_descendente,genero,tamaño)
                if(ascendente_descendente == "ascendente"):
                    print("_________________________________________")
                    if(deseo == "si"):
                        print("Top 10 mejores peliculas de:",genero)
                        print("Top,Titulo,Votos,Promedio")
                        print("_________________________________________")
                        x=1
                        for i in range(1,lt.size(resultado)+1):
                            print(x,(lt.getElement(resultado,i))["titulo"],",",(lt.getElement(resultado,i))["votos"],",",(lt.getElement(resultado,i))["promedio"])
                            x+=1
                        print("_________________________________________")

                    elif(deseo== "no"):
                        print("top",tamaño,"mejores peliculas de:",genero)
                        print("Top,Titulo,Votos,Promedio")
                        print("_________________________________________")
                        x=1
                        for i in range(1,lt.size(resultado)+1):
                            print(x,(lt.getElement(resultado,i))["titulo"],",",(lt.getElement(resultado,i))["votos"],",",(lt.getElement(resultado,i))["promedio"])
                            x+=1
                        print("_________________________________________")
                elif(ascendente_descendente == "descendente"):
                    print("_________________________________________")
                    if(deseo == "si"):
                        print("Top 10 peores peliculas de",genero)
                        print("Top,Titulo,Votos,Promedio")
                        print("_________________________________________")
                        x=1
                        for i in range(1,lt.size(resultado)+1):
                            print(x,(lt.getElement(resultado,i))["titulo"],",",(lt.getElement(resultado,i))["votos"],",",(lt.getElement(resultado,i))["promedio"])
                            x+=1
                        print("_________________________________________")

                    elif(deseo== "no"):
                        print("top",tamaño,"peores peliculas de:",genero)
                        print("Top,Titulo,Votos,Promedio")
                        print("_________________________________________")
                        x=1
                        for i in range(1,lt.size(resultado)+1):
                            print(x,(lt.getElement(resultado,i))["titulo"],",",(lt.getElement(resultado,i))["votos"],",",(lt.getElement(resultado,i))["promedio"])
                            x+=1
                        print("_________________________________________")
                        
                

            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()