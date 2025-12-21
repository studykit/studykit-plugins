# ExtrudeDefinition.SetToNextExtent Method

Parent Object: [ExtrudeDefinition](../ExtrudeDefinition/ExtrudeDefinition.md)

## Description

Method that changes the extents to be “to next face” extents.

## Syntax

ExtrudeDefinition.**SetToNextExtent**( ***ExtentDirection*** As [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md), ***Terminator*** As [SurfaceBody](../SurfaceBody/SurfaceBody.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ExtentDirection | [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) | Input constant that indicates which side of the sketch plane to extrude towards. Valid input is kPositiveExtentDirection or kNegativeExtentDirection. kPositiveExtentDirection defines the offset direction to be in the same direction as the normal of the sketch plane. |
| Terminator | [SurfaceBody](../SurfaceBody/SurfaceBody.md) | Input SurfaceBody object that specifies the solid or the surface on which to terminate the extrude. |

## Version

Introduced in version 2012
