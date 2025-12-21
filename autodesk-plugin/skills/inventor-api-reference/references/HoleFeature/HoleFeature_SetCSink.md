# HoleFeature.SetCSink Method

Parent Object: [HoleFeature](../HoleFeature/HoleFeature.md)

## Description

Method that changes the hole to be a countersink hole type. If the hole is already a countersink type you can access and modify the counterbore parameters using the CSinkDiameter and CSinkAngle properties of the HoleFeature object.

## Syntax

HoleFeature.**SetCSink**( ***CSinkDiameter*** As Variant, ***CSinkAngle*** As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CSinkDiameter | Variant | Input Variant that defines the diameter of the countersink. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input the units can be specified as part of the string or it will default to the current length units of the document. |
| CSinkAngle | Variant | Input Variant that defines the angle of the countersink. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are radians. If a string is input, the units can be specified as part of the string or it will default to the current angle units of the document. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |