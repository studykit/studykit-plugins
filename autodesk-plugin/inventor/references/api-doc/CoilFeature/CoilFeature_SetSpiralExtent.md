# CoilFeature.SetSpiralExtent Method

Parent Object: [CoilFeature](../CoilFeature/CoilFeature.md)

## Description

Set coil feature spiral extent.

## Syntax

CoilFeature.**SetSpiralExtent**( ***Pitch*** As Variant, ***Revolution*** As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Pitch | Variant | Input Variant that defines the pitch of the coil feature. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| Revolution | Variant | Input Variant that defines the number of revolutions of the coil feature. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, it is unitless. If a string is input it must resolve to a unitless value. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |