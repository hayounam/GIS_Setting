import arcpy
import csv
import os
import datetime 


#Your SDE Location
sde_path = r"C:\Users\hnam\AppData\Roaming\Esri\ArcGISPro\Favorites\SQLServer-GISSQL23-CityMGM3.sde"
arcpy.env.workspace = sde_path
#Your Saving Location
output_csv = r"C:\Users\hnam\OneDrive - City of Montgomery\Desktop\Python\sde_layers_list.csv"
extract_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
        writer.writerow(["Dataset", "FeatureClass", "FullPath"])
    
    datasets = arcpy.ListDatasets(feature_type='feature')
    datasets = [''] + datasets if datasets else ['']
    
    for ds in datasets:
        fcs = arcpy.ListFeatureClasses(feature_dataset=ds)
        for fc in fcs:
            full_path = os.path.join(arcpy.env.workspace, ds, fc) if ds else os.path.join(arcpy.env.workspace, fc)            writer.writerow([ds if ds else "(Standalone)", fc, full_path, extract_date])

print(f"CSV Location: {output_csv}")
