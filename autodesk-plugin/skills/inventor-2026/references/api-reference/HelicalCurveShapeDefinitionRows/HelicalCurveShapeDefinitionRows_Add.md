# HelicalCurveShapeDefinitionRows.Add Method

Parent Object: [HelicalCurveShapeDefinitionRows](../HelicalCurveShapeDefinitionRows/HelicalCurveShapeDefinitionRows.md)

## Description

Adds a new HelicalCurveShapeDefinitionRow.

## Syntax

HelicalCurveShapeDefinitionRows.**Add**( ***Diameter*** As Variant, [***Pitch***] As Variant, [***Revolution***] As Variant, [***Height***] As Variant, [***Index***] As Variant ) As [HelicalCurveShapeDefinitionRow](../HelicalCurveShapeDefinitionRow/HelicalCurveShapeDefinitionRow.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Diameter | Variant | Input value that defines the diameter of the helical curve. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| Pitch | Variant | Optional input value that defines the pitch of the helical curve. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. This is required if the ShapeDefinitionType is specified as kPitchAndRevolutionShapeType or kPitchAndHeightShapeType. |
| Revolution | Variant | Optional input Double value that defines the revolution of the helical curve. This is required if the ShapeDefinitionType is specified as kPitchAndRevolutionShapeType or kRevolutionAndHeightShapeType.   This is an optional argument whose default value is null. |
| Height | Variant | Optional input value that defines the overall height of the helical curve till this row. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. This is required if the ShapeDefinitionType is specified as kPitchAndHeightShapeType or kRevolutionAndHeightShapeType.   This is an optional argument whose default value is null. |
| Index | Variant | Optional input value that specifies the index of the row to insert. If not provided this defaults to 0 means it will be placed at last.   This is an optional argument whose default value is 0. |

## Version

Introduced in version 2019
