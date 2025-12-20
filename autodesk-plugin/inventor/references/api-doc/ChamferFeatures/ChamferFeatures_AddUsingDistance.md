# ChamferFeatures.AddUsingDistance Method

Parent Object: [ChamferFeatures](../ChamferFeatures/ChamferFeatures.md)

## Description

Method that creates a new ChamferFeature defined by a specified distance. The new ChamferFeature is returned.

## Syntax

ChamferFeatures.**AddUsingDistance**( ***Edges*** As [EdgeCollection](../EdgeCollection/EdgeCollection.md), ***Distance*** As Variant, [***AutomaticEdgeChain***] As Boolean, [***CornerSetback***] As Boolean, [***PreserveAllFeatures***] As Boolean ) As [ChamferFeature](../ChamferFeature/ChamferFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Edges | [EdgeCollection](../EdgeCollection/EdgeCollection.md) | Input object that contains the edges to be chamfered. |
| Distance | Variant | Input Variant that defines the distance for the chamfer. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current distance units of the document. |
| AutomaticEdgeChain | Boolean | Optional input Boolean that defines if automatic edge chaining along tangentially connected edges should be performed. The default is True. |
| CornerSetback | Boolean | Optional Boolean that defines how any corners will be treated. If True, the corner is joined by a flat intersection. If False, the corner is defined by the intersection of the chamfers. The default is True.   This is an optional argument whose default value is True. |
| PreserveAllFeatures | Boolean | Optional Boolean that defines the behavior when the chamfer intersects the body other than at adjacent faces. The default is False.   This is an optional argument whose default value is False. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Partial Chamfer Sample](../../sample-programs/PartialChamferSample_Sample.md) | This sample demonstrates how to edit a chamfer feature to set the partial chamfer on a chamfered edge. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |