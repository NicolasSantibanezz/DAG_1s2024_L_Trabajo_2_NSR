import arcpy
def script_tool(fcIn, buffersup):
    """Script code goes below"""
    return
if __name__ == "__main__":
    fcIn = arcpy.GetParameterAsText(0)
    buffersup = arcpy.GetParameterAsText(1)
    script_tool(fcIn, buffersup)
    arcpy.SetParameterAsText(1, "Result")
#Entorno
#Definir entorno
#Entorno
#Definir entorno
aprx = arcpy.mp.ArcGISProject("CURRENT")
#Contenidos activos en el proyecto
aprxMap = aprx.listMaps()[0]
aprxMap.addDataFromPath(fcIn)
aprxMap.addDataFromPath(buffersup)
content = []
n = len(aprxMap.listLayers())
for i in list(range(0,n)):
    content.append(aprxMap.listLayers()[i].name)
#select de las manzanas que se intersectan con el buffer de supermercados en este caso
arcpy.management.SelectLayerByLocation(content[1], "INTERSECT", content[0])

#Calcular y generar valores en la nueva columna que se creará
arcpy.management.CalculateField(content[1], "IND_com", expression = "1", field_type = "LONG")

#Limpiar seleccion 
arcpy.management.SelectLayerByAttribute(content[1], "CLEAR_SELECTION")

#Hacer un switch para cambiar los otros valores
arcpy.management.SelectLayerByAttribute(content[1], where_clause = "IND_com is NULL")

#Asignar valores a cuadras que no estan dentro del área de influencia}
arcpy.management.CalculateField(content[1], "IND_com", expression = "0")