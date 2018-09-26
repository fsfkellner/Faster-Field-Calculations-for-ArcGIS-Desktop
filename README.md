# Faster-Field-Calculations-for-ArcGIS-Desktop
Field calculations in ArcGIS Desktop can be painfully slow when there are many records (e.g.,>30,000) especially when the calculation is occurring with a joined table.

Faster calculations can be achieved using Python Libraries to store values and Arcpy Search Cursors to update values.

The Python Toolbox supplied here has a tool for field calculations within an existing table and second tool for field calculation that would be performed between two tables. 

When performing field calculations between two tables make sure the tables are not joined for the fastest performance. 
