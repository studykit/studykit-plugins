# RevolveFeatureProxy.SetToFaceExtent Method

Parent Object: [RevolveFeatureProxy](../RevolveFeatureProxy/RevolveFeatureProxy.md)

## Description

Method that changes the extents to be 'to face' extents.

## Syntax

RevolveFeatureProxy.**SetToFaceExtent**( ***ToFace*** As Object, ***ExtendToFace*** As Boolean, ***ExtentDirection*** As [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md), ***MinimumSolution*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ToFace | Object | Input Object that defines the 'to face'. This can be either a Face or WorkPlane object. |
| ExtendToFace | Boolean | Input Boolean that defines whether the 'to face' should be extended to contain the extents of the profile. |
| ExtentDirection | [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) | Input constant that indicates which side of the sketch plane to extrude towards. Valid input is kPositiveExtentDirection, kNegativeExtentDirection or kSymmetricExtentDirection. kPositiveExtentDirection defines the offset direction to be in the same direction as the normal of the sketch plane. |
| MinimumSolution | Boolean | Input Boolean that defines whether the feature terminates on the nearest valid face when there are multiple options for valid termination faces. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |