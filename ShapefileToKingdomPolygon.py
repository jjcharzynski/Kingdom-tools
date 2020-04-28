# -*- coding: utf-8 -*-

def ShapefileToKingdomPolygon(shapefolder, EPSGin, EPSGout, csvname, nameinrecord):
    '''
    ShapefileToKingdomPolygon(shapefolder, EPSGin, EPSGout, csvname)
    *Input parameters:
        shapefolder - file path of the folder in which the shapefiles are located. All shapefiles are assummed to be in the same EPSG coordinate system.
        ESPGin - ESPG code of the coordinate system of the shapefiles in the folder
        EPSGout - EPSG code of the Kingdom Project coordinate system
        csvname - name of the csv file generated. File will be saved in the shapefolder.
        nameinrecord - the location of the name field in the record (first field is 0)
    *Requirements
        Needs PyShp (shapefile), PyProj (Proj), os, csv installed
        The correct coordinate systems need to be set using the epsg code.
        http://prj2epsg.org/search
        https://spatialreference.org/ref/epsg/
    *Returns:
        Writes all shapefiles in a folder to a csv file that can be loaded via the Kingdom Tools>Polygon>Import to load as Kingdom planimeter polygons.
    '''

    import shapefile
    import os
    import csv
    from pyproj import Proj, transform
    import time

    start = time.time()   
    with open(str(shapefolder + '\\' + csvname + '.csv'),'w') as out:
        csv_out=csv.writer(out)
        csv_out.writerow(['Name', 'Number', 'X','Y'])
        for file in os.listdir(shapefolder):
            ext = os.path.splitext(file)[-1].lower()
            if ext == '.shp':
                path = str(shapefolder + '\\' + file)
                shape = shapefile.Reader(path)
#                print(shape)
                numberofshapes = len(shape)
                n = 0
                while n < numberofshapes:
                    record = shape.record(n)
                    name = record[nameinrecord]
#                    print(name)
                    feature = shape.shapeRecords()[n]
                    coordinates = feature.shape.__geo_interface__['coordinates']
#                    print(coordinates)
                    number = 0
                    for row in coordinates[0]:
                        number += 1
                        x1,y1 = row[0],row[1]
#                        print(x1,y1)
                        inProj = Proj(init=str('epsg:'+ str(EPSGin)))
                        outProj = Proj(init=str('epsg:'+ str(EPSGout)))
                        x2,y2 = transform(inProj,outProj,x1,y1)
#                        print("EPSG in:", EPSGin, "x:", x1, "y:", y1, "EPSG out:", EPSGout,  "x:", x2, "y:", y2)
                        s = [name, number, x2, y2]
                        print(s)
                        csv_out.writerow(s)
                    n += 1
            else:
                continue
    end = time.time()
    print('completed in', end - start, 'seconds.')