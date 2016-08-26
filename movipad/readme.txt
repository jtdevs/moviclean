Solucion para el problema de la diferenciacion servicios/productos:

El menu principal debera ser reformulado de la siguiente manera
	Productos
	Serivicios
	Ordenes de Trabajo
	Base de Datos

Productos:
	En esta seccion se daran tres opciones:
		Venta Directa
		Agregar a una OT
		Volver

Servicios:
	En esta seccion no habran opciones salvo la opcion de cancelar en todo momento, en cambio, se seguira el siguiente algoritmo:
		Ingresar la patente, si no existe en base de datos, agregar el vehiculo. Si existe, pasar sus datos al flujo del programa.
		Ingresar el rut del cliente. Si no existe en la base de datos, agregarlo. Si existe, pasar sus datos al flujo del programa.
		*OJO* Si el cliente no desea formar parte de la base de datos, se debera ingresar rut '0', y por tanto no agregar ningun dato
			  de cliente a la base de datos, aunque de todas formas se debera solicitar telefono de contacto, nombre y apellido y 
			  pasarlos al flujo del programa.
		Ingresar los codigos de servicio.
		Convenir hora de entrega del vehiculo y pasarla al flujo del programa.
		Imprimir el Voucher de recepcion.
		Asignar los datos adquiridos a una nueva orden de trabajo y agregar a la cola a espera de ser ingresado a un box.

Ordenes de Trabajo:
	En esta seccion se desplegara una lista con todas las ordenes de trabajo activas, las patentes asociadas y su estado (En cola, En box
	 o Para Entrega).
	 Por cada orden de trabajo desplegada, en caso de ser seleccionada se mostrara un menu con las distintas acciones que se pueden ejecutar
	 sobre ella. En el unico momento en que se puede cancelar una orden de trabajo es mientras se encuentre 'En cola'.

Base de Datos:
	Seccion en la cual se implementaran todas las funcionalidades secundarias solicitadas y las funcionalidades inherentes al manejo y mantencion
	de una bas de datos.