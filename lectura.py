def archivo(url):
  archivoUrl =  open(url)
  matriz = []
  for linea in archivoUrl.readlines():
    valores = linea.split(",")
    matriz.append(valores)
  matriz.pop(0)
  return matriz      