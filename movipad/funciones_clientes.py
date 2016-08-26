from funciones_tiempos import*
import os
############################################################################################################
#personasDB.txt -> rut/nombre/genero/correo/telefono/lista_patentes/veces

#Crea un mailist de todas las personas que hayan ido veces >= n
def crear_mailist(n):
    fecha = get_date()
    mailist = open('mailist-'+fecha+'.txt', 'w')
    archivo = open('personasDB.txt', 'r')
    for line in archivo:
        tmp = line.split('/')
        if int(tmp[5].strip()) >= n:
            mailist.write(tmp[2]+', ')
    mailist.write('contacto@moviclean.cl')
    archivo.close()
    mailist.close()
    return None

#Annade un nuevo cliente a la base de datos
def crear_cliente(rut, nombre, genero, correo, telefono, patente): #annade una nueva persona a la base de datos
    datos = ''
    datos += rut+'/'
    datos += nombre+'/'
    datos += genero+'/'
    datos += correo+'/'
    datos += telefono+'/'
    datos += patente+'/'
    datos += '1\n'
    archivo = open('personasDB.txt', 'a')
    archivo.write(datos)
    archivo.close()
    return None
####################################################
#Verifica si existe el cliente por rut, True or False
def buscar_cliente(rut):
    archivo = open('personasDB.txt', 'r')
    for line in archivo:
        if rut == line.split('/')[0]:
            archivo.close()
            return True
    archivo.close()
    return False

def datos_cliente(rut):
    archivo = open('personasDB.txt', 'r')
    for line in archivo:
        tmp = line.split('/')
        if rut == tmp[0]:
            archivo.close()
            return tmp[:5]
    archivo.close()
    print "El cliente no existe"
    return [0,0,0,0,0]
###################################################
#Aumenta en 1 la cantidad de veces que nos ha visitado el cliente
def veces_cliente(rut):
    archivo = open('personasDB.txt', 'r')
    temp = open('temp.txt', 'w')
    for line in archivo:
        line_elements = line.split('/')
        if rut == line_elements[0]:
            line = ''
            for n in range (6):
                line += line_elements[n]+'/'
            veces = int(line_elements[6])
            veces += 1
            line += str(veces)+'\n'
        temp.write(line)
    archivo.close()
    temp.close()
    archivo = open('personasDB.txt', 'w')
    temp = open('temp.txt', 'r')
    for line in temp:
        archivo.write(line)
    archivo.close()
    temp.close()
    os.remove('temp.txt')
    return None

#Annade una patente a un cliente si es que esta no existe en su historial
def vehiculo_a_cliente(patente, rut):
    archivo = open('personasDB.txt', 'r')
    temp = open('temp.txt', 'w')
    write = False
    for line in archivo:
        line_elements = line.split('/')
        if rut == line_elements[0]:
            patentes_persona = line_elements[5].split(',')
            if patente not in patentes_persona:
                write = True
                line = ''
                line += line_elements[0]+'/'
                line += line_elements[1]+'/'
                line += line_elements[2]+'/'
                line += line_elements[3]+'/'
                line += line_elements[4]+'/'
                patentes = ''
                for n in range(len(patentes_persona)):
                    patentes += patentes_persona[n]+','
                patentes += patente
                line += patentes+'/'
                line += line_elements[6]
        temp.write(line)
    archivo.close()
    temp.close()  
    if write == True:       
        archivo = open('personasDB.txt', 'w')
        temp = open('temp.txt', 'r')
        for line in temp:
            archivo.write(line)
        archivo.close()
        temp.close()
    os.remove('temp.txt')
    return None

#Valida el digito verificador del rut ingresado
def validar_rut(rut):
    rut = str(rut)
    secuencia = [9,8,7,6,5,4,9,8]
    dv = rut[-1]
    digitos = rut[:len(rut)-2]
    digitos = digitos[::-1]
    tmp = 0
    for i in range(len(digitos)):
        tmp += int(secuencia[i])*int(digitos[i])
    tmp = tmp%11
    if tmp == 10:
        if dv == 'k' or dv == 'K':
            return True
    elif str(tmp) == dv:
        return True
    else:
        return False

#Elimina un cliente de la base de datos
def del_cliente(rut):
    archivo = open('personasDB.txt', 'r')
    temp = open('temp.txt', 'w')
    for line in archivo:
        line_elements = line.split('/')
        if rut != line_elements[0]:
            temp.write(line)
    archivo.close()
    temp.close()
    archivo = open('personasDB.txt', 'w')
    temp = open('temp.txt', 'r')
    for line in temp:
        archivo.write(line)
    archivo.close()
    temp.close()
    os.remove('temp.txt')
    return None

#Modifica el nombre de un cliente
def mod_cliente_nombre(rut, nombre):
    archivo = open('personasDB.txt', 'r')
    temp = open('temp.txt', 'w')
    for line in archivo:
        line_elements = line.split('/')
        if rut == line_elements[0]:
            line = ''
            line += line_elements[0]+'/'#rut
            line += nombre+'/'
            line += line_elements[2]+'/'#genero
            line += line_elements[3]+'/'#correo
            line += line_elements[4]+'/'#telefono
            line += line_elements[5]+'/'#patentes
            line += line_elements[6]#veces
        temp.write(line)
    archivo.close()
    temp.close()
    archivo = open('personasDB.txt', 'w')
    temp = open('temp.txt', 'r')
    for line in temp:
        archivo.write(line)
    archivo.close()
    temp.close()
    os.remove('temp.txt')
    return None

def mod_cliente_genero(rut):
    archivo = open('personasDB.txt', 'r')
    temp = open('temp.txt', 'w')
    for line in archivo:
        line_elements = line.split('/')
        if rut == line_elements[0]:
            line = ''
            line += line_elements[0]+'/'#rut
            line += line_elements[1]+'/'#nombre
            if line_elements[2] == 'H':
            	genero = 'M'
            elif line_elements[2] == 'M':
            	genero = 'H'
            line += genero+'/'
            line += line_elements[3]+'/'#correo
            line += line_elements[4]+'/'#telefono
            line += line_elements[5]+'/'#patentes
            line += line_elements[6]#veces
        temp.write(line)
    archivo.close()
    temp.close()
    archivo = open('personasDB.txt', 'w')
    temp = open('temp.txt', 'r')
    for line in temp:
        archivo.write(line)
    archivo.close()
    temp.close()
    os.remove('temp.txt')
    return None

#Modifica el correo de un cliente
def mod_cliente_correo(rut, correo):
    archivo = open('personasDB.txt', 'r')
    temp = open('temp.txt', 'w')
    for line in archivo:
        line_elements = line.split('/')
        if rut == line_elements[0]:
            line = ''
            line += line_elements[0]+'/'#rut
            line += line_elements[1]+'/'#nombre
            line += line_elements[2]+'/'#genero
            line += correo+'/'
            line += line_elements[4]+'/'#telefono
            line += line_elements[5]+'/'#patentes
            line += line_elements[6]#veces
        temp.write(line)
    archivo.close()
    temp.close()
    archivo = open('personasDB.txt', 'w')
    temp = open('temp.txt', 'r')
    for line in temp:
        archivo.write(line)
    archivo.close()
    temp.close()
    os.remove('temp.txt')
    return None

#Modifica el telefono de un cliente
def mod_cliente_telefono(rut, telefono):
    archivo = open('personasDB.txt', 'r')
    temp = open('temp.txt', 'w')
    for line in archivo:
        line_elements = line.split('/')
        if rut == line_elements[0]:
            line = ''
            line += line_elements[0]+'/'#rut
            line += line_elements[1]+'/'#nombre
            line += line_elements[2]+'/'#genero
            line += line_elements[3]+'/'#correo
            line += telefono+'/'
            line += line_elements[5]+'/'#patentes
            line += line_elements[6]#veces
        temp.write(line)
    archivo.close()
    temp.close()
    archivo = open('personasDB.txt', 'w')
    temp = open('temp.txt', 'r')
    for line in temp:
        archivo.write(line)
    archivo.close()
    temp.close()
    os.remove('temp.txt')
    return None