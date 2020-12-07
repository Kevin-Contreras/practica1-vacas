import lectura
import operaciones
import archivoJSON
""" MENU DEL SISTEMA"""

def menu():
  numero = 0;

  while(True):
    print("*********************MENU********************")
    print("1) LECTUR1A DE ARCHIVOS CSV 2) CALCULO DE DATOS 3) GENERACION DE ARCHIVOS JS 4) SALIR DEL PROGRAMA")
    print("SELECCIONE UNA OPCION DEL MENU")
    numeroMenu = input()
    casteoNumero = int(numeroMenu)
    if(casteoNumero == 1 ):
      numero=1
      print("INGRESE LA DIRECCION DEL ARCHIVO CSV")
      url = input()
      lectura.archivo(url)
    elif (casteoNumero == 2 ):
      print(numero)
      if(numero==1):
        
        operaciones.calculos(lectura.archivo(url))
        print("SE REALIZARON LOS CALCULOS CON EXITO..................")
        numero=2
      else:
        print("NO SE PUEDE REALIZAR LA OPERACION NECESITA ELEGIR LA OPCION 1")
    elif(casteoNumero == 3):
      if(numero==2):
        archivoJSON.archivojson(operaciones.calculos(lectura.archivo(url)))
      else:
        print("NO SE PUEDE REALIZAR EL ARCHIVO JSON NECESITA ELEGIR LA OPCION 2")
    elif (casteoNumero == 4):
       break
menu() 

