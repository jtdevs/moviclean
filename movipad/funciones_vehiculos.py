import os
############################################################################################################
#patentesDB.txt -> patente/marca/modelo/color/tipo/veces

#Annade un vehiculo a la base de datos
def crear_vehiculo(patente, marca, modelo, color, tipo): #annade un nuevo vehiculo a la base de datos
    datos = ''
    datos += patente+'/'
    datos += marca+'/'
    datos += modelo+'/'
    datos += color+'/'
    datos += tipo+'/'
    datos += '1\n'
    archivo = open('patentesDB.txt', 'a')
    archivo.write(datos)
    archivo.close()
    return None

def validar_patente(patente):
    archivo = open('patentesDB.txt', 'r')
    for line in archivo:
        if patente == line.split('/')[0] and len(patente) == 6:
            return True
    else:
        return False

#Busca un vehiculo en la base de datos, True or False
def buscar_vehiculo(patente):
    archivo = open('patentesDB.txt', 'r')
    for line in archivo:
        if patente == line.split('/')[0]:
            archivo.close()
            return True
    archivo.close()
    return False

def datos_vehiculo(patente):
    archivo = open('patentesDB.txt', 'r')
    for line in archivo:
        tmp = line.split('/')
        if patente == tmp[0]:
            archivo.close()
            return tmp[:5]
    archivo.close()
    print "El vehiculo no existe"
    return [0,0,0,0,0]

#Aumenta 'incremento' veces la cantidad de veces que el vehiculo nos ha visitado
def veces_vehiculo(patente):
    archivo = open('patentesDB.txt', 'r')
    temp = open('temp.txt', 'w')
    for line in archivo:
        line_elements = line.split('/')
        if patente == line_elements[0]:
            line = ''
            for n in range (5):
                line += line_elements[n]+'/'
            veces = int(line_elements[5])
            veces += 1
            line += str(veces)+'\n'
        temp.write(line)
    archivo.close()
    temp.close()
    archivo = open('patentesDB.txt', 'w')
    temp = open('temp.txt', 'r')
    for line in temp:
        archivo.write(line)
    archivo.close()
    temp.close()
    os.remove('temp.txt')
    return None

#Modifica la marca de un vehiculo
def mod_vehiculo_marca(patente, marca):
    archivo = open('patentesDB.txt', 'r')
    temp = open('temp.txt', 'w')
    for line in archivo:
        line_elements = line.split('/')
        if patente == line_elements[0]:
            line = ''
            line += line_elements[0]+'/'#patente
            line += marca+'/'#marca
            line += line_elements[2]+'/'#modelo
            line += line_elements[3]+'/'#color
            line += line_elements[4]+'/'#tipo
            line += line_elements[5]#veces
        temp.write(line)
    archivo.close()
    temp.close()
    archivo = open('patentesDB.txt', 'w')
    temp = open('temp.txt', 'r')
    for line in temp:
        archivo.write(line)
    archivo.close()
    temp.close()
    os.remove('temp.txt')
    return None

#Modifica el modelo de un vehiculo
def mod_vehiculo_modelo(patente, modelo):
    archivo = open('patentesDB.txt', 'r')
    temp = open('temp.txt', 'w')
    for line in archivo:
        line_elements = line.split('/')
        if patente == line_elements[0]:
            line = ''
            line += line_elements[0]+'/'#patente
            line += line_elements[1]+'/'#marca
            line += modelo+'/'#modelo
            line += line_elements[3]+'/'#color
            line += line_elements[4]+'/'#tipo
            line += line_elements[5]#veces
        temp.write(line)
    archivo.close()
    temp.close()
    archivo = open('patentesDB.txt', 'w')
    temp = open('temp.txt', 'r')
    for line in temp:
        archivo.write(line)
    archivo.close()
    temp.close()
    os.remove('temp.txt')
    return None

def mod_vehiculo_color(patente, color):
    archivo = open('patentesDB.txt', 'r')
    temp = open('temp.txt', 'w')
    for line in archivo:
        line_elements = line.split('/')
        if patente == line_elements[0]:
            line = ''
            line += line_elements[0]+'/'#patente
            line += line_elements[1]+'/'#marca
            line += line_elements[2]+'/'#modelo
            line += tipo+'/'#color
            line += line_elements[4]+'/'#tipo
            line += line_elements[5]#veces
        temp.write(line)
    archivo.close()
    temp.close()
    archivo = open('patentesDB.txt', 'w')
    temp = open('temp.txt', 'r')
    for line in temp:
        archivo.write(line)
    archivo.close()
    temp.close()
    os.remove('temp.txt')
    return None

#Modifica el tipo de un vehiculo
def mod_vehiculo_tipo(patente, tipo):
    archivo = open('patentesDB.txt', 'r')
    temp = open('temp.txt', 'w')
    for line in archivo:
        line_elements = line.split('/')
        if patente == line_elements[0]:
            line = ''
            line += line_elements[0]+'/'#patente
            line += line_elements[1]+'/'#marca
            line += line_elements[2]+'/'#modelo
            line += line_elements[3]+'/'#color
            line += tipo+'/'#tipo
            line += line_elements[5]#veces
        temp.write(line)
    archivo.close()
    temp.close()
    archivo = open('patentesDB.txt', 'w')
    temp = open('temp.txt', 'r')
    for line in temp:
        archivo.write(line)
    archivo.close()
    temp.close()
    os.remove('temp.txt')
    return None

#Elimina un vehiculo de la base de datos
def del_vehiculo(patente):
    archivo = open('patentesDB.txt', 'r')
    temp = open('temp.txt', 'w')
    for line in archivo:
        line_elements = line.split('/')
        if patente != line_elements[0]:
            temp.write(line)
    archivo.close()
    temp.close()
    archivo = open('patentesDB.txt', 'w')
    temp = open('temp.txt', 'r')
    for line in temp:
        archivo.write(line)
    archivo.close()
    temp.close()
    os.remove('temp.txt')
    return None