# RipDefinition.SetSinglePointRipType Method

Parent Object: [RipDefinition](../RipDefinition/RipDefinition.md)

## Description

Method that sets the RipDefinition so that it defines a single point rip.

## Syntax

RipDefinition.**SetSinglePointRipType**( ***RipFace*** As [Face](../Face/Face.md), ***Point*** As Object, ***GapSize*** As Variant, ***GapSide*** As [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| RipFace | [Face](../Face/Face.md) | The face that the rip is defined along. This must be a face this is valid for defining a rip extent. For example a face along the edge of the part where the thickness of the part is represented is not valid as input. |
| Point | Object | The point that defines the location of the rip. Valid input includes Vertex, WorkPoint, SketchPoint, and SketchPoint3D objects. |
| GapSize | Variant | Variant that defines the width of the gap. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| GapSide | [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) | Input PartFeatureExtentDirectionEnum value to indicate the position of the gap. Valid values are kPositiveExtentDirection, kNegativeExtentDirection, and kSymmetricExtentDirection. kPositiveExtentDirection indicates that the material will be removed from the right from the perspective of the rip point where 'up' is along the normal of the rip face and you're looking towards the other edge of the face where the rip will end. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |

## Version

Introduced in version 2011
