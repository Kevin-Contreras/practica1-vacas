def archivo(url):
  archivoUrl =  open(url)
  matrizID=[];
  matrizNombre=[];
  matrizApellidos =[];
  matrizEdad = [];
  matrizEmpleo = [];
  matrizSalario=[]
  matrizID2=[];
  matrizNombre2=[];
  matrizApellidos2 =[];
  matrizEdad2 = [];
  matrizEmpleo2 = [];
  matrizSalario2=[]
  matriz = [];
  matriz2=[]
  matrizSinRepeticion = [];
  matrizSinRepeticion2 = [];
  i=0;
  u=0;

  for linea in archivoUrl.readlines():
    linease = linea.strip("\n")
    valores = linease.split(",")
    matriz.append(valores)
    
  matriz.pop(0)
  for linea2 in matriz:
    for linea3 in linea2:
      matrizID.append(linea2[0])
      matrizNombre.append(linea2[1])
      matrizApellidos.append(linea2[2])
      matrizEdad.append(linea2[3])
      matrizEmpleo.append(linea2[4])
      matrizSalario.append(linea2[5])
      i=i+1;
    i=0;
  for linea2 in range(len(set(matrizApellidos))):
    matrizID2.append(set(matrizID))
    matrizNombre2.append( set(matrizNombre))
    matrizApellidos2.append(set(matrizApellidos))
    matrizEdad2.append(set(matrizEdad))
    matrizSalario2.append(set(matrizSalario))
  for i in matriz:
    if( i[0] not in matriz2):
      matrizSinRepeticion.append(i)
      matriz2.append(i[0])

      
 
  set(matrizNombre)
  set(matrizApellidos)
  set(matrizEdad)
  set(matrizSalario) 
  set(matrizEmpleo) 
  
  return matrizSinRepeticion      