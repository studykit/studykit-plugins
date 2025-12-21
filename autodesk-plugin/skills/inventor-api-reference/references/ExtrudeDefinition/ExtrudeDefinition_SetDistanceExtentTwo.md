# ExtrudeDefinition.SetDistanceExtentTwo Method

Parent Object: [ExtrudeDefinition](../ExtrudeDefinition/ExtrudeDefinition.md)

## Description

Method that sets the second direction extent to be “distance” extents. This method returns an error if the first extent type is not distance extent.

## Syntax

ExtrudeDefinition.**SetDistanceExtentTwo**( ***Distance*** As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Distance | Variant | Input Variant that defines the length of the extrusion in the other direction for an asymmetric extrude. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |