import json
import os
def archivojson(url):
  cadena =""
  cadena2 = ""
  cadena3=""
  for trabajo in range(len(url[3])):
    diccionario  = {url[3][trabajo]:{ 'Candidatos':url[0][trabajo],'Edad Promedio':url[1][trabajo],'Pretension Salarial':url[2][trabajo]}}
    j = json.dumps(diccionario,sort_keys=True, indent=7)
    verdad = str(j)[1:-1]+","
    cadena =  cadena + verdad
  archivo = open("archivo.json","w")
  archivo.write("{"+cadena.strip(",")+"}")
  archivo.close()
  os.system("archivo.json")