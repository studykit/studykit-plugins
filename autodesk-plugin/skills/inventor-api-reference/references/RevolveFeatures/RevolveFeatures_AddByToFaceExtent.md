# RevolveFeatures.AddByToFaceExtent Method

Parent Object: [RevolveFeatures](../RevolveFeatures/RevolveFeatures.md)

## Description

Method that creates a new RevolveFeature using 'to face' extents. The new RevolveFeature is returned.

## Syntax

RevolveFeatures.**AddByToFaceExtent**( ***Profile*** As [Profile](../Profile/Profile.md), ***AxisEntity*** As Object, ***ToFace*** As Object, ***ExtendToFace*** As Boolean, ***ExtentDirection*** As [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md), ***MinimumSolution*** As Boolean, ***Operation*** As [PartFeatureOperationEnum](../PartFeatureOperationEnum.md) ) As [RevolveFeature](../RevolveFeature/RevolveFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Profile | [Profile](../Profile/Profile.md) | Input Profile object used to define the shape of the revolution. If the Operation argument is anything except kSurfaceOperation, then the input profile must have closed paths. Open paths are valid when creating surfaces. |
| AxisEntity | Object | Input linear entity that defines the axis of the revolution. This can either be a sketch line in the same sketch that was used to generate the profile or a WorkAxis object. |
| ToFace | Object | Input Object that defines the 'to face'. This can be either a Face or WorkPlane object. |
| ExtendToFace | Boolean | Input Boolean that defines whether the 'to face' should be extended to contain the extents of the profile. |
| ExtentDirection | [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) | Input constant that indicates which side of the sketch plane to extrude towards. Valid input is kPositiveExtentDirection, kNegativeExtentDirection or kSymmetricExtentDirection. kPositiveExtentDirection defines the offset direction to be in the same direction as the normal of the sketch plane. |
| MinimumSolution | Boolean | Input Boolean that defines whether the feature terminates on the nearest valid face when there are multiple options for valid termination faces. |
| Operation | [PartFeatureOperationEnum](../PartFeatureOperationEnum.md) | Input constant that indicates the type of operation to perform. Valid input is kJoinOperation, kCutOperation, kIntersectOperation, kSurfaceOperation. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |