#_todo_: modulos de obtencion de estadisticas a partir de los archivos generados
#_todo_: modulos de depuracion de bases de datos
from funciones_clientes import *
from funciones_tiempos import *
from funciones_ventas import *
from funciones_vehiculos import *
from funciones_servicios import *
#data = [patente, marca, modelo, color, tipo, rut, nombre, correo, telefono]
opt = ''
queued_services = {}
active_services = {}
finished_services = {}
while opt != 0:
    opt = int(raw_input("0->Salir, 1->Ingresar, 2->Comenzar, 3->Finalizar, 4->Entregar, 5->Resumen Diario, 6->Modificar Info: "))
    if opt == 1:
        data = []
###############################TOMA DE DATOS VEHICULO########################################################
        patente = raw_input("Ingrese Patente: ").upper()#_todo_ verificar que no exceda 6 caracteres
        if buscar_vehiculo(patente) == False:
            marca = raw_input("Ingrese Marca:").upper()#_todo_ verificar que no exceda 32 caracteres
            modelo = raw_input("Ingrese Modelo:").upper()#_todo_ verificar que no exceda 32 caracteres
            color = raw_input("Ingrese Color:").upper()#_todo_ verificar que no exceda 32 caracteres
            tipo =raw_input("Ingrese Tipo:").upper()#_todo_ verificar que no exceda 32 caracteres
            crear_vehiculo(patente, marca, modelo, color, tipo)
        else:
            veces_vehiculo(patente)
        data += datos_vehiculo(patente)
##################################TOMA DE DATOS CLIENTE#####################################################
        rut = raw_input("Ingrese Rut: ").upper()
        if rut != '0':
            while validar_rut(rut) == False:
                print("\nRut Incorrecto!\n")
                rut = raw_input("Ingrese Rut: ").upper()
            if buscar_cliente(rut, 'boolean') == False:
                nombre = raw_input("Ingrese Nombre: ")#_todo_ verificar que no exceda 32 caracteres
                nombre = nombre.upper()
                correo = raw_input("Ingrese Correo: ")#_todo_ verificar que no exceda 32 caracteres
                telefono = raw_input("Ingrese Telefono: ")#_todo_ verificar que no exceda 32 caracteres
                crear_cliente(rut, nombre, correo, telefono, patente)
            else:
                veces_cliente(rut)
            vehiculo_a_cliente(patente, rut)
        data+=datos_cliente(rut);
#################################TOMA DE DATOS SERVICIOS####################################################
        #_todo_ annadir codigo para diferenciar servicios de productos
        #_todo_ obtener precios en razon del codigo y el tamanno estandarizado del vehiculo
        servicio = ''
        codigos = ''
        print('\nIngrese el numero de servicio: (0 para salir)\n')
        while True:
            while True:
                servicio = raw_input('Ingrese codigo de servicio: ')
                if validar_codigo(servicio)==True or servicio == '0':
                    break
                else:
                    print('El codigo ingresado no existe.')
            if servicio == '0':
                break
            cantidad = int(raw_input('Ingrese numero de items (-1 para eliminar un servicio): '))
            if cantidad > 0:
                for k in range(cantidad):
                    if codigos != '':
                        codigos += ','
                    codigos += servicio
            elif cantidad == -1:
                tmp = codigos.split(',')
                codigos = ''
                for k in range(len(tmp)):
                    if tmp[k] != servicio:
                        if codigos != '':
                            codigos += ','
                        codigos += tmp[k]
        while True:
            hora_estimada = raw_input('Ingrese hora estimada de entrega: ')
            #_todo_ dar posibilidad de agregar nuevos productos al momento de entrega
            #_todo_ ver posibilidad de evitar el loop si son solo productos  -> Menu de venta simple exclusivo para productos
            if validar_hora(hora_estimada) == True:
                break
            else:
                print('La hora ingresada no esta en el formato HH:MM')
#############################ACTIVACION DEL SERVICIO########################################################
        hora_llegada = get_time()
        data.append(patente)
        data.append(rut)
        data.append(codigos)
        data.append(get_total(codigos))
        data.append(hora_llegada)
        data.append(hora_estimada)#revisar conflictos
        queued_services[patente] = data
        imprimir_voucher(buscar_cliente(rut, 'full')[1], buscar_cliente(rut, 'full')[3], patente, buscar_vehiculo(patente, 'full')[4], buscar_vehiculo(patente, 'full')[2], buscar_vehiculo(patente, 'full')[1], codigos, hora_estimada)
        #Problema con el descuento, como saber cual sera el precio final si se pueden agregar items al momento de entrega?
        #Mejora: Agregar una base de datos con descuentos preestablecidos
############################################################################################################
    elif opt == 2:#Comenzar
        print ("Lista de Espera")
        print queued_services.values()
        while True:
            patente = raw_input('Que patente desea ingresar al box? (0 para cancelar): ')
            patente = patente.upper()
            if patente in queued_services or patente == '0':
                break
            else:
                print("La patente ingresada no se encuentra en lista de espera.")
        if patente != '0':
            hora = get_time()
            queued_services[patente].append(hora)
            active_services[patente] = queued_services[patente]
            del queued_services[patente]
############################################################################################################        
    elif opt == 3:#Finalizar
        print ("Servicios Activos")
        print active_services.values()
        while True:
            patente = raw_input('Que patente desea sacar del box?(0 para cancelar): ')
            patente = patente.upper()
            if patente in active_services or patente == '0':
                break
            else:
                print("La patente ingresada no se encuentra en los servicios activos.")
        if patente != '0':
            hora = get_time()
            active_services[patente].append(hora)
            finished_services[patente] = active_services[patente]
            del active_services[patente]
############################################################################################################
    elif opt == 4:#Entregar
        print ("Servicios Para Entrega")
        print finished_services.values()
        while True:
            patente = raw_input('Que patente desea entregar? ')
            patente = patente.upper()
            if patente in finished_services or patente == '0':
                break
            else:
                print("La patente ingresada no se encuentra como servicio activo.")
        if patente != '0':
            finished_services[patente].append(hora)
            guardar_tiempos(finished_services[patente][2], finished_services[patente][4], finished_services[patente][5], finished_services[patente][6], finished_services[patente][7])
            nueva_venta(finished_services[patente][0], finished_services[patente][1], finished_services[patente][2], finished_services[patente][3])
            del finished_services[patente]
            
############################################################################################################
    elif opt == 5:#Resumen
        while True:
            print("Para imprimir un resumen diario, ingrese la fecha en el formato DD-MM-AA")
            fecha = raw_input("Si es el dia de hoy, ingrese 1, para volver ingrese 0: ")
            if fecha == '1' or fecha == '0':
                break
            if validar_fecha(fecha) == True:
                break
            else:
                print('Formato incorrecto, porfavor use DD-MM-AA')
        if fecha != '0':
            if fecha == '1':
                dumbvar = resumen_diario(get_date())
                if dumbvar == False:
                    print('La fecha ingresada no existe en la base de datos')
            else:
                dumbvar = resumen_diario(fecha)
                if dumbvar == False:
                    print('La fecha ingresada no existe en la base de datos')
############################################################################################################
    elif opt == 6:#Modificar info
        print("Modificar Informacion de la Base de Datos")
        opcion = raw_input('Para modificar un vehiculo ingrese 1, para clientes 2, para volver 0: ')
        if opcion == '1':
            while True:
                patente = raw_input("Ingrese Patente: ")
                patente = patente.upper()
                if validar_patente(patente) == True:
                    break
                else:
                    print('La patente ingresada no se encuentra en la base de datos o el formato es incorrecto')
            print("Para modificar marca   ingrese 1")
            print("Para modificar modelo  ingrese 2")
            print("Para modificar color   ingrese 3")
            print("Para modificar tipo    ingrese 4")
            print("Para eliminar  ingrese         5")
            print("Para volver    ingrese         0")
            accion = raw_input()
            if accion == '1':
                modificacion = raw_input("Ingrese marca: ")
                mod_vehiculo_marca(patente, modificacion)
            if accion == '2':
                modificacion = raw_input("Ingrese modelo: ")
                mod_vehiculo_modelo(patente, modificacion)
            if accion == '3':
                modificacion = raw_input("Ingrese color: ")
                mod_vehiculo_color(patente, modificacion)
            if accion == '4':
                modificacion = raw_input("Ingrese tipo: ")
                mod_vehiculo_tipo(patente, modificacion)
            if accion == '5':
                del_vehiculo(patente)
        elif opcion == '2':
            while True:
                rut = raw_input("Ingrese Rut: ")
                if validar_rut(rut) == True and buscar_cliente(rut, 'boolean') == True:
                    break
                else:
                    print('El rut ingresado no existe en la base de datos o no es incorrecto')#WTF??_todo_
            print("Para modificar telefono ingrese 1")
            print("Para modificar nombre   ingrese 2")
            print("Para modificar correo   ingrese 3")
            print("Para eliminar  ingrese          4")
            print("Para volver    ingrese          0")
            accion = raw_input()
            if accion == '1':
                modificacion = raw_input("Ingrese telefono: ")
                mod_cliente_telefono(rut, modificacion)
            if accion == '2':
                modificacion = raw_input("Ingrese nombre: ")
                mod_cliente_nombre(rut, modificacion)
            if accion == '3':
                modificacion = raw_input("Ingrese correo: ")
                mod_cliente_correo(rut, modificacion)
            if accion == '4':
                del_cliente(rut)
#_todo_ cambiar de patente a orden de trabajo (num voucher)
#_todo_ sugerir categoria en base a excel facilitado -> Pendiente Rodrigo
#_todo_ enlazar codigo y tamanno para obtener precio