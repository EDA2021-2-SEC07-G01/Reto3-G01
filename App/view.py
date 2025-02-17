﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
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
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

from typing import List
import config as cf
import sys
import controller
import pandas as pd
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as omap
from tabulate import tabulate
assert cf
import folium
import matplotlib.pyplot as plt
from IPython.display import display
import numpy as np

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    """
    Imprime el menú de visualización
    """
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Cargar información en el catálogo") # Se cargan los datos del catálogo
    print("2- Contar los avistamientos en una ciudad")
    print("3- Contar los avistamientos por duración") # Desplegar datos para la opción 3
    print("4- Contar los avistamientos por Hora/Minutos del día")
    print("5- Contar los avistamientos en un rango de fechas")
    print("6- Contar los avistamientos de una Zona Geográfica")
    print("7- Visualizar avistamientos de una zona geográfica")
    print("0- Salir")
    print("*******************************************")

catalog = None

def CreateCatalog():
    """Crea el catálogo de la base de datos de UFOs

    Returns:
        dict: Crea el catálogo como un diccionario en model con la información del .csv
    """
    return controller.CreateCatalog()

"""
Print Functions
"""
def printSightings(catalog, view=5): # TODO
    i = 0
    while i < view:
        print(" Los primeros 5 avistamientos cargados fueron: \n")
        i +=1

def printListsCities(list1, list2):
    headers = ["datetime", "city", "state", "country","shape","duration (seconds)"]
    table1 = []
    for sighting in lt.iterator(list1):
        table1.append([sighting["datetime"], sighting["city"],sighting["state"], sighting["country"],sighting["shape"],sighting["duration (seconds)"]])
    for sighting in lt.iterator(list2):
        table1.append([sighting["datetime"], sighting["city"],sighting["state"], sighting["country"],sighting["shape"],sighting["duration (seconds)"]])
    print(tabulate(table1,headers, tablefmt="grid"))

def printListsDates(list1, list2):
    headers = ["datetime","date","city", "state", "country","shape","duration (seconds)"]
    table1 = []
    for sighting in lt.iterator(list1):
        table1.append([sighting["elements"][0]["datetime"], sighting["elements"][0]["datetime"].split()[0], sighting["elements"][0]["city"],sighting["elements"][0]["state"], sighting["elements"][0]["country"],sighting["elements"][0]["shape"],sighting["elements"][0]["duration (seconds)"]])
    for sighting in lt.iterator(list2):
        table1.append([sighting["elements"][0]["datetime"], sighting["elements"][0]["datetime"].split()[0], sighting["elements"][0]["city"],sighting["elements"][0]["state"], sighting["elements"][0]["country"],sighting["elements"][0]["shape"],sighting["elements"][0]["duration (seconds)"]])
    print(tabulate(table1,headers, tablefmt="grid"))

def printDurationSeconds(list1, list2):
    headers = ["datetime","city","state", "country","shape","duration (seconds)"]
    table1 = []
    for sighting in lt.iterator(list1):
        table1.append([sighting["datetime"], sighting["city"], sighting["state"], sighting["country"], sighting["shape"], sighting["duration (seconds)"]])
    for sighting in lt.iterator(list2):
        table1.append([sighting["datetime"], sighting["city"], sighting["state"], sighting["country"], sighting["shape"], sighting["duration (seconds)"]])
    print(tabulate(table1,headers, tablefmt="grid"))

def printListsDatesByHour(list1, list2):
    headers = ["datetime","time","city", "state", "country","shape","duration (seconds)"]
    table1 = []
    for sighting in lt.iterator(list1):
        table1.append([sighting["datetime"], sighting["datetime"].split()[1], sighting["city"],sighting["state"], sighting["country"],sighting["shape"],sighting["duration (seconds)"]])
    for sighting in lt.iterator(list2):
        table1.append([sighting["datetime"], sighting["datetime"].split()[1], sighting["city"],sighting["state"], sighting["country"],sighting["shape"],sighting["duration (seconds)"]])
    print(tabulate(table1,headers, tablefmt="grid"))

def printLatitudLongitude(list1, list2):
    headers = ["datetime","city", "state", "country","shape","duration (seconds)", "latitude", "longitude"]
    table1 = []
    for sighting in lt.iterator(list1):
        table1.append([sighting["datetime"], sighting["city"],sighting["state"], sighting["country"],sighting["shape"],sighting["duration (seconds)"], sighting["latitude"], sighting["longitude"]])
    for sighting in lt.iterator(list2):
        table1.append([sighting["datetime"], sighting["city"],sighting["state"], sighting["country"],sighting["shape"],sighting["duration (seconds)"], sighting["latitude"], sighting["longitude"]])
    print(tabulate(table1,headers, tablefmt="grid"))

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = CreateCatalog()
        controller.AddData(catalog)
        #printSightings(catalog, view=5) Can be seen later

    elif int(inputs[0]) == 2:
        city = input("Ingrese la ciudad de búsqueda de interés: ")
        print("There are " +  str(omap.size(catalog["cities"])) + " different cities with UFO sightings.")
        print("The city with most UFO sightings is: " + str(controller.largestCity(catalog["cities"])))
        sightings_count, first_3, last_3 = controller.cities(catalog["cities"], city)
        print("\nThere are " + str(sightings_count) + " sightings at: " + city)
        print("The first 3 and last 3 UFO sightings are:")
        printListsCities(first_3, last_3)

    elif int(inputs[0]) == 3:
        print("There are "+str(omap.size(catalog["seconds"]))+" different durations of UFO sightings")
        print("\nThe longest UFO sightings are:")
        longest, count = controller.longestDurationSeconds(catalog["seconds"])
        print("Duration (seconds):", int(longest), ", Count:", count)
        low_lim = float(input("\nLímite inferior en segundos: "))
        upper_lim = float(input("Límite superior en segundos: "))
        sightings_count, first_3, last_3 = controller.seconds_range(catalog["seconds"], low_lim, upper_lim)
        print("\nThere are "+str(sightings_count)+" sightings between: "+str(low_lim)+" and "+str(upper_lim)+" seconds duration.")
        printDurationSeconds(first_3, last_3)

    elif int(inputs[0]) == 4:
        low_lim = input("Límite inferior en formato: HH:MM. ")
        upper_lim = input("Límite superior en formato: HH:MM. ")
        print("There are " + str(omap.size(catalog["datesByHour"])) + " UFO sighting with different times.")
        print("The latest UFO sighting time is:")
        date, count = controller.oldestDateByHour(catalog["datesByHour"])
        date = date.strftime("%H-%M-%S")
        print("Date: " + str(date) + ", count: " + str(count) + "\n")
        sightings_count, first_3, last_3 = controller.dates_rangeByHour(catalog["datesByHour"], low_lim, upper_lim)
        print("There are " + str(sightings_count) + " sightings between: " + low_lim + " and " + upper_lim)
        print("The first 3 and last 3 UFO sightings in this time are:")
        printListsDatesByHour(first_3, last_3)

    elif int(inputs[0]) == 5:
        low_lim = input("Límite inferior en formato: AAAA-MM-DD. ")
        upper_lim = input("Límite superior en formato: AAAA-MM-DD. ")
        print("\nThere are " + str(omap.size(catalog["dates"])) + " UFO sighting with different dates.")
        print("The oldest UFO sighting date is:")
        date, count = controller.oldestDate(catalog["dates"])
        date = date.strftime("%Y-%m-%d")
        print("Date: " + str(date) + ", count: " + str(count) + "\n")
        sightings_count, first_3, last_3 = controller.dates_range(catalog["dates"], low_lim, upper_lim)
        print("There are " + str(sightings_count) + " sightings between: " + low_lim + " and " + upper_lim)
        print("The first 3 and last 3 UFO sightings in this time are:")
        printListsDates(first_3, last_3)

    elif int(inputs[0]) == 6:
        long_min, long_max, lat_min, lat_max = map(float, input('Ingrese la longitud mínima, máxima, latitud mínima y máxima separadas por comas: ').split(','))
        sightings_count, first_5, last_5 = controller.coordinates(catalog["coordinates"], long_min, long_max, lat_min, lat_max )
        print("There are " + str(sightings_count) + " different UFO sightings in the current area.")
        print("\nThe first 5 and last 5 UFO sightings in this time are: ")
        printLatitudLongitude(first_5, last_5)

    elif int(inputs[0]) == 7:
        long_min, long_max, lat_min, lat_max = map(float, input('Ingrese la longitud mínima, máxima, latitud mínima y máxima separadas por comas: ').split(','))
        sightings_count, first_5, last_5 = controller.coordinates(catalog["coordinates"], long_min, long_max, lat_min, lat_max )
        print("There are " + str(sightings_count) + " different UFO sightings in the current area.")
        print("\nThe first 5 and last 5 UFO sightings in this time are: ")
        printLatitudLongitude(first_5, last_5) 
        map_sights = folium.Map(location=[np.mean([lat_max, lat_min]), np.mean([long_min, long_max])], zoom_start=6, tiles="Stamen Terrain")
        folium.Rectangle([(lat_min,long_min), (lat_max,long_max)],
                    color="blue",
                    weight=2,
                    fill=True,
                    fill_color="blue",
                    fill_opacity=0.1).add_to(map_sights)
        tooltip = "OVNI!"
        for sighting in lt.iterator(first_5):
            popup = "<b>City:</b> "+sighting["city"]+", \n<b>Datetime:</b> "+sighting["datetime"]+", \n<b>Duration [s]:</b> "+sighting["duration (seconds)"]+", \n<b>Shape:</b> "+sighting["shape"]
            folium.Marker(location=[sighting["latitude"], sighting["longitude"]], popup = popup, tooltip = tooltip, icon=folium.Icon(color="orange", icon="map-marker")).add_to(map_sights)
        for sighting in lt.iterator(last_5):
            popup = "<b>City:</b> "+sighting["city"]+", \n<b>Datetime:</b> "+sighting["datetime"]+", \n<b>Duration [s]:</b> "+sighting["duration (seconds)"]+", \n<b>Shape:</b> "+sighting["shape"]
            folium.Marker(location=[sighting["latitude"], sighting["longitude"]], popup = popup, tooltip = tooltip, icon=folium.Icon(color="orange", icon="map-marker")).add_to(map_sights)
        map_sights.save('ovnis.html')
    else:
        sys.exit(0)
sys.exit(0)
