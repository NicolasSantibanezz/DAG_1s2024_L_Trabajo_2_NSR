import arcpy


def script_tool(fcIn, manzanas):
    """Script code goes below"""
    return
if __name__ == "__main__":
    fcIn = arcpy.GetParameterAsText(0)
    manzanas = arcpy.GetParameterAsText(1)
    script_tool(fcIn, manzanas)
    arcpy.SetParameterAsText(1, "Result")

#Entorno
#Definición de entorno
aprx = arcpy.mp.ArcGISProject("CURRENT")


#Bloque para el calculo de la variable Riesgo por manzana
arcpy.management.CalculateField(fcIn, "Riesgo", expression = "100 * ((!IND_sup! * 1) + (!IND_amb! * 2) + (!IND_metro! * 3) + (!IND_infra! * 4) - ((!IND_muni! * 1) + (!IND_com! * 3))) / (14)", field_type = "SHORT")



#Bloque para presentar en la tabla de contenidos y en la pantalla
#el Feature Class final con los valores de riesgo por cuadra ya calculados

aprxMap = aprx.listMaps()[0]
aprxMap.addDataFromPath(fcIn)
content = []
content.append(aprxMap.listLayers()[0].name)
