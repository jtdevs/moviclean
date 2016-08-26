#trabajar reportes de ventas y otros en excel
#al pasar a excel, cambiar la posicions de veces por patentes
from funciones_clientes import *
from funciones_tiempos import *
from funciones_ventas import *
from funciones_vehiculos import *
from funciones_servicios import *
from Tkinter import *

data = []
codigos = ''
queued = {}
active = {}
finished = {}
tmp = 0

def Main_screen():
	for widget in movipad.winfo_children():
		widget.destroy()
	l = Label(movipad, text='Movipad')
	l.grid(row = 0, column=0)
	b0 = Button(movipad, text='Venta Productos', command=New_screen)
	b0.grid(row = 1, column=0)
	b1 = Button(movipad, text='Ingresar Servicio', command=patente_screen)
	b1.grid(row = 1, column=1)
	b2 = Button(movipad, text='Comenzar Servicio', command=queued_screen)
	b2.grid(row = 2, column=0)
	b3 = Button(movipad, text='Finalizar Servicio', command=active_screen)
	b3.grid(row = 2, column=1)
	b4 = Button(movipad, text='Entregar Servicio', command=finished_screen)
	b4.grid(row = 3, column=0)
	b4 = Button(movipad, text='Otras Opciones', command=otros_screen)
	b4.grid(row = 3, column=1)
	salir = Button(movipad, text='Salir', command=exit)
	salir.grid(row = 4, column=0)

def otros_screen():
	for widget in movipad.winfo_children():
		widget.destroy()
	l = Label(movipad, text='Otros')
	l.grid(row = 0)
	b0 = Button(movipad, text='Resumen De Ventas', command=resumen_screen)
	b0.grid(row = 1, column=0)
	b1 = Button(movipad, text='Crear Mailist', command=mailist_screen)
	b1.grid(row = 1, column=1)
	b2 = Button(movipad, text='Modificar Vehiculos', command=mod_vehiculos_screen)
	b2.grid(row = 2, column=0)
	b3 = Button(movipad, text='Modificar Clientes', command=mod_clientes_screen)
	b3.grid(row = 2, column=1)
	volver = Button(movipad, text='Volver', command=Main_screen)
	volver.grid(row = 3, column=0)

def resumen_screen():
	for widget in movipad.winfo_children():
		widget.destroy()
	l = Label(movipad, text='Ingrese Fecha DD-MM-AA')
	l.pack()
	fecha = StringVar()
	e1 = Entry(movipad, textvariable=fecha)
	e1.pack()
	b1 = Button(movipad, text='Resumen por fecha', command=lambda: resumen_por_fecha(fecha))
	b1.pack()
	b2 = Button(movipad, text='Resumen de Hoy', command=resumen)
	b2.pack()

def resumen():
	for widget in movipad.winfo_children():
		widget.destroy()
	dumbvar = resumen_diario(get_date())
	l = Label(movipad, text=dumbvar)
	l.pack()
	volver = Button(movipad, text='Volver', command=otros_screen)
	volver.pack()

def resumen_por_fecha(fecha):
	for widget in movipad.winfo_children():
		widget.destroy()
	foo = str(fecha.get()).upper()
	dumbvar = resumen_diario(foo)
	l = Label(movipad, text=dumbvar)
	l.pack()
	volver = Button(movipad, text='Volver', command=otros_screen)
	volver.pack()

def mailist_screen():
	for widget in movipad.winfo_children():
		widget.destroy()
	l1 = Label(movipad, text='Ingresar El Minimo Numero de Asistencias')
	l1.pack()
	asistencias = StringVar()
	e1 = Entry(movipad, textvariable=asistencias)
	e1.pack()
	b1 = Button(movipad, text='Ingresar', command=lambda: mailist(asistencias))
	b1.pack()
	volver = Button(movipad, text='Volver', command=otros_screen)
	volver.pack()

def mailist(asistencias):
	foo = int(asistencias.get())
	crear_mailist(foo)
	otros_screen()

def mod_vehiculos_screen():
	for widget in movipad.winfo_children():
		widget.destroy()
	b1 = Button(movipad, text='Modificar Marca', command= mod_marca_screen)
	b1.pack()
	b2 = Button(movipad, text='Modificar Modelo', command= mod_modelo_screen)
	b2.pack()
	b3 = Button(movipad, text='Modificar Categoria', command= mod_tipo_screen)
	b3.pack()
	b4 = Button(movipad, text='Borrar Vehiculo', command= borrar_vehiculo_screen)
	b4.pack()
	volver = Button(movipad, text='Volver', command=otros_screen)
	volver.pack()

def mod_marca_screen():
	for widget in movipad.winfo_children():
		widget.destroy()
	l1 = Label(movipad, text='Ingresar la patente')
	l1.pack()
	patente = StringVar()
	e1 = Entry(movipad, textvariable=patente)
	e1.pack()
	l2 = Label(movipad, text='Ingresar la nueva marca')
	l2.pack()
	cambio = StringVar()
	e2 = Entry(movipad, textvariable=cambio)
	e2.pack()
	b1 = Button(movipad, text='Ingresar', command=lambda: mod_marca(patente, cambio))
	b1.pack()
	volver = Button(movipad, text='Volver', command=mod_vehiculos_screen)
	volver.pack()

def mod_marca(patente, cambio):
	foo = str(patente.get()).upper()
	foo1 = str(cambio.get()).upper()
	mod_vehiculo_marca(foo, foo1)
	otros_screen()

def mod_modelo_screen():
	for widget in movipad.winfo_children():
		widget.destroy()
	l1 = Label(movipad, text='Ingresar la patente')
	l1.pack()
	patente = StringVar()
	e1 = Entry(movipad, textvariable=patente)
	e1.pack()
	l2 = Label(movipad, text='Ingresar el nuevo modelo')
	l2.pack()
	cambio = StringVar()
	e2 = Entry(movipad, textvariable=cambio)
	e2.pack()
	b1 = Button(movipad, text='Ingresar', command=lambda: mod_modelo(patente, cambio))
	b1.pack()
	volver = Button(movipad, text='Volver', command=mod_vehiculos_screen)
	volver.pack()

def mod_modelo(patente, cambio):
	foo = str(patente.get()).upper()
	foo1 = str(cambio.get()).upper()
	mod_vehiculo_modelo(foo, foo1)
	otros_screen()

def mod_tipo_screen():
	for widget in movipad.winfo_children():
		widget.destroy()
	l1 = Label(movipad, text='Ingresar la patente')
	l1.pack()
	patente = StringVar()
	e1 = Entry(movipad, textvariable=patente)
	e1.pack()
	l2 = Label(movipad, text='Ingresar la nueva Categoria')
	l2.pack()
	cambio = StringVar()
	e2 = Entry(movipad, textvariable=cambio)
	e2.pack()
	b1 = Button(movipad, text='Ingresar', command=lambda: mod_tipo(patente, cambio))
	b1.pack()
	volver = Button(movipad, text='Volver', command=mod_vehiculos_screen)
	volver.pack()

def mod_tipo(patente, cambio):
	foo = str(patente.get()).upper()
	foo1 = str(cambio.get()).upper()
	mod_vehiculo_tipo(foo, foo1)
	otros_screen()

def mod_color_screen():
	for widget in movipad.winfo_children():
		widget.destroy()
	l1 = Label(movipad, text='Ingresar la patente')
	l1.pack()
	patente = StringVar()
	e1 = Entry(movipad, textvariable=patente)
	e1.pack()
	l2 = Label(movipad, text='Ingresar el nuevo color')
	l2.pack()
	cambio = StringVar()
	e2 = Entry(movipad, textvariable=cambio)
	e2.pack()
	b1 = Button(movipad, text='Ingresar', command=lambda: mod_color(patente, cambio))
	b1.pack()
	volver = Button(movipad, text='Volver', command=mod_vehiculos_screen)
	volver.pack()

def mod_color(patente, cambio):
	foo = str(patente.get()).upper()
	foo1 = str(cambio.get()).upper()
	mod_vehiculo_color(foo, foo1)
	otros_screen()

def borrar_vehiculo_screen():
	for widget in movipad.winfo_children():
		widget.destroy()
	l1 = Label(movipad, text='Ingresar la patente')
	l1.pack()
	patente = StringVar()
	e1 = Entry(movipad, textvariable=patente)
	e1.pack()
	b1 = Button(movipad, text='Ingresar', command=lambda: borrar_vehiculo(patente))
	b1.pack()
	volver = Button(movipad, text='Volver', command=mod_vehiculos_screen)
	volver.pack()

def borrar_vehiculo(patente):
	foo = str(patente.get()).upper()
	del_vehiculo(foo)
	otros_screen()

def mod_clientes_screen():
	for widget in movipad.winfo_children():
		widget.destroy()
	b1 = Button(movipad, text='Modificar Nombre', command= mod_nombre_screen)
	b1.pack()
	b2 = Button(movipad, text='Modificar Genero', command= mod_genero_screen)
	b2.pack()
	b3 = Button(movipad, text='Modificar Correo', command= mod_correo_screen)
	b3.pack()
	b4 = Button(movipad, text='Modificar Telefono', command= mod_telefono_screen)
	b4.pack()
	b5 = Button(movipad, text='Borrar Cliente', command= borrar_cliente_screen)
	b5.pack()
	volver = Button(movipad, text='Volver', command=otros_screen)
	volver.pack()

def mod_correo_screen():
	for widget in movipad.winfo_children():
		widget.destroy()
	l1 = Label(movipad, text='Ingresar el rut')
	l1.pack()
	rut = StringVar()
	e1 = Entry(movipad, textvariable=rut)
	e1.pack()
	l2 = Label(movipad, text='Ingresar el nuevo correo')
	l2.pack()
	cambio = StringVar()
	e2 = Entry(movipad, textvariable=cambio)
	e2.pack()
	b1 = Button(movipad, text='Ingresar', command=lambda: mod_correo(rut, cambio))
	b1.pack()
	volver = Button(movipad, text='Volver', command=mod_clientes_screen)
	volver.pack()

def mod_correo(rut, cambio):
	foo = str(rut.get()).upper()
	foo1 = str(cambio.get()).upper()
	mod_cliente_correo(foo, foo1)
	otros_screen()

def mod_genero_screen():
	for widget in movipad.winfo_children():
		widget.destroy()
	l1 = Label(movipad, text='Ingresar el rut')
	l1.pack()
	rut = StringVar()
	e1 = Entry(movipad, textvariable=rut)
	e1.pack()
	b1 = Button(movipad, text='Cambiar', command=lambda: mod_genero(rut))
	b1.pack()
	volver = Button(movipad, text='Volver', command=mod_clientes_screen)
	volver.pack()

def mod_nombre_screen():
	for widget in movipad.winfo_children():
		widget.destroy()
	l1 = Label(movipad, text='Ingresar el rut')
	l1.pack()
	rut = StringVar()
	e1 = Entry(movipad, textvariable=rut)
	e1.pack()
	l2 = Label(movipad, text='Ingresar el nuevo nombre')
	l2.pack()
	cambio = StringVar()
	e2 = Entry(movipad, textvariable=cambio)
	e2.pack()
	b1 = Button(movipad, text='Ingresar', command=lambda: mod_nombre(rut, cambio))
	b1.pack()
	volver = Button(movipad, text='Volver', command=mod_clientes_screen)
	volver.pack()

def mod_nombre(rut, cambio):
	foo = str(rut.get()).upper()
	foo1 = str(cambio.get()).upper()
	mod_cliente_nombre(foo, foo1)
	otros_screen()

def mod_telefono_screen():
	for widget in movipad.winfo_children():
		widget.destroy()
	l1 = Label(movipad, text='Ingresar el rut')
	l1.pack()
	rut = StringVar()
	e1 = Entry(movipad, textvariable=rut)
	e1.pack()
	l2 = Label(movipad, text='Ingresar el nuevo telefono')
	l2.pack()
	cambio = StringVar()
	e2 = Entry(movipad, textvariable=cambio)
	e2.pack()
	b1 = Button(movipad, text='Ingresar', command=lambda: mod_telefono(rut, cambio))
	b1.pack()
	volver = Button(movipad, text='Volver', command=mod_clientes_screen)
	volver.pack()

def mod_telefono(rut, cambio):
	foo = str(rut.get()).upper()
	foo1 = str(cambio.get()).upper()
	mod_cliente_telefono(foo, foo1)
	otros_screen()

def borrar_cliente_screen():
	for widget in movipad.winfo_children():
		widget.destroy()
	l1 = Label(movipad, text='Ingresar el rut')
	l1.pack()
	rut = StringVar()
	e1 = Entry(movipad, textvariable=rut)
	e1.pack()
	b1 = Button(movipad, text='Ingresar', command=lambda: borrar_cliente(rut))
	b1.pack()
	volver = Button(movipad, text='Volver', command=mod_vehiculos_screen)
	volver.pack()

def borrar_cliente(rut):
	foo = str(rut.get()).upper()
	del_cliente(foo)
	otros_screen()

#####################################################################################################
def patente_screen():
	for widget in movipad.winfo_children():
		widget.destroy()
	l1 = Label(movipad, text='Ingresar Patente Vehiculo')
	l1.pack()
	patente = StringVar()
	e1 = Entry(movipad, textvariable=patente)
	e1.pack()
	siguiente = Button(movipad, text='Siguiente', command = lambda: check_patente(patente))
	siguiente.pack()
	volver = Button(movipad, text='Volver', command=Main_screen)
	volver.pack()

def check_patente(patente):
	foo = str(patente.get()).upper()
	if buscar_vehiculo(foo) == False:
		tomar_datos_vehiculo(patente)
	else:
		veces_vehiculo(foo)
		global data
		data += datos_vehiculo(foo)
		cliente_screen(patente)

def tomar_datos_vehiculo(patente):
	for widget in movipad.winfo_children():
		widget.destroy()
	scrollbar = Scrollbar(movipad)
	scrollbar.pack(side=RIGHT, fill=Y)
	l1 = Label(movipad, text='Tomar datos vehiculo')
	l1.pack()
	l2 = Label(movipad, text='Marca:')
	l2.pack()
	marca = StringVar()
	e1 = Entry(movipad, textvariable=marca)
	e1.pack()
	l3 = Label(movipad, text='Modelo:')
	l3.pack()
	modelo = StringVar()
	e2 = Entry(movipad, textvariable=modelo)
	e2.pack()
	l4 = Label(movipad, text='Color:')
	l4.pack()
	color = StringVar()
	e3 = Entry(movipad, textvariable=color)
	e3.pack()
	l5 = Label(movipad, text='Categoria:')
	l5.pack()
	tipo = StringVar()
	e4 = Entry(movipad, textvariable=tipo)
	e4.pack()
	siguiente = Button(movipad, text='Siguiente', command = lambda: add_vehiculo(patente, marca, modelo, color, tipo))
	siguiente.pack()
	volver = Button(movipad, text='Volver', command =Main_screen)
	volver.pack()

def add_vehiculo(patente, marca, modelo, color, tipo):
	foo1 = str(patente.get()).upper()
	foo2 = str(marca.get()).upper()
	foo3 = str(modelo.get()).upper()
	foo4 = str(color.get()).upper()
	foo5 = str(tipo.get()).upper()
	crear_vehiculo(foo1,foo2,foo3,foo4,foo5)
	global data
	data += datos_vehiculo(foo1)
	cliente_screen(patente)
#####################################################################################################

def cliente_screen(patente):
	for widget in movipad.winfo_children():
		widget.destroy()
	l1 = Label(movipad, text='Ingresar Rut Cliente')
	l1.pack()
	rut = StringVar()
	e1 = Entry(movipad, textvariable=rut)
	e1.pack()
	siguiente = Button(movipad, text='Siguiente', command = lambda: check_cliente(rut, patente))
	siguiente.pack()
	volver = Button(movipad, text='Volver', command=Main_screen)
	volver.pack()

def check_cliente(rut, patente):
	foo = str(rut.get()).upper()
	foo1 = str(patente.get()).upper()
	if validar_rut(foo) == 1:
		if buscar_cliente(foo) == False:
			tomar_datos_cliente(rut, patente)
		else:
			veces_cliente(foo)
			vehiculo_a_cliente(foo1, foo)
			global data
			data += datos_cliente(foo)
			servicios_screen()
	else:
		cliente_screen(patente)#_todo_patanalla de error

def tomar_datos_cliente(rut, patente):
	for widget in movipad.winfo_children():
		widget.destroy()
	l1 = Label(movipad, text='Tomar datos cliente')
	l1.pack()
	espacio = Label(movipad, text='')
	espacio.pack()
	l2 = Label(movipad, text='Nombre:')
	l2.pack()
	nombre = StringVar()
	e1 = Entry(movipad, textvariable=nombre)
	e1.pack()
	l3 = Label(movipad, text='Genero:')
	l3.pack()
	genero = StringVar()
	e2 = Entry(movipad, textvariable=genero)
	e2.pack()
	l4 = Label(movipad, text='Correo:')
	l4.pack()
	correo = StringVar()
	e3 = Entry(movipad, textvariable=correo)
	e3.pack()
	l5 = Label(movipad, text='Telefono:')
	l5.pack()
	telefono = StringVar()
	e4 = Entry(movipad, textvariable=telefono)
	e4.pack()
	siguiente = Button(movipad, text='Siguiente', command = lambda: add_cliente(rut, nombre, genero, correo, telefono, patente))
	siguiente.pack()
	volver = Button(movipad, text='Volver', command =Main_screen)
	volver.pack()

def add_cliente(rut, nombre, genero, correo, telefono, patente):
	foo1 = str(rut.get()).upper()
	foo2 = str(nombre.get()).upper()
	foo3 = str(genero.get()).upper()
	foo4 = str(correo.get()).upper()
	foo5 = str(telefono.get()).upper()
	foo6 = str(patente.get()).upper()
	crear_cliente(foo1,foo2,foo3,foo4,foo5,foo6)
	global data
	data += datos_cliente(foo1)
	servicios_screen()
#################################################################

def servicios_screen():
	for widget in movipad.winfo_children():
		widget.destroy()
	l1 = Label(movipad, text='Ingrese Un servicio o producto')
	l1.pack()
	codigo = StringVar()
	e1 = Entry(movipad, textvariable=codigo)
	e1.pack()
	ingresar = Button(movipad, text='Ingresar', command = lambda: add_service(codigo))
	ingresar.pack()
	siguiente = Button(movipad, text='Siguiente', command = lambda: ingresar_hora())
	siguiente.pack()

def servicio_invalido():
	for widget in movipad.winfo_children():
		widget.destroy()
	l1 = Label(movipad, text='Ingrese un codigo de servicio o producto')
	l1.pack()
	codigo = StringVar()
	e1 = Entry(movipad, textvariable=codigo)
	e1.pack()
	l1 = Label(movipad, text='El codigo ingresado no existe')
	l1.pack()
	ingresar = Button(movipad, text='Ingresar', command = lambda: add_service(codigo))
	ingresar.pack()
#_todo_ poder eliminar servicios o ingresar mas de uno a la vez
def add_service(codigo):
	foo = str(codigo.get()).upper()
	if validar_codigo(foo) == True:
		global codigos
		codigos += foo+','
		servicios_screen()
	else:
		servicio_invalido()

def ingresar_hora():
	for widget in movipad.winfo_children():
		widget.destroy()
	l1 = Label(movipad, text='Ingrese hora estimada entrega (HH:MM)')
	l1.pack()
	hora_estimada = StringVar()
	e1 = Entry(movipad, textvariable=hora_estimada)
	e1.pack()
	ingresar = Button(movipad, text='Ingresar', command = lambda: finalizar_ingreso(hora_estimada))
	ingresar.pack()

def finalizar_ingreso(hora_estimada):
	global codigos
	global data
	global queued
	data.append(codigos.strip(','))
	codigos = ''
	foo = str(hora_estimada.get()).upper()
	hora_llegada = get_time()
	data.append(foo)
	data.append(hora_llegada)
	OT = voucher_number()
	print data
	imprimir_voucher(data[6], data[9], data[0], data[4], data[2], data[1], data[10], data[11], 0, OT)
	queued[OT] = data
	data = []
	Main_screen()
#bug no ve diferencias de horas ni nombres de productos al annadir mas de un elemento a la cola
#Para las ventanas de colas, annadir un titular, y la palabra OT antes del codigo
def queued_screen():
	def selection(evt):
		global tmp
		tmp = str((listbox.get(ACTIVE)))
	for widget in movipad.winfo_children():
		widget.destroy()
	listbox = Listbox(movipad)
	listbox.pack()
	for item in queued:
		listbox.insert(END, item)
	listbox.bind('<<ListboxSelect>>', selection)
	siguiente = Button(movipad, text='Siguiente', command = lambda: display_queue_element(tmp))
	siguiente.pack()
	volver = Button(movipad, text='Volver', command=Main_screen)
	volver.pack()

def display_queue_element(selection):
	global queued
	for widget in movipad.winfo_children():
		widget.destroy()
	Label(movipad, text=('Hora Estimada: '+queued[selection][11])).pack()
	Label(movipad, text='Servicios/Productos:').pack()
	for key in queued[selection][10].split(','):
		if key != '':
			Label(movipad, text=get_name(key)).pack()
	siguiente = Button(movipad, text='Siguiente', command = lambda: queue_to_active(selection))
	siguiente.pack()
	volver = Button(movipad, text='Volver', command=queued_screen)
	volver.pack()

def queue_to_active(selection):
	global active
	global queued
	time = get_time()
	queued[selection].append(time)
	active[selection] = queued[selection]
	del queued[selection]
	Main_screen()

def active_screen():
	def selection(evt):
		global tmp
		tmp = str((listbox.get(ACTIVE)))
	for widget in movipad.winfo_children():
		widget.destroy()
	listbox = Listbox(movipad)
	listbox.pack()
	for item in active:
		listbox.insert(END, item)
	listbox.bind('<<ListboxSelect>>', selection)
	siguiente = Button(movipad, text='Siguiente', command = lambda: display_active_element(tmp))
	siguiente.pack()
	volver = Button(movipad, text='Volver', command=Main_screen)
	volver.pack()

def display_active_element(selection):
	global active
	for widget in movipad.winfo_children():
		widget.destroy()
	Label(movipad, text=('Hora Estimada: '+active[selection][11])).pack()
	Label(movipad, text='Servicios/Productos:').pack()
	for key in active[selection][10].split(','):
		if key != '':
			Label(movipad, text=get_name(key)).pack()
	siguiente = Button(movipad, text='Siguiente', command = lambda: active_to_finished(selection))
	siguiente.pack()
	volver = Button(movipad, text='Volver', command=active_screen)
	volver.pack()

def active_to_finished(selection):
	global finished
	global active
	time = get_time()
	active[selection].append(time)
	finished[selection] = active[selection]
	del active[selection]
	Main_screen()

def finished_screen():
	def selection(evt):
		global tmp
		tmp = str((listbox.get(ACTIVE)))
	for widget in movipad.winfo_children():
		widget.destroy()
	listbox = Listbox(movipad)
	listbox.pack()
	for item in finished:
		listbox.insert(END, item)
	listbox.bind('<<ListboxSelect>>', selection)
	siguiente = Button(movipad, text='Siguiente', command = lambda: display_finished_element(tmp))
	siguiente.pack()
	volver = Button(movipad, text='Volver', command=Main_screen)
	volver.pack()

def display_finished_element(selection):
	global finished
	for widget in movipad.winfo_children():
		widget.destroy()
	Label(movipad, text=('Hora Estimada: '+finished[selection][11])).pack()
	Label(movipad, text='Servicios/Productos:').pack()
	for key in finished[selection][10].split(','):
		if key != '':
			Label(movipad, text=get_name(key)).pack()
	siguiente = Button(movipad, text='Finalizar', command = lambda: finished_to_selling(selection))
	siguiente.pack()
	volver = Button(movipad, text='Volver', command=finished_screen)
	volver.pack()

def finished_to_selling(selection):
	global finished
	time = get_time()
	finished[selection].append(time)
	print finished[selection]
	guardar_tiempos(finished[selection][10], finished[selection][12], finished[selection][13], finished[selection][14], finished[selection][15])
	nueva_venta(finished[selection][0],finished[selection][5],finished[selection][10],get_total(finished[selection][10]))
	del finished[selection]
	Main_screen()

def New_screen():
    for widget in movipad.winfo_children():
    	widget.destroy()
    l1 = Label(movipad, text='Esta es una segunda pantalla')
    l1.pack()
    volver = Button(movipad, text='Volver', command =Main_screen)
    volver.pack()

movipad = Tk()
movipad.title("Movipad V1.0")
#movipad.geometry('240x160')
#scrollbar = Scrollbar(master)
#scrollbar.pack(side=RIGHT, fill=Y)
Main_screen()
movipad.mainloop()