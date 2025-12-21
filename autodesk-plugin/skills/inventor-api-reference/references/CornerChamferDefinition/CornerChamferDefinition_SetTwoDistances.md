# CornerChamferDefinition.SetTwoDistances Method

Parent Object: [CornerChamferDefinition](../CornerChamferDefinition/CornerChamferDefinition.md)

## Description

Method that changes the CornerChamferDefinition object to define a chamfer that is measured by two offset distances.

## Syntax

CornerChamferDefinition.**SetTwoDistances**( ***CornerEdge*** As [Edge](../Edge/Edge.md), ***Face*** As [Face](../Face/Face.md), ***DistanceOne*** As Variant, ***DistanceTwo*** As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CornerEdge | [Edge](../Edge/Edge.md) | Input Edge object that defines the corner to place the chamfer on.. |
| Face | [Face](../Face/Face.md) | Input Face object that specifies which face the first distance applies to. The corner edges specified must lie on this face. |
| DistanceOne | Variant | Input Variant that defines the first distance for the chamfer.. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| DistanceTwo | Variant | Input Variant that defines the second distance for the chamfer.. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |