# HemDefinition.SetSingleHemType Method

Parent Object: [HemDefinition](../HemDefinition/HemDefinition.md)

## Description

Method that changes the HemDefinition object to define a hem whose shape has a single bend.

## Syntax

HemDefinition.**SetSingleHemType**( ***Gap*** As Variant, ***Length*** As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Gap | Variant | Input Variant that defines the gap of the hem. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| Length | Variant | Input Variant that defines the length of the hem. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |

## Version

Introduced in version 2010
