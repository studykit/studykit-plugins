# HemDefinition.SetRolledHemType Method

Parent Object: [HemDefinition](../HemDefinition/HemDefinition.md)

## Description

Method that changes the HemDefinition object to define a hem whose shape has a rolled bend.

## Syntax

HemDefinition.**SetRolledHemType**( ***Radius*** As Variant, ***Angle*** As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Radius | Variant | Input Variant that defines the radius of the hem. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| Angle | Variant | Input Variant that defines the angle of the hem. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are radians. If a string is input, the units can be specified as part of the string or it will default to the current angle units of the document. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |