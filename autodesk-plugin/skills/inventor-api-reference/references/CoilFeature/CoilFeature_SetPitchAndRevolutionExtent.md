# CoilFeature.SetPitchAndRevolutionExtent Method

Parent Object: [CoilFeature](../CoilFeature/CoilFeature.md)

## Description

Set coil feature pitch and revolution extent.

## Syntax

CoilFeature.**SetPitchAndRevolutionExtent**( ***Pitch*** As Variant, ***Revolution*** As Variant, [***TaperAngle***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Pitch | Variant | Input Variant that defines the pitch of the coil feature. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| Revolution | Variant | Input variant that defines the number of revolutions of the coil feature. |
| TaperAngle | Variant | Optional input variant that defines the taper angle of the coil feature. If not supplied it defaults to zero. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are radians. If a string is input, the units can be specified as part of the string or it will default to the current angle units of the document. |

## Version

Introduced in version 2008
