# RipDefinition.SetPointToPointRipType Method

Parent Object: [RipDefinition](../RipDefinition/RipDefinition.md)

## Description

Method that sets the RipDefinition so that it defines a point to point rip.

## Syntax

RipDefinition.**SetPointToPointRipType**( ***RipFace*** As [Face](../Face/Face.md), ***PointOne*** As Object, ***PointTwo*** As Object, ***GapSize*** As Variant, ***GapSide*** As [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| RipFace | [Face](../Face/Face.md) | The face that the rip is defined along. This must be a face this is valid for defining a rip extent. For example a face along the edge of the part where the thickness of the part is represented is not valid as input. |
| PointOne | Object | Point that defines the location of the first rip point. Valid input includes Vertex, WorkPoint, SketchPoint, and SketchPoint3D objects. |
| PointTwo | Object | Point that defines the location of the second rip point. Valid input includes Vertex, WorkPoint, SketchPoint, and SketchPoint3D objects. |
| GapSize | Variant | Variant that defines the width of the gap. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| GapSide | [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) | Input PartFeatureExtentDirectionEnum value to indicate the position of the gap. Valid values are kPositiveExtentDirection, kNegativeExtentDirection, and kSymmetricExtentDirection. kPositiveExtentDirection indicates that the material will be removed from the right from the perspective of the first rip point where 'up' is along the normal of the rip face and you're looking towards the second rip point. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |