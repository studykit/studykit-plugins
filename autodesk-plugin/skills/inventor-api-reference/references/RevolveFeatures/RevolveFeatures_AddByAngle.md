# RevolveFeatures.AddByAngle Method

Parent Object: [RevolveFeatures](../RevolveFeatures/RevolveFeatures.md)

## Description

Method that creates a new RevolveFeature that sweeps a specified angle. The new RevolveFeature is returned.

## Syntax

RevolveFeatures.**AddByAngle**( ***Profile*** As [Profile](../Profile/Profile.md), ***AxisEntity*** As Object, ***Angle*** As Variant, ***ExtentDirection*** As [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md), ***Operation*** As [PartFeatureOperationEnum](../PartFeatureOperationEnum.md) ) As [RevolveFeature](../RevolveFeature/RevolveFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Profile | [Profile](../Profile/Profile.md) | Input Profile object used to define the shape of the revolution. If the AsSolid argument is True, then the input profile must have closed paths. Open paths are valid when creating surfaces. |
| AxisEntity | Object | Input linear entity that defines the axis of the revolution. This can either be a sketch line in the same sketch that was used to generate the profile or a WorkAxis object. |
| Angle | Variant | Input Variant that defines the sweep angle of the revolution. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are radians. If a string is input, the units can be specified as part of the string or it will default to the current angle units of the document. |
| ExtentDirection | [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) | Input constant that indicates which side of the sketch plane to extrude toward. Valid input is kPositive, kNegative, or kSymmetric. kPositive defines the offset direction to be in the same direction as the normal of the sketch plane. |
| Operation | [PartFeatureOperationEnum](../PartFeatureOperationEnum.md) | Input constant that indicates the type of operation to perform. Valid input is kJoinOperation, kCutOperation, kIntersectOperation, or kSurfaceOperation |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |