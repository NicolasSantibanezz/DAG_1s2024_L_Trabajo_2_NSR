import arcpy
def script_tool(fcIn, dirout, Outname,):
    """Script code goes below"""
    return
if __name__ == "__main__":
    fcIn = arcpy.GetParameterAsText(0)
    dirout = arcpy.GetParameterAsText(1)
    Outname = arcpy.GetParameterAsText(2)
    script_tool(fcIn, dirout, Outname)
    arcpy.SetParameterAsText(2, "Result")
 
#Definición de variables a utilizar, nombre de la entidad resultante y seleccionar el directorio
#En otras palabras definición del entorno, y el agregar feature al mapa en vista
fcOut = f"{dirout}\{Outname}"
distancia = "20 Meters"
aprx = arcpy.mp.ArcGISProject("CURRENT")
aprxMap = aprx.listMaps()[0]
#Definición de la función buffer a partir de las variables establecidas
arcpy.analysis.Buffer(fcIn, fcOut, distancia, dissolve_option="ALL")
#Bloque que importa la capa resultado al map
aprxMap.addDataFromPath(fcOut)
content = []
content.append(aprxMap.listLayers()[0].name)
