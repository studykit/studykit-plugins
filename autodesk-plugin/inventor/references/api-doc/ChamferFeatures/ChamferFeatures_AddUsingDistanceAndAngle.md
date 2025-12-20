# ChamferFeatures.AddUsingDistanceAndAngle Method

Parent Object: [ChamferFeatures](../ChamferFeatures/ChamferFeatures.md)

## Description

Method that creates a new ChamferFeature that is defined by a distance and at a specified angle to an input face. The new ChamferFeature is returned.

## Syntax

ChamferFeatures.**AddUsingDistanceAndAngle**( ***Edges*** As [EdgeCollection](../EdgeCollection/EdgeCollection.md), ***Face*** As [Face](../Face/Face.md), ***Distance*** As Variant, ***Angle*** As Variant, [***AutomaticEdgeChain***] As Boolean, [***PreserveAllFeatures***] As Boolean ) As [ChamferFeature](../ChamferFeature/ChamferFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Edges | [EdgeCollection](../EdgeCollection/EdgeCollection.md) | Input object that contains the edges to be chamfered. |
| Face | [Face](../Face/Face.md) | Input object that is chamfer angle is measured from. |
| Distance | Variant | Input Variant that defines the distance for the chamfer. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current distance units of the document. |
| Angle | Variant | Input Variant that defines the angle for the chamfer. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are radians. If a string is input, the units can be specified as part of the string or it will default to the current angle units of the document. |
| AutomaticEdgeChain | Boolean | Optional input Boolean that defines if automatic edge chaining along tangentially connected edges should be performed. The default is True. |
| PreserveAllFeatures | Boolean | Optional Boolean that defines the behavior when the chamfer intersects the body other than at adjacent faces. The default is False.   This is an optional argument whose default value is False. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |