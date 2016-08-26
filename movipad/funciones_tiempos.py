import datetime
############################################################################################################
#tiemposDB.txt -> codigos/h_inicio/h_termino

#Annade los tiempos relacionados a una lista de servicios
def guardar_tiempos(codigos, h_llegada, h_inicio, h_termino, h_salida):
    tmp = ''
    tmp += codigos+'/'
    tmp += h_llegada+'/'
    tmp += h_inicio+'/'
    tmp += h_termino+'/'
    tmp += h_salida+'\n'
    archivo = open('tiemposDB.txt', 'a')
    archivo.write(tmp)
    archivo.close()
    return None

#Obtiene la hora actual
def get_time():
    hora = str(datetime.datetime.today()).split(' ')[1][:5]
    return hora

#Obtiene la fecha actual
def get_date():
    tmp = str(datetime.datetime.today()).split(' ')[0].split('-')
    year = tmp[0][2:4]
    month = tmp[1]
    day = tmp[2]
    fecha = day+'-'+month+'-'+year
    #fecha = time.strftime("%d-%m-%y")
    return fecha

#Obtiene el dia de la semana
num_a_dia = {0:'Lunes    ', 1:'Martes   ', 2:'Miercoles', 3:'Jueves   ', 4:'Viernes  ', 5:'Sabado   ', 6:'Domingo  '}
def get_dayofweek():
    num = datetime.datetime.today().weekday()
    return num_a_dia[num]

#Validar el formato de la fecha
def validar_fecha(fecha):
    tmp = fecha.split('-')
    if len(fecha) == 8 and int(tmp[0]) <= 31 and int(tmp[1]) <= 12:
        return True
    else:
        return False

def validar_hora(hora):
    tmp = hora.split(':')
    if len(hora) == 5 and int(tmp[0]) <= 24 and int(tmp[1]) <= 60:
        return True
    else:
        return False
############################################################################################################