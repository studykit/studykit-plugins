# HemDefinition.SetWidthOffsetWidthExtent Method

Parent Object: [HemDefinition](../HemDefinition/HemDefinition.md)

## Description

Method that changes the ContourFlangeDefinition object to define a hem whose width is defined relative to another entity.

## Syntax

HemDefinition.**SetWidthOffsetWidthExtent**( ***Width*** As Variant, ***OffsetDistance*** As Variant, ***OffsetEntity*** As Object, ***PositiveDirection*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Width | Variant | Input Variant that defines the distance to use for the width extent of the hem. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| OffsetDistance | Variant | Input Variant that defines the distance of the hem from the offset entity. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| OffsetEntity | Object | Input Object that defines the entity the distance is measured relative to. This can be a point (WorkPoint or a Vertex object) or a plane (Face or WorkPlane object that is perpendicular to the selected edge). |
| PositiveDirection | Boolean | Input Boolean that specifies the side of the offset entity the hem is on. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |