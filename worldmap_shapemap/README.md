## Download the TopoJSON file
Save the JSON file from Raw or follow the below steps to get the map on your own.

## Downloading the World Map from Natural Earth Data Site

1. Visit the [Natural Earth Data website](https://www.naturalearthdata.com/downloads/)
2. Choose Cultural under any scale of your choice
3. Click on the "Download" button next to "Admin 0 - Countries".

## Converting to PowerBI compatible TopoJSON file

1. Unzip the shapefile that you have downloaded.
2. You may find several files in different formats.
3. Now head over to [mapshaper](https://mapshaper.org/)
4. Upload the files with **.dbf**, **.prj**, **.shp** and **.shx** formats.
5. Simplify the map by clicking on Simplify in the top-right menu.
6. Make sure to select prevent shape removal as shown in the image below, otherwise map areas may disappear through the simplification process!
7. Simplify the map by moving the slider to the right. Also, repair intersections if detected.
8. Click on Export to save the map. Select **TopoJSON**, and then click on Export.
