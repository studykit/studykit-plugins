# ContourFlangeDefinition.SetDistanceExtent Method

Parent Object: [ContourFlangeDefinition](../ContourFlangeDefinition/ContourFlangeDefinition.md)

## Description

Method that changes the ContourFlangeDefinition object to define a contour flange whose width is defined by a distance from the input Profile.

## Syntax

ContourFlangeDefinition.**SetDistanceExtent**( ***Distance*** As Variant, ***ExtentDirection*** As [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Distance | Variant | Defines the length of the extrusion. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| ExtentDirection | [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) | Constant that indicates which side of the sketch plane to exend the flange to. Valid input is kPositiveExtentDirection, kNegativeExtentDirection, or kSymmetricExtentDirection. kPositiveExtentDirection defines the offset direction to be in the same direction as the normal of the sketch plane. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |