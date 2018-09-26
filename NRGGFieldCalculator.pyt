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
        datatype = 'GPTableView',
        parameterType ="Required",
        direction ="Input")

        param1 = arcpy.Parameter(displayName = 'Unique ID Field',
        name = 'Join Field',
        datatype = 'Field',
        parameterType ="Required",
        direction ="Input")
        param1.parameterDependencies = [param0.name]
        
        param2 = arcpy.Parameter(displayName = 'Select the Field to be Updated',
        name = 'Update Field',
        datatype = 'Field',
        parameterType ="Required",
        direction ="Input")
        param2.parameterDependencies = [param0.name]

        param3 = arcpy.Parameter(displayName = 'Select the Field With the Update Value',
        name = 'Value Field',
        datatype = 'Field',
        parameterType ="Required",
        direction ="Input")
        param3.parameterDependencies = [param0.name]

        param4 = arcpy.Parameter(displayName = 'Optional SQL Query to Perform Before Field Calculation',
        name = 'SQL Query',
        datatype = 'GPSQLExpression',
        parameterType ="Optional",
        direction ="Input")
        param4.parameterDependencies = [param0.name]

        params = [param0, param1, param2, param3, param4]
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
        fcquery = parameters[4].valueAsText
        
        cursor = arcpy.da.SearchCursor(fc, [Uniqueid, Valuefield], fcquery)

        valueDi = {}
        for row in cursor:
            key = row[0]
            vals = row[1]
            if key not in valueDi:
                valueDi[key] = []
                valueDi[key] = vals
            else:
                valueDi[key] = vals

        cursor = arcpy.da.UpdateCursor(fc, [Uniqueid, Updatefield])
        for row in cursor: 
            if not row[0] in valueDi:
                continue
            row[1] = (valueDi[row[0]])
            cursor.updateRow(row)

class JoinCalculateFields(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "CalculateField Between Two Tables"
        self.description = ""
        self.canRunInBackground = True

    def getParameterInfo(self):
        """Define parameter definitions"""
        param10 = arcpy.Parameter(displayName = 'Target Feature Class or Table',
        name = 'Feature Class',
        datatype = 'GPTableView',
        parameterType ="Required",
        direction ="Input")

        param11 = arcpy.Parameter(displayName = 'Target Feature Class or Table Unique ID Field',
        name = 'Unique ID Needed to Assure Correct Values Are Computed',
        datatype = 'Field',
        parameterType ="Required",
        direction ="Input")
        param11.parameterDependencies = [param10.name]
        
        param12 = arcpy.Parameter(displayName = 'Select the Target Field',
        name = 'Update Field',
        datatype = 'Field',
        parameterType ="Required",
        direction ="Input")
        param12.parameterDependencies = [param10.name]

        param13 = arcpy.Parameter(displayName = 'Optional SQL Query to Perform on Target Data Before Field Calculation',
        name = 'Update SQL Query',
        datatype = 'GPSQLExpression',
        parameterType ="Optional",
        direction ="Input")
        param13.parameterDependencies = [param10.name]

        param14 = arcpy.Parameter(displayName = 'Value Table or Feature Class',
        name = 'Value Table or Feature Class',
        datatype = 'GPTableView',
        parameterType = "Required",
        direction = "Input")

        param15 = arcpy.Parameter(displayName = 'Value Unique ID Field',
        name = 'Join Field',
        datatype = 'Field',
        parameterType ="Required",
        direction ="Input")
        param15.parameterDependencies = [param14.name]

        param16 = arcpy.Parameter(displayName = 'Select the Field With the Update Value',
        name = 'Value Field',
        datatype = 'Field',
        parameterType ="Required",
        direction ="Input")
        param16.parameterDependencies = [param14.name]

        param17 = arcpy.Parameter(displayName = 'Optional SQL Query to Perform on Value Data Before Field Calculation',
        name = 'Value SQL Query',
        datatype = 'GPSQLExpression',
        parameterType ="Optional",
        direction ="Input")
        param17.parameterDependencies = [param14.name]

        params = [param10, param11, param12, param13, param14, param15, param16, param17]
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
        fcquery = parameters[3].valueAsText
        joinfc = parameters[4].valueAsText
        JoinUniqueid = parameters[5].valueAsText
        Valuefield = parameters[6].valueAsText
        joinfcquery = parameters[7].valueAsText

        cursor = arcpy.da.SearchCursor(joinfc, [JoinUniqueid, Valuefield], joinfcquery)

        valueDi = {}
        for row in cursor:
            key = row[0]
            vals = row[1]
            if key not in valueDi:
                valueDi[key] = []
                valueDi[key] = vals
            else:
                valueDi[key] = vals

        cursor = arcpy.da.UpdateCursor(fc, [Uniqueid, Updatefield], fcquery)
        for row in cursor: 
            if not row[0] in valueDi:
                continue
            row[1] = (valueDi[row[0]])
            cursor.updateRow(row)