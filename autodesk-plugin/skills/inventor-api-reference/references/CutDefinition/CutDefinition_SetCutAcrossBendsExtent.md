# CutDefinition.SetCutAcrossBendsExtent Method

Parent Object: [CutDefinition](../CutDefinition/CutDefinition.md)

## Description

Method that changes the cut to cut across bends.

## Remarks

Calling this method for a CutDefinition object that was obtained from an existing cut feature will cause the cut feature to update with the change.

## Syntax

CutDefinition.**SetCutAcrossBendsExtent**( ***Distance*** As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Distance | Variant | Input Variant that defines the depth of the cut. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |