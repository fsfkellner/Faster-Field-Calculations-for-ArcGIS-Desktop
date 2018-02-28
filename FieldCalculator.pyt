import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [CalculateFields,JoinCalculateFields]


class CalculateFields(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "CalculateField on Same Table"
        self.description = "This toolbox was designed to perform ArcGIS field calculations, but harness the speed and power of Python dictionaries and Arcpy Search Cursors. This tool is only for field calculations within the same table. For field calcuations between two feature classes or tables please use the other tool in this toolbox."
        self.canRunInBackground = True

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(displayName = 'Feature Class or Table',
        name = 'Feature Class',
        datatype = 'GPType',
        parameterType ="Required",
        direction ="Input")

        param1 = arcpy.Parameter(displayName = 'Unique ID Field',
        name = 'Join Field',
        datatype = 'Field',
        parameterType ="Required",
        direction ="Input")
        param1.parameterDependencies = [param0.name]
        
        param2 = arcpy.Parameter(displayName = 'Select the update field',
        name = 'Update Field',
        datatype = 'Field',
        parameterType ="Required",
        direction ="Input")
        param2.parameterDependencies = [param0.name]

        param3 = arcpy.Parameter(displayName = 'Pick the field with the update value',
        name = 'Value Field',
        datatype = 'Field',
        parameterType ="Required",
        direction ="Input")
        param3.parameterDependencies = [param0.name]

        params = [param0, param1, param2, param3]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return
        

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        fc = parameters[0].valueAsText
        Uniqueid = parameters[1].valueAsText
        Updatefield = parameters[2].valueAsText
        Valuefield = parameters[3].valueAsText
        cursor = arcpy.da.SearchCursor(fc, [Uniqueid, Valuefield])

        valueDi = {}
        for row in cursor:
            key = row[0]
            vals = row[1]
            if key not in valueDi:
                valueDi[key] = []
                valueDi[key] = vals
            else:
                valueDi[key] = vals

        cursor = arcpy.da.UpdateCursor (fc, [Uniqueid, Updatefield ])
        for row in cursor: 
            if not row[0] in valueDi:
                continue
                #create row tuple

            row[1] = (valueDi[row[0]])
            cursor.updateRow(row)
class JoinCalculateFields(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "CalculateField Using a Join Table"
        self.description = ""
        self.canRunInBackground = True

    def getParameterInfo(self):
        """Define parameter definitions"""
        param10 = arcpy.Parameter(displayName = 'Update Feature Class or Table',
        name = 'Feature Class',
        datatype = 'GPType',
        parameterType ="Required",
        direction ="Input")

        param11 = arcpy.Parameter(displayName = 'Update Unique ID Field',
        name = 'Unique ID needed to assure correct values are computed',
        datatype = 'Field',
        parameterType ="Required",
        direction ="Input")
        param11.parameterDependencies = [param10.name]
        
        param12 = arcpy.Parameter(displayName = 'Select the update field',
        name = 'Update Field',
        datatype = 'Field',
        parameterType ="Required",
        direction ="Input")
        param12.parameterDependencies = [param10.name]

        param16 = arcpy.Parameter(displayName = 'Value Table or Feature Class',
        name = 'Value Table or Feature Class',
        datatype = 'GPType',
        parameterType = "Required",
        direction = "Input")

        param14 = arcpy.Parameter(displayName = 'Value Unique ID Field',
        name = 'Join Field',
        datatype = 'Field',
        parameterType ="Required",
        direction ="Input")
        param14.parameterDependencies = [param16.name]

        param15 = arcpy.Parameter(displayName = 'Pick the field with the update value',
        name = 'Value Field',
        datatype = 'Field',
        parameterType ="Required",
        direction ="Input")
        param15.parameterDependencies = [param16.name]

        params = [param10, param11, param12, param16, param14, param15]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return
        

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        fc = parameters[0].valueAsText
        Uniqueid = parameters[1].valueAsText
        Updatefield = parameters[2].valueAsText
        joinfc = parameters[3].valueAsText
        JoinUniqueid = parameters[4].valueAsText
        Valuefield = parameters[5].valueAsText
        cursor = arcpy.da.SearchCursor(joinfc, [JoinUniqueid, Valuefield])

        valueDi = {}
        for row in cursor:
            key = row[0]
            vals = row[1]
            if key not in valueDi:
                valueDi[key] = []
                valueDi[key] = vals
            else:
                valueDi[key] = vals

        cursor = arcpy.da.UpdateCursor (fc, [Uniqueid, Updatefield ])
        for row in cursor: 
            if not row[0] in valueDi:
                continue
            row[1] = (valueDi[row[0]])
            cursor.updateRow(row)