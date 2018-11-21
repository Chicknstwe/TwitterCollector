# -*- coding: utf-8 -*-

def filterStatuses(raw_statuses):
    """
    Filtra los estados de tweets en función de los campos "fields", que representan los campos de interés.
    
    raw_statuses: list, lista que contiene cada estado de tweets en forma de diccionario.
    
    output: diccionario x : y donde x es la id (str) de cad tweet e y es un diccionario con los campos de interés.
    """
    
    from datetime import datetime as t
    
    fields = ['created_at', 'favorite_count', 'hashtags', 'id_str', 'retweet_count', 'full_text', 'user_mentions']
    statuses = {status['id_str']:{field:status[field] for field in fields if field != 'id_str'} for status in raw_statuses}
    
    for status in statuses:
        statuses[status]['hashtags'] = ', '.join(['#' + hashtag.text for hashtag in statuses[status]['hashtags']])
        statuses[status]['user_mentions'] = ', '.join(['@' + user_mention.screen_name for user_mention in statuses[status]['user_mentions']])
    
        # Adds current time as one of the fields
        statuses[status]['collected_at'] = str(t.now())
    
    return statuses

def getFilesInFolder(folder):
    """
    Proporciona una lista de archivos en el directorio folder, siendo folder la ruta especificada.
    
    Ejemplo de ruta folder: './database/'
    
    input: string folder representada por una ruta
    output: list que contiene variables string con nombres de archivos en el directorio folder
    """
    from os import listdir
    from os.path import isfile, join
    
    return [f for f in listdir(folder) if isfile(join(folder, f))]

def getFoldersInFolder(folder=None):
    """
    Proporciona una lista de directorios en el directorio folder, siendo folder el nombre del directorio. La función busca el directorio indicado a partir del directorio raiz ('./').
    
    Ejemplo de directorio folder: 'database' o 'database/user'
    
    input: string folder representada por una ruta o None
    output: list que contiene variables string con nombres de archivos en el directorio folder o en el directorio base si folder es None
    """
    
    from os import listdir
    from os.path import isfile, join
    
    if folder != None:
        base = './{}/'.format(folder)
    else:
        base = './'
    
    return [f for f in listdir(base) if not isfile(join(base, f))]

def connected(reference = 'http://www.google.es'):
    """
    Determina si hay conexión a internet o no intentando conectar a http://www.google.es.
    
    Devuelve True si la hay y False en caso contrario.
    """
    import urllib
    
    try:
        urllib.request.urlopen(reference, timeout=1)
        return True
    except urllib.request.URLError:
        return False

def createFolder(directory):
    """
    Crea un directorio con el nombre directory en la ruta designada.
    
    input: string directory
    """
    import os
    
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except Exception as exc:
        print ('Error {} creando el directorio {}.'.format(exc, directory))
