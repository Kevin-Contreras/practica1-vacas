def archivo(url):
  archivoUrl =  open(url)
  martriz = []
 
  for linea in archivoUrl.readlines():
    print(linea)    