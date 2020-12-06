def calculos (url):
  contador=0;
  contador2=0;
  promedioEdad=0;
  trabajos =[]
  trabajo2 = []
  arregloFinal1 = []
  arregloCandidatos = []
  arregloEdad =[]

  for arreglo in url:
    trabajos.append(arreglo[4])
  for objecto in set(trabajos):
    trabajo2.append(objecto)

  for arreglo2 in trabajo2:
    for arreglo3 in url:
      if(arreglo2 == arreglo3[4]):
        arregloFinal1.append(arreglo3)
        contador=contador+1;
        contador2= contador2 + int(arreglo3[3])
        promedioEdad = contador2/contador
    """ PERSONAS REGISTRADAS PARA CADA PUESTO"""
    arregloCandidatos.append(contador)
    arregloEdad.append(promedioEdad)  
    """---------------------------------------"""

    contador=0
    contador2=0;
    promedioEdad=0;
  print(arregloFinal1)
  print(arregloCandidatos)
  print(arregloEdad)

   

