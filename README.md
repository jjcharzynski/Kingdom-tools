# Kingdom Tools

This repository is a collection of python scrpts that were written to help a Kingdom user complete workflows easier. 

# Table of Contents
- [ShapefileToKingdomPolygon](#ShapefileToKingdomPolygon)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Input Parameters](#input-parameters)
- [Output](#output)
- [References](#references)

## ShapefileToKingdomPolygon

This Python script converts shapefiles to a CSV format suitable for importing into the Kingdom Software (S&P Global IHS Kingdom, seismic and geological interpretation sotfware.) as planimeter polygons. It takes shapefiles located in a folder with a specified EPSG coordinate system and converts them into the Kingdom Project coordinate system, saving the results in a CSV file. 

### Prerequisites

Before using this script, ensure you have the following dependencies installed:

- [PyShp (shapefile)](https://pypi.org/project/pyshp/)
- [PyProj (Proj)](https://pypi.org/project/pyproj/)
- Python modules: `os`, `csv`

Additionally, you must set the correct coordinate systems using EPSG codes. You can find the EPSG code for your coordinate system on websites like [prj2epsg.org](http://prj2epsg.org/search) or [spatialreference.org](https://spatialreference.org/ref/epsg/).

### Usage

1. Place all the shapefiles you want to convert into a single folder.
2. Modify the script to specify the input and output EPSG codes, CSV filename, and the location of the name field in the record (first field is 0).
3. Run the script.

### Input Parameters

The `ShapefileToKingdomPolygon` function accepts the following parameters:

- `shapefolder` - File path of the folder where the shapefiles are located. All shapefiles are assumed to be in the same EPSG coordinate system.
- `EPSGin` - EPSG code of the coordinate system of the shapefiles in the folder.
- `EPSGout` - EPSG code of the Kingdom Project coordinate system.
- `csvname` - Name of the CSV file generated. The file will be saved in the `shapefolder`.
- `nameinrecord` - The location of the name field in the record (first field is 0).

### Output

The script will generate a CSV file with the following columns:

- `Name` - Name of the shapefile record.
- `Number` - Number of the coordinate point within the shape.
- `X` - X-coordinate of the point in the Kingdom Project coordinate system.
- `Y` - Y-coordinate of the point in the Kingdom Project coordinate system.

### References

- [PyShp (shapefile)](https://pypi.org/project/pyshp/)
- [PyProj (Proj)](https://pypi.org/project/pyproj/)
- [EPSG Codes](http://prj2epsg.org/search)
- [SpatialReference.org](https://spatialreference.org/ref/epsg/)
