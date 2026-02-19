# GIS_Setting

This repository contains:
- Static web files (HTML) for GIS Setting
- Python scripts and Jupyter notebooks designed for use in **ArcGIS Pro Notebooks**

**Note**: The Python code here is **independent** of the web files. It is meant to be copied/pasted or imported into ArcGIS Pro for data processing, polling, analysis, or automation tasks.

## Repository Structure



## Python Code Usage (ArcGIS Pro)

These scripts/notebooks are intended for **ArcGIS Pro Notebooks**.

### How to Use

1. **Open ArcGIS Pro**
2. Go to the **Catalog** pane → Right-click **Notebooks** → **New Notebook** (or **Add Notebook**)
3. **Option A: Use .ipynb directly** (recommended)
   - Download the `.ipynb` file from this repo (right-click → Save link as...)
   - In ArcGIS Pro: Add the downloaded notebook
4. **Option B: Copy-paste code**
   - Open `.py` or `.ipynb` in GitHub (click file → Raw → copy all)
   - Paste into a new or existing notebook cell
5. Run the cells sequentially.  
   ArcGIS Pro's default Python environment (`arcgispro-py3`) already includes `arcpy`, so most GIS functions work out of the box.

### Dependencies

- ArcGIS Pro (with Python environment)
- Any extra packages → install via **Python Package Manager** in ArcGIS Pro or conda  
  (see `requirements.txt` for non-arcpy packages)

### Important Notes

- These scripts are **not** meant to run on GitHub or as web backends.
- They are standalone tools for desktop GIS workflows in ArcGIS Pro.
- If you need real-time polling in a web app, consider moving Python logic to Flask/FastAPI on Vercel/Render/etc.
