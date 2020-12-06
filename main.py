import lectura
import operaciones
""" MENU DEL SISTEMA"""
def menu():
  while(True):
    print("*********************MENU********************")
    print("1) LECTURA DE ARCHIVOS CSV 2) CALCULO DE DATOS 3) GENERACION DE ARCHIVOS JS 4) SALIR DEL PROGRAMA")
    print("SELECCIONE UNA OPCION DEL MENU")
    numeroMenu = input()
    casteoNumero = int(numeroMenu)
    if(casteoNumero == 1 ):
      print("INGRESE LA DIRECCION DEL ARCHIVO CSV")
      url = input()
      lectura.archivo(url)
    elif (casteoNumero == 2 ):
      operaciones.calculos(lectura.archivo(url))
    elif(casteoNumero == 3):
      print("GENERACION DE ARCHIVO JS")
    elif (casteoNumero == 4):
       break
menu() 

