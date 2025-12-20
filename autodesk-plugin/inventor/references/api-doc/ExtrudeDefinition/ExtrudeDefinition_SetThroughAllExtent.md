# ExtrudeDefinition.SetThroughAllExtent Method

Parent Object: [ExtrudeDefinition](../ExtrudeDefinition/ExtrudeDefinition.md)

## Description

Method that changes the extents to be “through all” extents.

## Syntax

ExtrudeDefinition.**SetThroughAllExtent**( ***ExtentDirection*** As [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ExtentDirection | [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) | Input constant that indicates which side of the sketch plane to extrude towards. Valid input is kPositiveExtentDirection, kNegativeExtentDirection, or kSymmetricExtentDirection. kPositiveExtentDirection defines the offset direction to be in the same direction as the normal of the sketch plane. |

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |