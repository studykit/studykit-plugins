# RevolveFeatures.AddFull Method

Parent Object: [RevolveFeatures](../RevolveFeatures/RevolveFeatures.md)

## Description

Method that creates a new RevolveFeature that is a full 360-degree sweep. The new RevolveFeature is returned.

## Syntax

RevolveFeatures.**AddFull**( ***Profile*** As [Profile](../Profile/Profile.md), ***AxisEntity*** As Object, ***Operation*** As [PartFeatureOperationEnum](../PartFeatureOperationEnum.md) ) As [RevolveFeature](../RevolveFeature/RevolveFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Profile | [Profile](../Profile/Profile.md) | Input Profile object used to define the shape of the revolution. If the AsSolid argument is True, then the input profile must have closed paths. Open paths are valid when creating surfaces. |
| AxisEntity | Object | Input linear entity that defines the axis of the revolution. This must be a sketch line in the same sketch that was used to generate the profile. |
| Operation | [PartFeatureOperationEnum](../PartFeatureOperationEnum.md) | Input constant that indicates the type of operation to perform. Valid input is kJoinOperation, kCutOperation, kIntersectOperation, or kSurfaceOperation. |

## Version

Introduced in version 5
