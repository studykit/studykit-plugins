# CoilFeatures.AddSpiral Method

Parent Object: [CoilFeatures](../CoilFeatures/CoilFeatures.md)

## Description

Method that creates a new CoilFeature that sweeps a specified angle. The new CoilFeature is returned.

## Syntax

CoilFeatures.**AddSpiral**( ***Profile*** As [Profile](../Profile/Profile.md), ***AxisEntity*** As Object, ***Pitch*** As Variant, ***Revolution*** As Variant, ***Operation*** As [PartFeatureOperationEnum](../PartFeatureOperationEnum.md), [***AxisDirectionReversed***] As Boolean, [***ClockwiseRotation***] As Boolean ) As [CoilFeature](../CoilFeature/CoilFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Profile | [Profile](../Profile/Profile.md) | Input object used to define the shape of the coil. |
| AxisEntity | Object | Input linear entity that defines the axis of the revolution. Valid input is either a sketch line or work axis. The axis entity must not intersect the input profile. |
| Pitch | Variant | Input Variant that defines the pitch of the coil feature. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| Revolution | Variant | Input Variant that defines the number of revolutions of the coil feature. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, it is unitless. If a string is input it must resolve to a unitless value. |
| Operation | [PartFeatureOperationEnum](../PartFeatureOperationEnum.md) | Input constant that indicates the type of operation to perform. Valid input is kJoinOperation, kCutOperation, kIntersectOperation, kSurfaceOperation. |
| AxisDirectionReversed | Boolean | Optional input Boolean that indicates a reversal of axis direction. The default is False, which means the axis direction will be in the same direction as the natural direction of the input axis entity. |
| ClockwiseRotation | Boolean | Optional input Boolean that defines whether the rotation of the coil is clockwise or counter-clockwise. The default is False, indicating counter-clockwise rotation.   This is an optional argument whose default value is False. |

## Version

Introduced in version 5.3
