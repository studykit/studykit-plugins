# FlangeDefinition.SetToHeightExtent Method

Parent Object: [FlangeDefinition](../FlangeDefinition/FlangeDefinition.md)

## Description

Method that changes the FlangeDefinition object to define a flange whose height is defined by extending to the specified entity.

## Syntax

FlangeDefinition.**SetToHeightExtent**( ***ToEntity*** As Object, [***Offset***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ToEntity | Object | Input Object that defines the 'To' point. A WorkPoint or Vertex object is valid for input. |
| Offset | Variant | Optional Input Variant that defines the offset distance from the 'To' point. The default value is zero. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |