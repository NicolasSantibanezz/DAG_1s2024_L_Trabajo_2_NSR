import arcpy
def script_tool(fcIn, dirout, newname):
    """Script code goes below"""
    return
if __name__ == "__main__":
    fcIn = arcpy.GetParameterAsText(0)
    dirout = arcpy.GetParameterAsText(1)
    newname = arcpy.GetParameterAsText(2)
   
    script_tool(fcIn, dirout, newname)
    arcpy.SetParameterAsText(2, "Result")

#Entorno
#Definir entorno
fcout = f"{dirout}\{newname}"
aprx = arcpy.mp.ArcGISProject("CURRENT")

#Formateo para referenciar la lista de contenidos y agregar las capas en orden
aprxMap = aprx.listMaps()[0]

#Función Export Features para mover la capa con los datos finales a la DataSet de Capas_Resultados
arcpy.conversion.ExportFeatures(fcIn, fcout)

