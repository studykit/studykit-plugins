# HelicalCurves.CreateVariableShapeDefinition Method

Parent Object: [HelicalCurves](../HelicalCurves/HelicalCurves.md)

## Description

Creates a helical curve shape definition which can be used to create a helical curve.

## Syntax

HelicalCurves.**CreateVariableShapeDefinition**( ***ShapeDefinitionType*** As [HelicalShapeDefinitionTypeEnum](../HelicalShapeDefinitionTypeEnum.md), ***AxisStartPoint*** As [Point](../Point/Point.md), ***AxisEndPoint*** As [Point](../Point/Point.md), ***CurveStartPoint*** As [Point](../Point/Point.md), ***Diameter*** As Variant, [***Pitch***] As Variant, [***Revolution***] As Variant, [***Height***] As Variant ) As [HelicalCurveVariableShapeDefinition](../HelicalCurveVariableShapeDefinition/HelicalCurveVariableShapeDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ShapeDefinitionType | [HelicalShapeDefinitionTypeEnum](../HelicalShapeDefinitionTypeEnum.md) | Input HelicalShapeDefinitionTypeEnum that defines the helical curve shape definition type. Valid value includes: kPitchAndRevolutionShapeType, kPitchAndHeightShapeType, and kRevolutionAndHeightShapeType. |
| AxisStartPoint | [Point](../Point/Point.md) | Input Point object that defines the axis start point of the helical curve. |
| AxisEndPoint | [Point](../Point/Point.md) | Input Point object that defines the axis end point of the helical curve. |
| CurveStartPoint | [Point](../Point/Point.md) | Input Point object that defines the start point of the helical curve. This maybe not the exact position of the start point of the helical curve, but defines the direction of the helical curve start point will be in, the direction is from the AxisStartPoint to CurveStartPoint. If the CurveStartPoint is not on the plane that is perpendicular to the axis and across the AxisStartPoint then it will be projected onto the plane. |
| Diameter | Variant | Input value that defines the diameter of the helical curve. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| Pitch | Variant | Optional input value that defines the pitch of the helical curve. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. This is required if the ShapeDefinitionType is specified as kPitchAndRevolutionShapeType, kPitchAndHeightShapeType or kSpiralShapeType. |
| Revolution | Variant | Optional input Double value that defines the revolution of the helical curve. This is required if the ShapeDefinitionType is specified as kPitchAndRevolutionShapeType, kRevolutionAndHeightShapeType or kSpiralShapeType.   This is an optional argument whose default value is null. |
| Height | Variant | Optional input value that defines the height of the helical curve. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. This is required if the ShapeDefinitionType is specified as kPitchAndHeightShapeType or kRevolutionAndHeightShapeType.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |