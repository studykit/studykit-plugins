# CoilFeatures.AddByRevolutionAndHeight Method

Parent Object: [CoilFeatures](../CoilFeatures/CoilFeatures.md)

## Description

Method that creates a new CoilFeature whose extent is defined by specifying the number of revolutions and the total height. The new CoilFeature is returned.

## Syntax

CoilFeatures.**AddByRevolutionAndHeight**( ***Profile*** As [Profile](../Profile/Profile.md), ***AxisEntity*** As Object, ***Revolution*** As Variant, ***Height*** As Variant, ***Operation*** As [PartFeatureOperationEnum](../PartFeatureOperationEnum.md), [***AxisDirectionReversed***] As Boolean, [***ClockwiseRotation***] As Boolean, [***TaperAngle***] As Variant, [***FlatStartType***] As Boolean, [***StartTransitionAngle***] As Variant, [***StartFlatAngle***] As Variant, [***FlatEndType***] As Boolean, [***EndTransitionAngle***] As Variant, [***EndFlatAngle***] As Variant ) As [CoilFeature](../CoilFeature/CoilFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Profile | [Profile](../Profile/Profile.md) | Input object used to define the shape of the coil. |
| AxisEntity | Object | Input linear entity that defines the axis of the revolution. Valid input is either a sketch line or work axis. The axis entity must not intersect the input profile. |
| Revolution | Variant | Input Variant that defines the number of revolutions of the coil feature. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, it is unitless. If a string is input it must resolve to a unitless value. |
| Height | Variant | Input Variant that defines the height of the coil feature. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| Operation | [PartFeatureOperationEnum](../PartFeatureOperationEnum.md) | Input constant that indicates the type of operation to perform. Valid input is kJoinOperation, kCutOperation, kIntersectOperation, kSurfaceOperation. |
| AxisDirectionReversed | Boolean | Optional input Boolean that indicates a reversal of axis direction. The default is False, which means the axis direction will be in the same direction as the natural direction of the input axis entity. |
| ClockwiseRotation | Boolean | Optional input Boolean that defines whether the rotation of the coil is clockwise or counter-clockwise. The default is False, indicating counter-clockwise rotation.   This is an optional argument whose default value is False. |
| TaperAngle | Variant | Optional input Variant that defines the taper angle of the coil feature. If this argument is not supplied it defaults to zero. It can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are radians. If a string is input, the units can be specified as part of the string or it will default to the current angle units of the document.   This is an optional argument whose default value is 0. |
| FlatStartType | Boolean | Optional input Boolean that indicates the coil's end type. The default is False indicating a natural end type. True indicates a flat start type.   This is an optional argument whose default value is False. |
| StartTransitionAngle | Variant | Optional input Variant that defines the transition angle for the coil's end. This argument is used only if FlatStartType is True, otherwise it is ignored. The default value for this argument is p/2 (90 degrees). It can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are radians. If a string is input, the units can be specified as part of the string or it will default to the current angle units of the document.   This is an optional argument whose default value is null. |
| StartFlatAngle | Variant | Optional input Variant that defines the flat angle for the coil's end. This argument is used only if FlatStartType is True, otherwise it is ignored. The default value for this argument is p/2 (90 degrees). It can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are radians. If a string is input, the units can be specified as part of the string or it will default to the current angle units of the document.   This is an optional argument whose default value is null. |
| FlatEndType | Boolean | Optional input Boolean that indicates the coil's end type. The default is False indicating a natural end type. True indicates a flat end type.   This is an optional argument whose default value is False. |
| EndTransitionAngle | Variant | Optional input Variant that defines the transition angle for the coil's end. This argument is used only if FlatEndType is True, otherwise it is ignored. The default value for this argument is p/2 (90 degrees). It can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are radians. If a string is input, the units can be specified as part of the string or it will default to the current angle units of the document.   This is an optional argument whose default value is null. |
| EndFlatAngle | Variant | Optional input Variant that defines the flat angle for the coil's end. This argument is used only if FlatEndType is True, otherwise it is ignored. The default value for this argument is p/2 (90 degrees). It can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are radians. If a string is input, the units can be specified as part of the string or it will default to the current angle units of the document.   This is an optional argument whose default value is null. |

## Version

Introduced in version 5.3
