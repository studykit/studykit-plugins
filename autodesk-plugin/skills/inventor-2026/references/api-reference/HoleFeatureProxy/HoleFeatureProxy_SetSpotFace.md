# HoleFeatureProxy.SetSpotFace Method

Parent Object: [HoleFeatureProxy](../HoleFeatureProxy/HoleFeatureProxy.md)

## Description

Method that changes the hole to be a spotface hole type. If the hole is already a spotface type you can access and modify the spotface parameters using the SpotFaceDiameter and SpotFaceDepth properties of the HoleFeature object. This method will fail of the hole contains a tapered thread.

## Syntax

HoleFeatureProxy.**SetSpotFace**( ***SpotFaceDiameter*** As Variant, ***SpotFaceDepth*** As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SpotFaceDiameter | Variant | Input Variant that defines the diameter of the spotface. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| SpotFaceDepth | Variant | Input Variant that defines the depth of the spotface. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |

## Version

Introduced in version 2008
