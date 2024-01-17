import pandas as pd
import geopandas as gpd
import ee
import geemap


## EXPORTAR EE.FEATURECOLLECTION PARA O GOOGLE DRIVE NO FORMATO DETERMINADO
def exportar_vetor_GEE(fc, folder, description, format_export):
    try:
        export_options = {
                      'collection': fc,
                      'folder': folder,
                      'description': description,
                      'fileFormat': format_export #'GEOJSON'
                     }

        # Inicie o processo de exportação
        task = ee.batch.Export.table.toDrive(**export_options)
        task.start()

        print('Exportação completa')
    
    except Exception as e:
        print('Erro:', e)
