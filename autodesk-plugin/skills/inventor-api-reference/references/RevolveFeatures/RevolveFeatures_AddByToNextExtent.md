# RevolveFeatures.AddByToNextExtent Method

Parent Object: [RevolveFeatures](../RevolveFeatures/RevolveFeatures.md)

## Description

Method that creates a new RevolveFeature using 'to next' extents. The new RevolveFeature is returned.

## Syntax

RevolveFeatures.**AddByToNextExtent**( ***Profile*** As [Profile](../Profile/Profile.md), ***AxisEntity*** As Object, ***ExtentDirection*** As [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md), ***Terminator*** As [SurfaceBody](../SurfaceBody/SurfaceBody.md), ***Operation*** As [PartFeatureOperationEnum](../PartFeatureOperationEnum.md) ) As [RevolveFeature](../RevolveFeature/RevolveFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Profile | [Profile](../Profile/Profile.md) | Input Profile object used to define the shape of the revolution. If the Operation argument is anything except kSurfaceOperation, then the input profile must have closed paths. Open paths are valid when creating surfaces. |
| AxisEntity | Object | Input linear entity that defines the axis of the revolution. This can either be a sketch line in the same sketch that was used to generate the profile or a WorkAxis object. |
| ExtentDirection | [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) | Input constant that indicates which side of the sketch plane to extrude towards. Valid input is kPositiveExtentDirection or kNegativeExtentDirection. kPositiveExtentDirection defines the offset direction to be in the same direction as the normal of the sketch plane. |
| Terminator | [SurfaceBody](../SurfaceBody/SurfaceBody.md) | Input SurfaceBody object that specifies the solid or the surface on which to terminate the revolution. |
| Operation | [PartFeatureOperationEnum](../PartFeatureOperationEnum.md) | Input constant that indicates the type of operation to perform. Valid input is kJoinOperation, kCutOperation, kIntersectOperation, kSurfaceOperation. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |