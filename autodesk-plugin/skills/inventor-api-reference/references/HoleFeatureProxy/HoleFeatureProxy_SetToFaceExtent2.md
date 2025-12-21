# HoleFeatureProxy.SetToFaceExtent2 Method

Parent Object: [HoleFeatureProxy](../HoleFeatureProxy/HoleFeatureProxy.md)

## Description

Method that specifies the termination type for the hole feature. Hole features can be specified to terminate at a particular distance or object, or can be specified as through all, which means it extends through all faces of the feature. This method defines th.

## Syntax

HoleFeatureProxy.**SetToFaceExtent2**( ***ToFace*** As Object, ***ExtendToFace*** As Boolean, [***DrillPointType***] As Variant, [***BottomTipAngle***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ToFace | Object | Input Object that defines the to face. This can be either a Face or WorkPlane object. |
| ExtendToFace | Boolean | Input Boolean that defines whether the “to face” should be extended to contain the extents of the profile. |
| DrillPointType | Variant | Optional input DrillPointTypeEnum that specifies the drill point of the hole. If specifies an angled drill point then the BottomTipAngle argument needs to be provided to specify the angle. The default value is kFlatDrillPointType. |
| BottomTipAngle | Variant | Optional input Variant that defines the angle of the tip at the bottom of a hole. This argument is only used when the DrillPointType argument is kAngledDrillPointType, kAngledVDrillPointType or kAngledYDrillPointType. If this argument is not supplied a default value of 118 degrees is assigned.    This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are radians. If a string is input, the units can be specified as part of the string or it will default to the current angle units of the document.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2025
