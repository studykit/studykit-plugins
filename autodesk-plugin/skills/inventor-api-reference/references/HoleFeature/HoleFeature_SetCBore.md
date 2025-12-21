# HoleFeature.SetCBore Method

Parent Object: [HoleFeature](../HoleFeature/HoleFeature.md)

## Description

Method that changes the hole to be a counterbore hole type. If the hole is already a counterbore type you can access and modify the counterbore parameters using the CBoreDiameter and CBoreDepth properties of the HoleFeature object.

## Syntax

HoleFeature.**SetCBore**( ***CBoreDiameter*** As Variant, ***CBoreDepth*** As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CBoreDiameter | Variant | Input Variant that defines the diameter of the counterbore. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units. |
| CBoreDepth | Variant | Input Variant that defines the depth of the counterbore. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |

## Version

Introduced in version 5
