# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 12:45:52 2018

@author: Deme
"""

def filterStatuses(raw_statuses):
    """
    Filtra los estados de tweets en función de los campos "fields", que represe
    ntan los campos de interés.
    
    raw_statuses: list, lista que contiene cada estado de tweets en forma de di
    ccionario.
    
    output: diccionario x : y donde x es la id (str) de cad tweet e y es un dic
    cionario con los campos de interés.
    """
    
    from datetime import datetime as t
    
    fields = ['created_at', 'favorite_count', 'hashtags', 'id_str', 'retweet_count', 'full_text']
    statuses = {status['id_str']:{field:status[field] for field in fields if field != 'id_str'} for status in raw_statuses}
    
    for status in statuses:
        statuses[status]['hashtags'] = ', '.join(['#' + hashtag.text for hashtag in statuses[status]['hashtags']])
    
        # Adds current time as one of the fields
        statuses[status]['collected_at'] = str(t.now())
    
    return statuses

def getFilesInFolder(folder):
    
    from os import listdir
    from os.path import isfile, join
    
    return [f for f in listdir(folder) if isfile(join(folder, f))]

def getFoldersInFolder(folder=None):
    
    from os import listdir
    from os.path import isfile, join
    
    if folder != None:
        base = './{}/'.format(folder)
    else:
        base = './'
    
    return [f for f in listdir(base) if not isfile(join(base, f))]

def connected(reference = 'http://www.google.es'):
    """
    Determina si hay conexión a internet o no.
    
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
    """
    import os
    
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' + directory)