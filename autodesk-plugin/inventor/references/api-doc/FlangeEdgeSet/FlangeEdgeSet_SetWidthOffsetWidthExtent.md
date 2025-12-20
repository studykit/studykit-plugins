# FlangeEdgeSet.SetWidthOffsetWidthExtent Method

Parent Object: [FlangeEdgeSet](../FlangeEdgeSet/FlangeEdgeSet.md)

## Description

Method that sets the width extent of the specified physical flange to define a flange whose width is defined relative to another entity.

## Syntax

FlangeEdgeSet.**SetWidthOffsetWidthExtent**( ***Width*** As Variant, ***OffsetDistance*** As Variant, ***OffsetEntity*** As Object, ***PositiveDirection*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Width | Variant | Input Variant that defines the distance used for the width extent of the flange.  This value is used to define that distance. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| OffsetDistance | Variant | Input Variant that defines the distance of the flange from the offset entity.  This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| OffsetEntity | Object | Input Object that defines the entity the distance is measured relative to. This can be a point (WorkPoint or a Vertex object) or a plane (Face or WorkPlane object that is perpendicular to the selected edge). |
| PositiveDirection | Boolean | Input Boolean that specifies the side of the offset entity the flange is on. |

## Version

Introduced in version 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |