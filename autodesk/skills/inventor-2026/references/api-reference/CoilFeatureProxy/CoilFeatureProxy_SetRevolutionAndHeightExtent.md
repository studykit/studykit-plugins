# CoilFeatureProxy.SetRevolutionAndHeightExtent Method

Parent Object: [CoilFeatureProxy](../CoilFeatureProxy/CoilFeatureProxy.md)

## Description

Set coil feature revolution and height extent.

## Syntax

CoilFeatureProxy.**SetRevolutionAndHeightExtent**( ***Revolution*** As Variant, ***Height*** As Variant, [***TaperAngle***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Revolution | Variant | Input Variant that defines the number of revolutions of the coil feature. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, it is unitless. If a string is input it must resolve to a unitless value. |
| Height | Variant | Input Variant that defines the height of the coil feature. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| TaperAngle | Variant | Optional input variant that defines the taper angle of the coil feature. If not supplied it defaults to zero. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are radians. If a string is input, the units can be specified as part of the string or it will default to the current angle units of the document. |

## Version

Introduced in version 2008
