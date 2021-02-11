'''
Created on 11/02/2021
@author: lukes158@gmail.com l0m1s
'''

from configparser import ConfigParser


def leggi_configurazioni(file,nameOption):
    config_object = ConfigParser()
    config_object.read(file)
    xElement = []
    for element in config_object.options(nameOption):
        xElement.append(config_object.get(nameOption, element))
    return xElement


if __name__ == "__main__":
    file = "config.ini"
    
    xConfigColori = leggi_configurazioni(file,'COLORI')
    xConfigServer = leggi_configurazioni(file,'SERVER')

    print(xConfigColori)
    print(xConfigServer)