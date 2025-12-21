# OccurrencePatterns.AddRectangularPattern Method

Parent Object: [OccurrencePatterns](../OccurrencePatterns/OccurrencePatterns.md)

## Description

Method that creates a new rectangular occurrence pattern of input component(s).

## Syntax

OccurrencePatterns.**AddRectangularPattern**( ***ParentComponents*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***ColumnEntity*** As Object, ***ColumnEntityNaturalDirection*** As Boolean, ***ColumnOffset*** As Variant, ***ColumnCount*** As Variant, [***RowEntity***] As Variant, [***RowEntityNaturalDirection***] As Boolean, [***RowOffset***] As Variant, [***RowCount***] As Variant ) As [RectangularOccurrencePattern](../RectangularOccurrencePattern/RectangularOccurrencePattern.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ParentComponents | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection that contains the components to pattern. The valid objects that can be specified in the collection are ComponentOccurrence and OccurrencePattern objects. |
| ColumnEntity | Object | Input proxy object that defines the column (x) direction of the pattern. This must be a proxy to a linear edge or a work axis. |
| ColumnEntityNaturalDirection | Boolean | Input Boolean that specifies if the column direction is in the natural direction of the column entity or opposed. True if it is in the same direction as the natural direction of the column entity. |
| ColumnOffset | Variant | Input Variant that defines the distance between the columns. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| ColumnCount | Variant | Input Variant that defines the number of columns. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a string is input it must result in a unitless number. |
| RowEntity | Variant | Optional input Variant that defines the row (y) direction of the pattern. This must be a proxy to a linear edge or a work axis. If this argument is left out then the pattern will have a single row and all subsequent arguments will be ignored. |
| RowEntityNaturalDirection | Boolean | Optional input Boolean that specifies if the row direction is in the natural direction of the row entity or opposed. True if it is in the same direction as the natural direction of the row entity. This argument must be supplied if the RowEntity argument is provided; otherwise it is ignored.     This is an optional argument whose default value is True. |
| RowOffset | Variant | Optional input Variant that defines the distance between the rows. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. This argument must be supplied if the RowEntity argument is provided; otherwise it is ignored.   This is an optional argument whose default value is null. |
| RowCount | Variant | Optional input Variant that defines the number of rows. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a string is input it must result in a unitless number. This argument must be supplied if the RowEntity argument is provided; otherwise it is ignored.Sub PatternComponent()    ' Set a reference to the active assembly document  Dim oDoc As AssemblyDocument  Set oDoc = ThisApplication.ActiveDocument    ' Set a reference to the AssemblyComponentDefinition  Dim oDef As AssemblyComponentDefinition  Set oDef = oDoc.ComponentDefinition    ' Get the x\-axis of the assembly  Dim oXAxis As WorkAxis  Set oXAxis = oDef.WorkAxes.Item(1)    ' Get the y\-axis of the assembly  Dim oYAxis As WorkAxis  Set oYAxis = oDef.WorkAxes.Item(2)    Dim oParentOccs As ObjectCollection  Set oParentOccs = ThisApplication.TransientObjects.CreateObjectCollection    oParentOccs.Add oDef.Occurrences.Item(1)    ' Create a rectangular pattern of components\:  ' 4 columns in the x\-direction with an offset of 5 in  ' 3 rows in the y\-direction with an offset of 4 in  Dim oRectOccPattern As RectangularOccurrencePattern  Set oRectOccPattern = oDef.OccurrencePatterns.AddRectangularPattern( \_  oParentOccs, oXAxis, True, "5 in", 4, oYAxis, True, "4 in", 3)  End Sub    This is an optional argument whose default value is null. |

## Version

Introduced in version 6
