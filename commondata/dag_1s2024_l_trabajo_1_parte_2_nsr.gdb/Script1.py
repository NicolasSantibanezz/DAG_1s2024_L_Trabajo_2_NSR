import arcpy
def script_tool(fcIn, dirout, buffersup, newname):
    """Script code goes below"""
    return
if __name__ == "__main__":
    fcIn = arcpy.GetParameterAsText(0)
    dirout = arcpy.GetParameterAsText(1)
    buffersup = arcpy.GetParameterAsText(2)
    newname = arcpy.GetParameterAsText(3)
    script_tool(fcIn, dirout, buffersup, newname)
    arcpy.SetParameterAsText(3, "Result")

#Entorno
#Definir entorno
fcout = f"{dirout}\{newname}"
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
arcpy.management.CalculateField(content[1], "IND_sup", expression = "1", field_type = "LONG")

#Limpiar seleccion 
arcpy.management.SelectLayerByAttribute(content[1], "CLEAR_SELECTION")

#Hacer un switch para cambiar los otros valores
arcpy.management.SelectLayerByAttribute(content[1], where_clause = "IND_sup is NULL")

#Asignar valores a cuadras que no estan dentro del área de influencia}
arcpy.management.CalculateField(content[1], "IND_sup", expression = "0")
