from funciones_tiempos import*
from funciones_servicios import*
import socket

printer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
printer.connect(("192.168.2.1", 40))
############################################################################################################
#OT.txt -> OT
def voucher_number():
    voucher = open('OT.txt', 'r')
    voucher_number = int(voucher.readline().rstrip())
    voucher.close()
    voucher = open('OT.txt', 'w')
    voucher.write(str(voucher_number+1))
    voucher.close()
    return str(voucher_number)

############################################################################################################
#ventasDB.txt -> DD-MM-AA/HH:MM/rut/patente/codigo/monto

#Annade una nueva venta a la base de datos
def nueva_venta(patente, rut, codigos, total):
    tmp = ''
    fecha = get_date()
    tmp += fecha+'/'
    hora = get_time()
    tmp += hora+'/'
    tmp += str(patente)+'/'
    tmp += str(rut)+'/'
    tmp += str(codigos)+'/'
    tmp += str(total)+'\n'
    archivo = open('ventasDB.txt', 'a')
    archivo.write(tmp)
    archivo.close()
    return None

#_todo_->preguntar
def buscar_oferta():
    #ingresar un monto de descuento opcional
    pass

#Imprime el resumen de ventas diario
#_todo_ pasar de .txt a xlsx
def resumen_diario(fecha):#fecha en el formato DD-MM-AA
    servicios = {}
    total_diario = 0
    archivo = open('ventasDB.txt', 'r')
    existe_fecha = False
    for line in archivo:
        datos = line.split('/')
        if fecha == datos[0]:
            existe_fecha = True
            total_diario += int(datos[5])
            codigos = datos[4].split(',')
            for n in range(len(codigos)):
                if codigos[n] not in servicios:
                    servicios[codigos[n]] = 1
                else:
                    servicios[codigos[n]] += 1
    archivo.close()
    if existe_fecha == True:
        resumen = open('resumen-'+fecha+'.txt', 'w')
        print('Resumen '+fecha)
        resumen.write('Resumen '+fecha+'\n')
        print('Cod      Cant')
        resumen.write('Cod  Descripcion                       Cant'+'\n')
        for cod, cont in servicios.items():
            descripcion = get_name(cod)
            espacios = ' '*(33-len(descripcion))
            print (cod+' '+descripcion+espacios+str(cont))
            resumen.write(cod+' '+descripcion+espacios+str(cont)+'\n')
        print ('Ingreso Total:'+str(total_diario))
        resumen.write('Ingreso Total:'+str(total_diario))
        resumen.close()
        return 'Resumen Creado!'
    else:
        return 'Aun no existen registros para la fecha ingresada'

#Imprime el voucher de recepcion
def imprimir_voucher(nombre, telefono, patente, tipo, modelo, marca, servicios, h_estimada, descuento, OT):
    #COPIA CLIENTE
    printer.send('mayus')
    printer.send("           MOVICLEAN            ")
    printer.send('minus')
    printer.send("   AVDA. LOMAS DE LA LUZ 4650   ")
    printer.send("  ARAUCO PREMIUM OUTLET CURAUMA ")
    printer.send("  CEL./WHATS'APP +56-9/94920612 ")
    printer.send("        www.moviclean.cl        ")
    printer.send("    Facebook Moviclean Chile    ")
    printer.send("    Twitter Moviclean Chile     ")
    printer.send("________________________________")
    printer.send("   VOUCHER RECEPCION VEHICULO   ")
    voucher_numbr = OT
    espacios = (6-len(voucher_numbr))*'0'+voucher_numbr
    printer.send("           # "+espacios+"             ")#letras grandes
    printer.send("________________________________")
    printer.send("        ***IMPORTANTE***        ")#letras grandes
    printer.send("     CONSERVE Y NO EXTRAVIE     ")
    printer.send("        ESTE COMPROBANTE!       ")
    printer.send("   Le sera exigido al momento   ")
    printer.send("     de retirar su vehiculo     ")
    printer.send("________________________________")
    day = get_dayofweek()
    date = get_date()
    time = get_time()
    printer.send(day+' '+date+'         '+time)
    printer.send("Hora aprox. entrega        "+h_estimada)
    espacios = ' '*(32-(len(nombre)+6))
    printer.send("Nombre"+espacios+nombre)
    espacios = ' '*(32-(len(telefono)+8))
    printer.send("Telefono"+espacios+telefono)
    espacios = ' '*(32-(len(patente)+7))
    printer.send("Patente"+espacios+patente)
    espacios = ' '*(32-(len(marca)+5))
    printer.send("Marca"+espacios+marca)
    espacios = ' '*(32-(len(modelo)+6))
    printer.send("Modelo"+espacios+modelo)
    espacios = ' '*(32-(len(tipo)+9))
    printer.send("Categoria"+espacios+tipo)
    printer.send("                                ")
    printer.send("COD./ CANT./ SERVICIOS/ SUBTOTAL")
    printer.send("________________________________")
    servicios_copy = servicios.split(',')
    while len(servicios_copy) != 0:
        codigo = servicios_copy[0]
        linea_voucher = str(codigo)+'    '
        count = str(servicios_copy.count(codigo))
        precio = str(get_price(codigo)*int(count))
        if len(count) == 1:
            count = '0'+count
        linea_voucher += count+'               $'+' '*(7-len(precio))+precio
        printer.send(linea_voucher)
        service_name = get_name(codigo)
        printer.send(service_name+' '*(32-len(service_name)))
        printer.send("--------------------------------")
        while codigo in servicios_copy:
            servicios_copy.remove(codigo)
    if str(descuento) != '0':
        printer.send("DESCUENTO ESPECIAL       $"+' '*(6-len(str(descuento)))+str(descuento))
    total_voucher = str(get_total(servicios)-int(descuento))
    printer.send("TOTAL A PAGAR            $"+' '*(6-len(total_voucher))+total_voucher)
    printer.send("                                ")
    printer.send("        DECLARACION LEGAL       ")
    printer.send("________________________________")
    printer.send("SE   DEJA   EXPRESA   CONSTANCIA")
    printer.send("QUE     MOVICLEAN     LTDA.   NO")
    printer.send("SE   HACE    RESPONSABLE    BAJO")
    printer.send("NINGUNA  CIRCUNSTANCIA  POR  LAS")
    printer.send("PERTENENCIAS QUE   SE ENCUENTREN")
    printer.send("AL INTERIOR  DEL  VEHICULO. PARA")
    printer.send("AQUELLAS   PERTENENCIAS   QUE EL")
    printer.send("CLIENTE   CONSIDERE   DE   VALOR")
    printer.send("DEBERA  SOLICITAR  AL SUPERVISOR")
    printer.send("UNA  CAJA CONTENEDORA CON SELLOS")
    printer.send("DE  SEGURIDAD  PARA  EL GUARDADO")
    printer.send("SEGURO   DE   ELLAS;   CAJA  QUE")
    printer.send("PERMANECERA  DENTRO DEL VEHICULO")
    printer.send("DURANTE  TODO  EL   PROCESO   DE")
    printer.send("LIMPIEZA.                       ")
    printer.send("                                ")
    printer.send("       ***COPIA CLIENTE***      ")
    printer.send("________________________________")
    printer.send("lf")
    printer.send("lf")
    ############################################################################################################
    ############################################################################################################
    #COPIA MOVICLEAN
    printer.send("lf")
    printer.send("   VOUCHER RECEPCION VEHICULO   ")
    espacios = (6-len(voucher_numbr))*'0'+voucher_numbr
    printer.send("           # "+espacios+"             ")#letras grandes
    printer.send("________________________________")
    printer.send("        ***IMPORTANTE***        ")#letras grandes
    printer.send("     CONSERVE Y NO EXTRAVIE     ")
    printer.send("        ESTE COMPROBANTE!       ")
    printer.send("   Le sera exigido al momento   ")
    printer.send("     de retirar su vehiculo     ")
    printer.send("________________________________")
    printer.send(day+' '+date+'         '+time)
    printer.send("Hora aprox. entrega        "+h_estimada)
    espacios = ' '*(32-(len(nombre)+6))
    printer.send("Nombre"+espacios+nombre)
    espacios = ' '*(32-(len(telefono)+8))
    printer.send("Telefono"+espacios+telefono)
    espacios = ' '*(32-(len(patente)+7))
    printer.send("Patente"+espacios+patente)
    espacios = ' '*(32-(len(marca)+5))
    printer.send("Marca"+espacios+marca)
    espacios = ' '*(32-(len(modelo)+6))
    printer.send("Modelo"+espacios+modelo)
    espacios = ' '*(32-(len(tipo)+9))
    printer.send("Categoria"+espacios+tipo)
    printer.send("                                ")
    printer.send("COD./ CANT./ SERVICIOS/ SUBTOTAL")
    printer.send("________________________________")
    servicios_copy = servicios.split(',')
    while len(servicios_copy) != 0:
        codigo = servicios_copy[0]
        linea_voucher = '|'+str(codigo)+'    '
        count = str(servicios_copy.count(codigo))
        precio = str(get_price(codigo)*int(count))
        if len(count) == 1:
            count = '0'+count
        linea_voucher += count+'               $'+' '*(7-len(precio))+precio
        printer.send(linea_voucher)
        service_name = get_name(codigo)
        printer.send(service_name+' '*(32-len(service_name)))
        printer.send("--------------------------------")
        while codigo in servicios_copy:
            servicios_copy.remove(codigo)
    if str(descuento) != '0':
        printer.send("DESCUENTO ESPECIAL       $"+' '*(6-len(str(descuento)))+str(descuento))
    total_voucher = str(get_total(servicios)-int(descuento))
    printer.send("TOTAL A PAGAR            $"+' '*(6-len(total_voucher))+total_voucher)
    printer.send("                                ")
    printer.send("        DECLARACION LEGAL       ")
    printer.send("________________________________")
    printer.send("SE   DEJA   EXPRESA   CONSTANCIA")
    printer.send("QUE     MOVICLEAN     LTDA.   NO")
    printer.send("SE   HACE    RESPONSABLE    BAJO")
    printer.send("NINGUNA  CIRCUNSTANCIA  POR  LAS")
    printer.send("PERTENENCIAS QUE   SE ENCUENTREN")
    printer.send("AL INTERIOR  DEL  VEHICULO. PARA")
    printer.send("AQUELLAS   PERTENENCIAS   QUE EL")
    printer.send("CLIENTE   CONSIDERE   DE   VALOR")
    printer.send("DEBERA  SOLICITAR  AL SUPERVISOR")
    printer.send("UNA  CAJA CONTENEDORA CON SELLOS")
    printer.send("DE  SEGURIDAD  PARA  EL GUARDADO")
    printer.send("SEGURO   DE   ELLAS;   CAJA  QUE")
    printer.send("PERMANECERA  DENTRO DEL VEHICULO")
    printer.send("DURANTE  TODO  EL   PROCESO   DE")
    printer.send("LIMPIEZA.                       ")
    printer.send("                                ")
    printer.send("                                ")
    printer.send("                                ")
    printer.send("        _________________       ")
    printer.send("          FIRMA CLIENTE         ")
    printer.send("                                ")
    printer.send("       ***COPIA EMPRESA***      ")
    printer.send("lf")
    printer.send("lf")
    return None