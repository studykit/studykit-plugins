# CornerChamferDefinition.SetDistanceAndAngle Method

Parent Object: [CornerChamferDefinition](../CornerChamferDefinition/CornerChamferDefinition.md)

## Description

Method that changes the CornerChamferDefinition object to define a chamfer that is measured by an offset from the corner along one face and then ang chamfer feature where the chamfer is defined by a distance from an edge and an angle from a face.

## Syntax

CornerChamferDefinition.**SetDistanceAndAngle**( ***CornerEdges*** As [EdgeCollection](../EdgeCollection/EdgeCollection.md), ***Face*** As [Face](../Face/Face.md), ***Distance*** As Variant, ***Angle*** As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CornerEdges | [EdgeCollection](../EdgeCollection/EdgeCollection.md) | Input EdgeCollection object that contains all of the corners to apply a fillet on. These must be corner edges and must also be edges of the face specified through the Face argument. |
| Face | [Face](../Face/Face.md) | Input Face object that the chamfer angle is measured from. |
| Distance | Variant | Input Variant that defines the distance for the chamfer. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| Angle | Variant | Input Variant that defines the angle for the chamfer. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are radians. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |