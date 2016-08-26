from openpyxl import load_workbook
#Verifica la existencia de un codigo en la base de datos
def validar_codigo(codigo):
    archivo = open('serviciosDB.txt', 'r')
    for line in archivo:
        if str(codigo) == line.split('/')[0]:
            return True
    else:
        return False

#Para una lista de codigos en el formato 'codigo1,codigo2,codigo3,...,codigoN' retorna el valor total
def get_total(codigos):
    code_values = codigos.split(',')
    total = 0
    for n in range(len(code_values)):
        total += get_price(code_values[n])
    return total

def get_total_list(code_values):
    total = 0
    for n in range(len(code_values)):
        total += get_price(code_values[n])
    return total

#Para un codigo en particular, obtiene el valor monetario desde la base de datos
def get_price(codigo):
    archivo = open('serviciosDB.txt', 'r')
    for line in archivo:
        elements = line.split('/')
        if elements[0] == str(codigo):
            return int(elements[2])
    else:
        return 0

#serviciosDB.txt -> codigo_corto/codigo_venta/glosa/tamanno/tipo/precio

#Lee un archivo 'precios.xlsx' con el formato Codigo-Descripcion-Precio y actualiza dichas variables en la base de datos
#RESTRICCION: NO PUEDE USARSE EL CARCATER / EN LA DESCRIPCION
def actualizar_serviciosDB():
    wb = load_workbook(filename='precios.xlsx', read_only=True)
    ws = wb['Sheet 1']
    archivo = open('serviciosDB.txt', 'w')
    for row in ws.rows:
        tmp = ''
        for i in range(6):
            tmp+=str(row[i].value)
            if i != 5:
                tmp += '/'
        tmp += '\n'
        archivo.write(tmp)
    archivo.close()

def get_name(codigo):
    archivo = open('serviciosDB.txt', 'r')
    for line in archivo:
        elements = line.split('/')
        if elements[0] == str(codigo):
            return elements[1]
    else:
        return 'Not found'