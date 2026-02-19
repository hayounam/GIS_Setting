import arcpy
import csv
import os
import datetime

# Your Path
sde_path = r"C:\Users\hnam\AppData\Roaming\Esri\ArcGISPro\Favorites\SQLServer-GISSQL23-CityMGM3.sde"
arcpy.env.workspace = sde_path

today = datetime.datetime.now().strftime("%Y%m%d_%H%M")
output_csv = r"C:\Users\hnam\OneDrive - City of Montgomery\Desktop\Python\sde_layers_list_{}.csv".format(today)

extract_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("Extracting layers from:", sde_path)
print("Saving to:", output_csv)

with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    
    writer.writerow(["Dataset", "FeatureClass", "FullPath", "ExtractDate"])
    
    datasets = arcpy.ListDatasets(feature_type='feature') or ['']    
    for ds in datasets:
        fcs = arcpy.ListFeatureClasses(feature_dataset=ds)
        for fc in fcs:
            if ds:
                full_path = os.path.join(arcpy.env.workspace, ds, fc)
                dataset_name = ds
            else:
                full_path = os.path.join(arcpy.env.workspace, fc)
                dataset_name = "(Standalone)"
            
            writer.writerow([dataset_name, fc, full_path, extract_date])

print(f"Done! CSV Location: {output_csv}")
