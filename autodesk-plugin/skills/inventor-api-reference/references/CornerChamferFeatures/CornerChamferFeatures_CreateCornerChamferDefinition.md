# CornerChamferFeatures.CreateCornerChamferDefinition Method

Parent Object: [CornerChamferFeatures](../CornerChamferFeatures/CornerChamferFeatures.md)

## Description

Method that creates a new CornerChamferDefinition object.

## Remarks

This object is not a corner chamfer feature but contains the information that defines a corner chamfer feature and can be used to create a new corner chamfer feature or edit an existing one. The returned CornerChamferDefinition can be used as input to the CornerChamferFeatures.Add method to create a new corner chamfer feature. You can edit the properties of the CornerChamferDefinition object before creating the corner chamfer feature to get the desired corner chamfer feature. The CornerChamferDefinition object returned by this method will create a chamfer feature where the offset distance is the same on both faces. You can change the chamfer type by editing the CornerChamferDefinition object before using it to create a corner chamfer feature.

## Syntax

CornerChamferFeatures.**CreateCornerChamferDefinition**( ***CornerEdges*** As Object, ***Distance*** As Variant ) As [CornerChamferDefinition](../CornerChamferDefinition/CornerChamferDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CornerEdges | Object | Input object that defines the corner(s) to apply a corner chamfer on. This can be a single Edge object or an EdgeCollection that contains the Edge objects to chamfer. Any non-corner edges will be ignored. |
| Distance | Variant | Input Variant that defines the distance from the edge. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |