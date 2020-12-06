def calculos (url):
  contador=0;
  contador2=0;
  contador3 =0;
  promedioEdad=0;
  promedioSalario=0;
  trabajos =[]
  trabajo2 = []
  arregloFinal1 = []
  arregloCandidatos = []
  arregloEdad =[]
  arregloSalario =[]
  todoslosDatos = []

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
        contador3= contador3 + int(arreglo3[5].strip("\n"))
        promedioSalario = contador3/contador
        
    """ PERSONAS REGISTRADAS PARA CADA PUESTO"""
    arregloCandidatos.append(contador)
    arregloEdad.append(promedioEdad)  
    arregloSalario.append(promedioSalario)
    contador=0
    contador2=0;
    promedioEdad=0;
    contador3=0;
    promedioSalario=0;
  todoslosDatos.append(arregloCandidatos)
  todoslosDatos.append(arregloEdad)
  todoslosDatos.append(arregloSalario)
  todoslosDatos.append(trabajo2)
  """---------------------------------------"""
  print(todoslosDatos)
  return todoslosDatos
   

