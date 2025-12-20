# CornerRoundDefinition.AddEdgeSet Method

Parent Object: [CornerRoundDefinition](../CornerRoundDefinition/CornerRoundDefinition.md)

## Description

Method that creates a new edge set within the corner round definition.

## Syntax

CornerRoundDefinition.**AddEdgeSet**( ***CornerEdges*** As [EdgeCollection](../EdgeCollection/EdgeCollection.md), ***Radius*** As Variant ) As [CornerRoundEdgeSet](../CornerRoundEdgeSet/CornerRoundEdgeSet.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CornerEdges | [EdgeCollection](../EdgeCollection/EdgeCollection.md) | Input EdgesCollection object that contains all of the corners to apply a corner round on. Any non-corner edges will be ignored. |
| Radius | Variant | Input Variant that defines the corner radius. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |