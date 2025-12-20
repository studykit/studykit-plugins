# ThreadFeatures.Add Method

Parent Object: [ThreadFeatures](../ThreadFeatures/ThreadFeatures.md)

## Description

Method that creates a new ThreadFeature. The new ThreadFeature object is returned.

## Syntax

ThreadFeatures.**Add**( ***Face*** As [Face](../Face/Face.md), ***StartEdge*** As [Edge](../Edge/Edge.md), ***ThreadInfo*** As [ThreadInfo](../ThreadInfo/ThreadInfo.md), [***DirectionReversed***] As Boolean, [***FullDepth***] As Boolean, [***ThreadDepth***] As Variant, [***ThreadOffset***] As Variant ) As [ThreadFeature](../ThreadFeature/ThreadFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Face | [Face](../Face/Face.md) | Input Face object that defines which face the thread feature is to be applied to. The face must be either a cylinder or cone. |
| StartEdge | [Edge](../Edge/Edge.md) | Input Edge object that defines the start of the thread. The edge must be an edge of the input face. |
| ThreadInfo | [ThreadInfo](../ThreadInfo/ThreadInfo.md) | Input ThreadInfo object that defines the thread attributes. This must be a StandardThreadInfo in the case where the input face is a cylinder and a TaperedThreadInfo in the case where the input face is a cone. |
| DirectionReversed | Boolean | Optional input Boolean that specifies which direction from the start along the cone or cylinder the thread goes in. |
| FullDepth | Boolean | Optional input Boolean that specifies if the thread go the full length of the cylinder or cone. A value of True indicates it goes the full the length. If False, the ThreadDepth argument needs to be supplies.   This is an optional argument whose default value is True. |
| ThreadDepth | Variant | Input Variant that defines the depth of the thread. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document.   This is an optional argument whose default value is null. |
| ThreadOffset | Variant | Optional input Variant that defines the offset of the start of the thread from the start edge. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Thread Feature Create](../../sample-programs/ThreadFeature_Sample.md) | This sample demonstrates the creation of a thread feature. It creates a cylinder in a new part document and creates a thread feature on the cylinder. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |